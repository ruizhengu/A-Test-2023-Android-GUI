package de.nulide.shiftcal;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.content.res.ColorStateList;
import android.os.Bundle;
import android.util.Log;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;

import de.nulide.shiftcal.logic.io.IO;
import de.nulide.shiftcal.logic.object.Employer;
import de.nulide.shiftcal.logic.object.Employment;
import de.nulide.shiftcal.logic.object.Settings;
import de.nulide.shiftcal.sync.SyncHandler;
import de.nulide.shiftcal.tools.ColorHelper;
import de.nulide.shiftcal.ui.EmployerAdapter;

public class EmployersActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemClickListener {

    static Employment em;
    private ListView listViewEmployers;
    private ArrayList<Employer> employers;
    private FloatingActionButton fabAddEmployer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_employers);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Settings settings = IO.readSettings(getFilesDir());
        int color = ColorHelper.changeActivityColors(this, toolbar, settings);

        fabAddEmployer = findViewById(R.id.fabAddEmployer);
        fabAddEmployer.setBackgroundTintList(ColorStateList.valueOf(color));
        fabAddEmployer.setOnClickListener(this);

        listViewEmployers = findViewById(R.id.listViewEmployers);
        registerForContextMenu(listViewEmployers);
        listViewEmployers.setOnItemClickListener(this);
    }

    public void updateEmployers() {
        em = IO.readEmployment(getFilesDir());
        employers = new ArrayList<>(em.getEmployerList());
        EmployerAdapter adapter = new EmployerAdapter(this, employers);
        listViewEmployers.setAdapter(adapter);
    }

    @Override
    public void onClick(View view) {
        Intent myIntent = new Intent(this, EmployerCreatorActivity.class);
        myIntent.putExtra("toEditEmployer", -1);
        startActivity(myIntent);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        Intent myIntent = new Intent(this, EmployerCreatorActivity.class);
        myIntent.putExtra("toEditEmployer", employers.get(i).getId());
        startActivity(myIntent);
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        menu.setHeaderTitle("Select The Action");
        menu.add(0, v.getId(), 0, "Edit");
        menu.add(0, v.getId(), 0, "Delete");
        menu.add(0, v.getId(), 0, "Archive");
    }

    @Override
    public boolean onContextItemSelected(MenuItem item) {
        AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
        int index = info.position;
        if (item.getTitle() == "Edit") {
            Intent myIntent = new Intent(this, EmployerCreatorActivity.class);
            myIntent.putExtra("toEditEmployer", employers.get(index).getId());
            startActivity(myIntent);
        } else if (item.getTitle() == "Delete") {
            em.deleteEmployer(employers.get(index).getId());
            IO.writeEmployment(getFilesDir(), this, em);
            SyncHandler.sync(this);
            updateEmployers();
        } else if (item.getTitle() == "Archive") {
            Employer employer = employers.get(index);
            employer.setArchived();
            em.setEmployer(employer.getId(), employer);
            IO.writeEmployment(getFilesDir(), this, em);
            updateEmployers();
        } else {
            return false;
        }
        return true;
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateEmployers();
    }
}