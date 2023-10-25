import javax.swing.*;
import java.awt.*;

class Butoane extends JPanel {
    public Butoane() {
        JButton b1 = new JButton("Seria A");
        Button b2 = new Button("Seria B");
        this.setLayout(new GridLayout(1, 0));
        add(b1);
        add(b2);
    }
}

class ButoaneRadio extends JPanel {
    public ButoaneRadio() {
        // Create radio buttons
        JRadioButton butonAlb = new JRadioButton("var 1 10-18");
        butonAlb.setSelected(true);
        JRadioButton butonRosu = new JRadioButton("var 2 10-18");

        // Group the radio buttons
        ButtonGroup group = new ButtonGroup();
        group.add(butonAlb);
        group.add(butonRosu);

        // Add the radio buttons to this panel
        add(butonAlb);
        add(butonRosu);
    }
}

class ListBox1 extends JScrollPane {
    private JList<String> list;

    public JList<String> getList() {
        return list;
    }

    public ListBox1() {
        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("Randul 1");
        listModel.addElement("Randul 2");
        listModel.addElement("Randul 3");
        list = new JList<>(listModel);
        list.setVisibleRowCount(3);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        list.setSelectedIndex(0);
        setViewportView(list);
    }
}

public class DesenAplicatie extends JFrame {
    public static void main(String[] args) {
        DesenAplicatie app = new DesenAplicatie();
        Butoane panouButoane = new Butoane();
        ButoaneRadio panouButoaneRadio = new ButoaneRadio();
        ListBox1 panouListe = new ListBox1();
        JPanel panou = new JPanel();
        panou.add(panouButoane);
        panou.add(panouButoaneRadio);
        panou.add(panouListe);
        app.getContentPane().add(panou);
        app.pack();
        app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        app.setVisible(true);
    }
}