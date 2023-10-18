import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
public class A1 extends JPanel {

    public A1()
    {
        JRadioButton r1_Yes = new JRadioButton("Yes  ?",true);
        JRadioButton r1_No = new JRadioButton("No  ?",false);


        ButtonGroup radioGroup1 = new ButtonGroup();
        ButtonGroup radioGroup2 = new ButtonGroup();
        setLayout(null);
        add(r1_Yes);
        add(r1_No);

        radioGroup1.add(r1_Yes);
        radioGroup1.add(r1_No);

        r1_Yes.setBounds(10,10,80,60);
        r1_No.setBounds(80,30,80,20);


        JRadioButton buton1 = new JRadioButton("Buton1",true);
        JRadioButton buton2 = new JRadioButton("Buton2",false);

        add(buton1);
        add(buton2);
        buton1.setBounds(10,90,100,70);
        buton2.setBounds(80,90,100,70);

        radioGroup2.add(buton1);
        radioGroup2.add(buton2);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.getContentPane().add(new A1());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,300);
        frame.setVisible(true);
    }
}