import java.awt.*;
import javax.swing.*;
public class Ex2
{
    public static void main(String[] args)
    {
        JFrame f=new JFrame("Dispunere cu BorderLayout");
        Container cp=f.getContentPane();
        cp.setLayout(new BorderLayout());
        cp.add(new JLabel("Nord"),BorderLayout.NORTH);
        cp.add(new JLabel("Sud"),BorderLayout.SOUTH);
        cp.add(new JButton("Est"),BorderLayout.EAST);
        cp.add(new JButton("Vest"),BorderLayout.WEST);
        cp.add(new JTextField("Centru"),BorderLayout.CENTER);
        // f.setSize(300,200);
        f.pack();
        f.setVisible(true);
    }
}