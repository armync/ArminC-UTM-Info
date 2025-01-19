package model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Client {
    private String nume;
    private String adresa;

    //HAS_A
    private ArrayList<ContBancar> conturi;

    public Client(String nume, String adresa, ArrayList<ContBancar> conturi) {
        this.nume = nume;
        this.adresa = adresa;
        //cpmpozitia
        this.conturi = new ArrayList<>();
        Collections.copy( this.conturi, conturi);
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

    public ArrayList<ContBancar> getConturi() {
        return conturi;
    }

    public void setConturi(ArrayList<ContBancar> conturi) {
        this.conturi = conturi;
    }

    @Override
    public String toString() {
        return "Client{" +
                "nume='" + nume + '\'' +
                ", adresa='" + adresa + '\'' +
                ", conturi=" + conturi +
                '}';
    }
}
