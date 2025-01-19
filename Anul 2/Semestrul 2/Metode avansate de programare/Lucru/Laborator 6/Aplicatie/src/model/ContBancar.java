package model;

import java.util.Random;

public abstract class ContBancar {
    private String numarCont;
    private double suma;

    public ContBancar(double suma) {
        this.numarCont = getStringBuilder().toString();
        this.suma = suma;
    }

    public ContBancar() {
        this.numarCont = getStringBuilder().toString();
        this.suma = Constants.SUMA_MINIMA_DC;
    }

    private  StringBuilder getStringBuilder() {
        StringBuilder sb = new StringBuilder();
        sb.append("ROBCR");
        Random gen = new Random();
        int x = 1000 + gen.nextInt(100000);
        sb.append(x);
        return sb;
    }

    public String getNumarCont() {
        return numarCont;
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
}
