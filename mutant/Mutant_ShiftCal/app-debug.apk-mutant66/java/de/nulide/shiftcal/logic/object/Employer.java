package de.nulide.shiftcal.logic.object;

public class Employer {
    private String name;
    private int id;
    private boolean archived;

    public Employer(String name, int id, boolean archived) {
        this.name = name;
        this.id = id;
        this.archived = archived;
    }

    public Employer() {
        this.name = "Error";
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
        return this.archived;
    }

    public void setArchived() {
        this.archived = true;
    }
}
