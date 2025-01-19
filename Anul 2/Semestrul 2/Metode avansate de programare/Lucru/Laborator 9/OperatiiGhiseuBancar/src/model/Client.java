package model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Client {
    private String nume;
    private String adresa;

    //asociere
    private List<ContBancar> listaConturi;


    public Client(String nume, String adresa, ArrayList<ContBancar> listaConturi) {
        this.nume = nume;
        this.adresa = adresa;
        //compozitie deep
        this.listaConturi = new ArrayList<>();//234
        for(int i=0; i<listaConturi.size(); i++)
        {
            try {
                this.listaConturi.add((ContBancar) listaConturi.get(i).clone());
            } catch (CloneNotSupportedException e) {
                throw new RuntimeException(e);
            }
        }
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

    public List<ContBancar> getListaConturi() {
        return listaConturi;
    }

    public void setListaConturi(ArrayList<ContBancar> listaConturi) {
        this.listaConturi = listaConturi;
    }

    @Override
    public String toString() {
        return "Client{" +
                "nume='" + nume + '\'' +
                ", adresa='" + adresa + '\'' +
                ", listaConturi=" + listaConturi +
                '}';
    }
}
