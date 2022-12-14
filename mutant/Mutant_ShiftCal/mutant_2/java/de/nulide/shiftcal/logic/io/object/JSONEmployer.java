package de.nulide.shiftcal.logic.io.object;

public class JSONEmployer {

    private String name;
    private int id;
    private boolean archived;

    public JSONEmployer() {
    }

    public JSONEmployer(String name, int id, boolean archived) {
        this.name = name;
        this.id = id;
        this.archived = archived;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public boolean isArchived() {
        return archived;
    }

    public void setArchived(boolean archived) {
        this.archived = archived;
    }
}
