package control;

import model.Client;
import model.ContBancar;
import model.ContEURO;
import model.ContRON;

import java.io.FileNotFoundException;
import java.util.ArrayList;

public class GhiseuBancar {
    public static void main(String[] args) {

        ContEURO contEURO1 = new ContEURO(507.45);
        //System.out.println(contEURO);
        ContRON contRON1 = new ContRON(2400.45);
        //System.out.println(contRON);

        ArrayList<ContBancar> listaConturi1 = new ArrayList<>();//123
        listaConturi1.add(contEURO1);
        listaConturi1.add(contRON1);

        ArrayList<ContBancar> listaConturi2 = new ArrayList<>();
        listaConturi2.add(new ContEURO(507.54));
        listaConturi2.add(new ContRON(3243));

        Client client1 = new Client("Maria", "Vacaresti 189", listaConturi1);
        Client client2 = new Client("Ioana", "Academiei 189", listaConturi2);

    
    }
}
