package de.nulide.shiftcal.logic.io.object;

import java.util.ArrayList;
import java.util.List;

public class JSONEmployment {
    private List<JSONEmployer> employers;

    public JSONEmployment() {
        employers = new ArrayList<>();
    }

    public List<JSONEmployer> getEmployers() {
        return employers;
    }

    public void setEmployers(List<JSONEmployer> employers) {
        this.employers = employers;
    }
}
