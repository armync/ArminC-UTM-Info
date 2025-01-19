package model;

import java.util.Random;

import static model.Constants.DOBANDA_EURO;

public class ContEURO extends ContBancar{
    private static double dobanda = DOBANDA_EURO;

    public ContEURO(double suma) {
        super(suma);
        this.setNumarCont(construiesteNumarCont());
    }
    private String construiesteNumarCont() {
        StringBuilder cont = new StringBuilder();
        cont.append("ROBCR");
        cont.append(TipCont.EURO); // sau TipCont.RON în funcție de tipul de cont
        Random random = new Random();
        int numar = 1000 + random.nextInt(8999);
        cont.append(numar);

        return cont.toString();
    }

    public double getDobanda() {
        if (this.getSuma() < Constants.SUMA_CONT_EURO_MINIMA) {
            return 0.0;
        } else {
            return this.getSuma() * DOBANDA_EURO;
        }
    }

    @Override
    public String toString() {
        return "ContEURO " + ContEURO.dobanda + " "+ super.toString();
    }
}
