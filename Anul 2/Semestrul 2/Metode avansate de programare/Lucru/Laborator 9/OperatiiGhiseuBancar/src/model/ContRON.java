package model;

import java.util.Random;

public class ContRON extends ContBancar{
    public ContRON(double suma) {
        super(suma);
        this.setNumarCont(construiesteNumarCont());
    }
    private String construiesteNumarCont() {
        StringBuilder cont = new StringBuilder();
        cont.append(this.getNumarCont());
        cont.append(TipCont.RON);
        Random random  = new Random();
        int numar = 1000 + random.nextInt(8999);
        cont.append((numar));

        return cont.toString();
    }

    public void transfer(ContRON contDestinatie, double suma)
    {
        this.setSuma(this.getSuma() - suma);
        contDestinatie.setSuma(contDestinatie.getSuma() + suma);
    }

    @Override
    public String toString() {
        return "ContRON " + super.toString();
    }
}
