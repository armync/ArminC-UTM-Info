package clase_social_network;

public class User {
    private String nume;
    private String adresa;
    private String vârstă;

    //asociere
    private Profil profil;

    public User(String nume, String adresa, String vârstă, Profil profil) {
        this.nume = nume;
        this.adresa = adresa;
        this.vârstă = vârstă;

        //compozitie
        this.profil = new Profil(profil.getPosts());
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getAdresa() {
        return adresa;
    }

    public void setAdresa(String adresa) {
        this.adresa = adresa;
    }

    public String getVârstă() {
        return vârstă;
    }

    public void setVârstă(String vârstă) {
        this.vârstă = vârstă;
    }

    public Profil getProfil() {
        return profil;
    }

    public void setProfil(Profil profil) {
        this.profil = profil;
    }

    @Override
    public String toString() {
        return "User{" +
                "nume='" + nume + '\'' +
                ", adresa='" + adresa + '\'' +
                ", vârstă='" + vârstă + '\'' +
                ", profil=" + profil +
                '}';
    }

}
