import javax.swing.*;
import java.awt.*;
public class Aplicatia4 extends JFrame
{
    public static void main(String args[])
    {
//creare obiecte
        Aplicatia4 app = new Aplicatia4();
        Butoane panouButoane = new Butoane();
        CheckBoxuri panouCheckBoxuri = new CheckBoxuri();
        ButoaneRadio panouButoaneRadio = new ButoaneRadio();
        ButoaneRadio2 panouButoaneRadio2 = new ButoaneRadio2();
        ListBox1 panouListe = new ListBox1();
        JPanel panou = new JPanel();
        panou.setLayout(new GridLayout(0, 1));
//radio
        JPanel radioPanou = new JPanel();
        panou.setLayout(new GridLayout(0, 1));
        radioPanou.add(panouButoaneRadio);
        radioPanou.add(panouButoaneRadio2);
//aduagare obiecte la panou
        panou.add(panouButoane);
        panou.add(panouCheckBoxuri);
        panou.add(radioPanou);
        panou.add(panouListe);
//functii
        app.getContentPane().add(panou);
        app.pack();
        app.setTitle("Armin Chanchian");
// app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        app.setVisible(true);
    }
}
class Butoane extends JPanel
{
    public Butoane()
    {
        JButton b1 = new JButton("ButonA");
        JButton b2 = new JButton("ButonB");
        JButton b3 = new JButton("ButonC");
        this.setLayout(new GridLayout(1,0));
        add(b1);
        add(b2);
        add(b3);
    }
}
class CheckBoxuri extends JPanel
{
    public CheckBoxuri()
    {
//cream butoane de tip checkBox
        JCheckBox cb1 = new JCheckBox("Optiune1");
        cb1.setSelected(true);//alegem ca primul buton sa fie bifat la pornire
        JCheckBox cb2 = new JCheckBox("Optiune2");
        JCheckBox cb3 = new JCheckBox("Optiune3");
        this.setLayout(new GridLayout(0,1));//dispunere de tip Grid
        add(cb1);//adaugam butonul b1
        add(cb2);//adaugam butonul b2
        add(cb3);//adaugam butonul b3
    }
}
class ButoaneRadio extends JPanel
{
    public ButoaneRadio()
    {
// Creare butoane radio
        JRadioButton butonAlb = new JRadioButton("Alb");
        butonAlb.setActionCommand("Alb");
        butonAlb.setSelected(true);
        JRadioButton butonRosu = new JRadioButton("Rosu");
        butonRosu.setActionCommand("Rosu");
        JRadioButton butonVerde = new JRadioButton("Verde");
        butonVerde.setActionCommand("Verde");
// Adaugarea butoanelor la grup
        ButtonGroup group = new ButtonGroup();
        group.add(butonAlb);
        group.add(butonRosu);
        group.add(butonVerde);
// Adaugarea butoanelor la Layout
        this.setLayout(new GridLayout(0,1));
        add(butonAlb);
        add(butonRosu);
        add(butonVerde);
    }
}

class ButoaneRadio2 extends JPanel
{
    public ButoaneRadio2()
    {
// Creare butoane radio
        JRadioButton butonSus = new JRadioButton("Sus");
        butonSus.setActionCommand("Sus");
        butonSus.setSelected(true);
        JRadioButton butonJos = new JRadioButton("Jos");
        butonJos.setActionCommand("Jos");
        JRadioButton butonStanga = new JRadioButton("Stanga");
        butonStanga.setActionCommand("Stanga");
        JRadioButton butonDreapta = new JRadioButton("Dreapta");
        butonDreapta.setActionCommand("Dreapta");
// Adaugarea butoanelor la grup
        ButtonGroup group = new ButtonGroup();
        group.add(butonSus);
        group.add(butonJos);
        group.add(butonStanga);
        group.add(butonDreapta);
// Adaugarea butoanelor la Layout
        this.setLayout(new GridLayout(0,1));
        add(butonSus);
        add(butonJos);
        add(butonStanga);
        add(butonDreapta);
    }
}

// lista
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