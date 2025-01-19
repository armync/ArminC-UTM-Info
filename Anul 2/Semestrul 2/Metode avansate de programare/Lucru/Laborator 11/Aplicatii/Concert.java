import java.util.Objects;

public class Concert {
    private String localitate;
    private String Denumire;
    private double pretBilet;
    private int numarLocuri;

    public Concert(String denumire, String localitate, double pretBilet, int numarLocuri) {
        this.localitate = localitate;
        Denumire = denumire;
        this.pretBilet = pretBilet;
        this.numarLocuri = numarLocuri;
    }

    @Override
    public String toString() {
        return "Concert{" +
                "localitate='" + localitate + '\'' +
                ", Denumire='" + Denumire + '\'' +
                ", pretBilet=" + pretBilet +
                ", numarLocuri=" + numarLocuri +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Concert concert = (Concert) o;
        return Double.compare(pretBilet, concert.pretBilet) == 0 &&
                numarLocuri == concert.numarLocuri               &&
                Objects.equals(localitate, concert.localitate)   &&
                Objects.equals(Denumire, concert.Denumire);
    }

    @Override
    public int hashCode() {
        return Objects.hash(localitate, Denumire, pretBilet, numarLocuri);
    }

    public String getLocalitate() {
        return localitate;
    }

    public void setLocalitate(String localitate) {
        this.localitate = localitate;
    }

    public String getDenumire() {
        return Denumire;
    }

    public void setDenumire(String denumire) {
        Denumire = denumire;
    }

    public double getPretBilet() {
        return pretBilet;
    }

    public void setPretBilet(double pretBilet) {
        this.pretBilet = pretBilet;
    }

    public int getNumarLocuri() {
        return numarLocuri;
    }

    public void setNumarLocuri(int numarLocuri) {
        this.numarLocuri = numarLocuri;
    }
}
