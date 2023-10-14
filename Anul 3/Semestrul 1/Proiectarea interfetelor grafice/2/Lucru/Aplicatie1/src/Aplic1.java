import javax.swing.*;

public class Aplic1{
    public static void main(String[] args){
        JFrame win = new JFrame("Seminar 1 - 2023");
        //win.setSize(300,200);
        win.pack();
        win.setLocation(20,20);
        win.setResizable(true);
        win.getContentPane().add(new JLabel("Utilizare Swing"));
        win.setVisible(true);
    }
}