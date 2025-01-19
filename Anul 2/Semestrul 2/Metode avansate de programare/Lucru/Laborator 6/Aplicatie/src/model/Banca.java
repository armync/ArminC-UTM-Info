package model;

import java.util.ArrayList;
import java.util.Collections;

public class Banca {
    //HAS_A
    private ArrayList<Client> clienti;
    private String denumire;

    public Banca(ArrayList<Client> clienti, String denumire) {
        //compozitie
        this.clienti = new ArrayList<>();
        Collections.copy(this.clienti, clienti);
        this.denumire = denumire;
    }

    public ArrayList<Client> getClienti() {
        return clienti;
    }

    public void setClienti(ArrayList<Client> clienti) {
        this.clienti = clienti;
    }

    public String getDenumire() {
        return denumire;
    }

    public void setDenumire(String denumire) {
        this.denumire = denumire;
    }

    @Override
    public String toString() {
        return "Banca{" +
                "clienti=" + clienti +
                ", denumire='" + denumire + '\'' +
                '}';
    }

    public void addClient(Client client)
    {
        this.clienti.add(client);
    }
    public void afisareClient(Client client)
    {
         for(int i=0; i<clienti.size(); i++)
             if(client.equals(clienti.get(i))) {
                 System.out.println(client);
                 break;
             }
    }
}
