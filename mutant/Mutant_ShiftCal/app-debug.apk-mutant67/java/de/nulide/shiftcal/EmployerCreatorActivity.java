package de.nulide.shiftcal;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.res.ColorStateList;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import de.nulide.shiftcal.logic.io.IO;
import de.nulide.shiftcal.logic.object.Employer;
import de.nulide.shiftcal.logic.object.Employment;
import de.nulide.shiftcal.logic.object.Settings;
import de.nulide.shiftcal.logic.object.ShiftCalendar;
import de.nulide.shiftcal.tools.ColorHelper;

public class EmployerCreatorActivity extends AppCompatActivity implements View.OnClickListener {

    private Employment em;
    private int toEditEmployer = -1;
    private EditText etViewName;
    private FloatingActionButton fabDoneEmployer;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_employer_creator);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Settings settings = IO.readSettings(getFilesDir());
        int color = ColorHelper.changeActivityColors(this, toolbar, settings);

        Bundle bundle = getIntent().getExtras();
        toEditEmployer = bundle.getInt("toEditEmployer");

        em = IO.readEmployment(getFilesDir());

        fabDoneEmployer = findViewById(R.id.fabDoneEmployer);
        fabDoneEmployer.setOnClickListener(this);
        fabDoneEmployer.setBackgroundTintList(ColorStateList.valueOf(color));
        etViewName = findViewById(R.id.scEditTextName);

        if (toEditEmployer != -1) {
            etViewName.setText(em.getEmployerByIndex(toEditEmployer).getName());
        }
    }

    @Override
    public void onClick(View view) {
        if (view == fabDoneEmployer) {
            String name = etViewName.getText().toString();

            if (!name.isEmpty()) {
                Employer nE = new Employer(name, em.getNextEmployerId(), false);
                if (toEditEmployer != -1) {
                    nE.setId(em.getEmployerById(toEditEmployer).getId());
                    em.setEmployer(toEditEmployer, nE);
                } else {
                    em.addEmployer(nE);
                }
                IO.writeEmployment(getFilesDir(), this, em);
                this.finish();
            } else {
                Snackbar.make(view, "Error: Not enough Information!", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        }
    }
}