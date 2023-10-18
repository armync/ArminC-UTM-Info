import java.awt.*;
import javax.swing.*;

public class Main
{
    public static void main(String[] args)
    {
        JFrame f=new JFrame("Dispunere cu FlowLayout");
        JButton b1=new JButton("1");
        JButton b2=new JButton("2");
        JButton b3=new JButton("3");
        JButton b4=new JButton("4");
        JButton b5=new JButton("5");
        JButton b6=new JButton("6");
        Container cp=f.getContentPane();
        cp.setLayout(new FlowLayout());
        cp.add(b1);
        cp.add(b2);
        cp.add(b3);
        cp.add(b4);
        cp.add(b5);
        cp.add(b6);
        // f.setSize(200,100);
        f.pack();
        f.setVisible(true);
    }
}