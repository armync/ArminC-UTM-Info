import java.awt.*;
import javax.swing.*;
public class Ex3
{
    public static void main(String[] args)
    {
        JFrame f=new JFrame("Dispunere cu GridLayout");
        Container cp=f.getContentPane();
        cp.setLayout(new GridLayout(1,10));
        cp.add(new JButton("1"));
        cp.add(new JButton("2"));
        cp.add(new JButton("3"));
        cp.add(new JButton("4"));
        cp.add(new JButton("5"));
        cp.add(new JButton("6"));
        cp.add(new JButton("7"));
        cp.add(new JButton("8"));
        cp.add(new JButton("9"));
        cp.add(new JButton("10"));
        cp.add(new JButton("11"));
        f.setSize(300,200);
        f.setLocation(100,100);
        f.setVisible(true);
    }
}