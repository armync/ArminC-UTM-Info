package model;

public class ContRON extends ContBancar implements SumaTotala{
    public void transfer(ContRON contRON, double suma)
    {
        if(this.getSuma()>=suma) {
            this.setSuma(this.getSuma() - suma);
            contRON.setSuma(contRON.getSuma() +suma);
        }
            System.out.println("Fonduri insuficiente!!!");
    }

    @Override
    public double getSumaTotala() {
        return this.getSuma();
    }
}
