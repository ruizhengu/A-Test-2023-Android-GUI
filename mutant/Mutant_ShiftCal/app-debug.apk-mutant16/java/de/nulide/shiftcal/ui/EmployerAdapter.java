package de.nulide.shiftcal.ui;

import android.content.Context;
import android.graphics.Typeface;
import android.text.Layout;
import android.util.TypedValue;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.ArrayList;

import de.nulide.shiftcal.R;
import de.nulide.shiftcal.logic.object.Employer;

public class EmployerAdapter extends ArrayAdapter<Employer> {

    private final Context context;
    private final ArrayList<Employer> employers;

    public EmployerAdapter(@NonNull Context context, ArrayList<Employer> employers) {
        super(context, R.layout.row_employer, employers);
        this.context = context;
        this.employers = employers;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        View rowView = inflater.inflate(R.layout.row_employer, parent, false);

        TextView tvName = rowView.findViewById(R.id.textViewName);

        tvName.setText(employers.get(position).getName());
        tvName.setTextSize(TypedValue.COMPLEX_UNIT_SP, 39f);
        tvName.setTypeface(null, Typeface.BOLD);

        return rowView;
    }
}
