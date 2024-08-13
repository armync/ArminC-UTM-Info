package surse;

public class AngajatBestIT {
    private String nume, functie;
    private int varsta;
    private double salariu;

    public AngajatBestIT(String nume, String functie, int varsta, double salariu) {
        this.nume = nume;
        this.functie = functie;
        this.varsta = varsta;
        this.salariu = salariu;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getFunctie() {
        return functie;
    }

    public void setFunctie(String functie) {
        this.functie = functie;
    }

    public int getVarsta() {
        return varsta;
    }

    public void setVarsta(int varsta) {
        this.varsta = varsta;
    }

    public double getSalariu() {
        return salariu;
    }

    public void setSalariu(double salariu) {
        this.salariu = salariu;
    }

    @Override
    public String toString() {
        return "AngajatBestIT{" +
                "nume='" + nume + '\'' +
                ", functie='" + functie + '\'' +
                ", varsta=" + varsta +
                ", salariu=" + salariu +
                '}';
    }
}
