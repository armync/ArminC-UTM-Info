import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class FormMain extends JFrame{
    public FormMain() {
        this.setJMenuBar(new MainMenuBar());
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500, 500);
        this.setVisible(true);
    }
    public static void main(String[] args) {
        new FormMain();
    } }