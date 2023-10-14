import javax.swing.*;
import javax.swing.border.TitledBorder; // imports TitledBorder class (no package and its subpackages)

public class Main extends JFrame {
    JComponent comp = new JLabel("Test label");

public Main(){
    comp.setBorder(new TitledBorder("Titlu border"));
        getContentPane().add(comp);
            setSize(250,250);
        setVisible(true);
}

public static void main(String[] arg){
    new Main();
    }
}