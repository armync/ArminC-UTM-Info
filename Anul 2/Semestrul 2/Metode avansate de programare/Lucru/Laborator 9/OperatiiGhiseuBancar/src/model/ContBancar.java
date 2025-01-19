package model;

import java.util.Random;

public abstract class ContBancar implements Cloneable{
    private String numarCont;
    private double suma;

    public ContBancar(double suma) {
        this.suma = suma;
        this.numarCont = "ROBCR";
    }
    public ContBancar() {
    }

    public String getNumarCont() {
        return numarCont;
    }

    public void setNumarCont(String numarCont) {
        this.numarCont = numarCont;
    }

    public double getSuma() {
        return suma;
    }

    public void setSuma(double suma) {
        this.suma = suma;
    }

    @Override
    public String toString() {
        return "ContBancar{" +
                "numarCont='" + numarCont + '\'' +
                ", suma=" + suma +
                '}';
    }

    //protected abstract String construiesteCont();
    //operatii

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public void tranzactie(TranzactieCont tranzactieCont, double suma)
    {
        switch (tranzactieCont)
        {
           case ALIMENTARE:
                alimentare(suma);
               break;
            case RETRAGERE:
                retargere(suma);
                break;
        }
    }

    private void retargere(double suma) {
        this.suma-=suma;
    }

    private void alimentare(double suma) {
        this.suma+=suma;
    }
}
