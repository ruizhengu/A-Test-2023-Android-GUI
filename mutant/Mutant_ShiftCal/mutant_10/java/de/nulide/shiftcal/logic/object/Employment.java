package de.nulide.shiftcal.logic.object;

import android.util.Log;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Employment {
    private List<Employer> employers;
    private int nextEmployerId;

    public Employment() {
        employers = new ArrayList<>();
        nextEmployerId = 0;
    }

    public List<Employer> getEmployerList() {
        List<Employer> employers = new LinkedList<Employer>();
        for (Employer e : this.employers) {
            if (!e.isArchived()) {
                employers.add(e);
            }
        }
        return employers;
    }

    public Employer getEmployerById(int id) {
        Employer e = new Employer();
        for (int i = 0; i < employers.size(); i++) {
            if (employers.get(i).getId() == id) {
                return employers.get(i);
            }
        }
        return e;
    }

    public Employer getEmployerByIndex(int i) {
        return employers.get(i);
    }

    public void deleteEmployer(int id) {
        for (int i = 0; i < employers.size(); i++) {
            if (employers.get(i).getId() == id) {
                employers.remove(i);
                return;
            }
        }
    }

    public void setEmployer(int id, Employer e) {
        for (int i = 0; i < employers.size(); i++) {
            if (employers.get(i).getId() == id) {
                employers.set(i, e);
                return;
            }
        }
    }

    public void addEmployer(Employer e) {
        employers.add(e);
        if (e.getId() >= nextEmployerId) {
            nextEmployerId = e.getId() + 1;
        }
    }

    public int getEmployersSize() {
        return employers.size();
    }

    public int getNextEmployerId() {
        return nextEmployerId;
    }
}
