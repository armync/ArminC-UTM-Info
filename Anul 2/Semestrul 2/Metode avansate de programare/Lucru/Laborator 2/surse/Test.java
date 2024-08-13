package surse;

public class Test {
    public static void main(String[] args) {
        AngajatBestIT []ang = new AngajatBestIT[3];

        ang[0] = new AngajatBestIT("Popescu Ioan", "Programator C++",
                23, 5000.50);
        ang[1] = new AngajatBestIT("Popa Ana", "Programator Python",
                27, 6000.50);
        ang[2] = new AngajatBestIT("Mihai George", "Programator Java",
                21, 4000.50);

        System.out.println("Angajatii din internship:");
        for(int i = 0; i < ang.length; i++)
            if(ang[i].getVarsta() <= 25)
                System.out.println(ang[i]);
    }
}
