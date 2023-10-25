import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args){
        JFrame frame = new JFrame("JTable");
        String[] columns = {"Nr crt", "Nume student", "N1", "N2", "N3", "N4", "N5", "N6"};

        Object[][] data = {
                {"1", "Popescu Ion", 10.00, 10.00, 10.00, 8.50, 7.50, 5.70},
                {"2", "Ana Maria", 8, 7, 9, 7, 5, 6},
                {"3", "Chanchian Armin", 9, 7, 9, 7, 6, 7}
        };

        JTable table = new JTable(data,columns);
        JScrollPane scrollPane = new JScrollPane(table);
        table.setFillsViewportHeight(true);

        JLabel lblHeading = new JLabel("Eticheta");
        lblHeading.setFont(new Font("Arial",Font.TRUETYPE_FONT,24));

        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(lblHeading,BorderLayout.PAGE_START);
        frame.getContentPane().add(scrollPane,BorderLayout.CENTER);

        frame.setSize(550,200);
        frame.setVisible(true);

    }
}