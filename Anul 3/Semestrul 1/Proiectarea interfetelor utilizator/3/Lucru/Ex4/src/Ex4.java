import java.awt.*;
import javax.swing.*;
public class Ex4
{
    public static void main(String[] args)
    {
        JFrame f=new JFrame("Dispunere cu GridLayout");
        Container cp=f.getContentPane();
        cp.setLayout(new GridLayout(3,2));
        cp.add(new JButton("1"));
        cp.add(new JButton("2"));
        cp.add(new JButton("3"));
        cp.add(new JButton("4"));
        cp.add(new JButton("5"));
        cp.add(new JButton("6"));
        f.setSize(300,200);
        f.setVisible(true);
        cp.add(new JButton("7"));
        cp.add(new JButton("8"));
        if(!cp.isValid())
            cp.validate();
    }
}