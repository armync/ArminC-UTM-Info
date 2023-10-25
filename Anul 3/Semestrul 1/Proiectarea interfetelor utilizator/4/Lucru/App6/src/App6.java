import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class App6 extends JFrame {
    JButton button = new JButton("Apasa", new ImageIcon("src/poze/1.png"));
    JTextField text = new JTextField(30);
    JButton button1 = new JButton("Apasa", new ImageIcon("src/poze/2.png"));
    JButton button2 = new JButton("Reset");
    JTextField text1 = new JTextField(30);
    JButton b3 = new JButton("Apasa3");
    JTextField text2 = new JTextField(30);

    public App6() {
        this.setTitle("test");
        Container cp = getContentPane();
        cp.setLayout(null);

        cp.add(button);
        cp.add(button1);
        cp.add(button2);
        cp.add(text);
        cp.add(text1);
        cp.add(b3);
        cp.add(text2);

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                text.setText("Ai apasat pe butonul 1");
                text1.setText("");
            }
        });

        button.setBounds(30, 30, 100, 80);
        text.setBounds(140, 60, 200, 20);

        button1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                text1.setText("Ai apasat pe butonul 2");
                text.setText("");
            }
        });

        button1.setBounds(30, 130, 90, 70);
        text1.setBounds(142, 150, 200, 20);

        button2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                text1.setText("");
                text.setText("");
                text2.setText("");
            }
        });

        button2.setBounds(130, 310, 90, 60);

        b3.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                text2.setText("Ai apasat pe butonul 3");
                text1.setText("");
                text.setText("");
            }
        });

        b3.setBounds(30, 220, 90, 70);
        text2.setBounds(142, 235, 200, 20);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 600);
        this.setResizable(false);
        this.setLocation(393, 345);
    }

    public static void main(String[] args) throws Exception {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
        SwingUtilities.invokeLater(() -> {
            new App6().setVisible(true);
        });
    }
}
