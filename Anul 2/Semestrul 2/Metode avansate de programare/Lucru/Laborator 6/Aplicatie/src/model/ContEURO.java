package model;

public class ContEURO extends ContBancar implements SumaTotala{
    private static double dobanda = 0.03;

    public double getDobandaSold()
    {
        return this.getSuma()*dobanda;
    }

    public static double getDobanda() {
        return dobanda;
    }

    public static void setDobanda(double dobanda) {
        ContEURO.dobanda = dobanda;
    }

    @Override
    public String toString() {
        return "ContEURO " + super.toString() + " " + ContEURO.dobanda;
    }

    @Override
    public double getSumaTotala() {
        return this.getSuma()*Constants.EURO_RON;
    }
}
