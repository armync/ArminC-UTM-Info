import javax.swing.*;
import java.awt.event.*;

public class MainMenuBar extends JMenuBar {
    JFrame frmParent;
    public MainMenuBar() {
        JMenu fileMenu = new JMenu("File");
        JMenu editMenu = new JMenu("Edit");
        JMenu quitMenu = new JMenu("Quit");

        // Meniul File: Open, Save, Close
        JMenuItem openItem = new JMenuItem("Open");
        JMenuItem saveItem = new JMenuItem("Save");
        JMenuItem closeItem = new JMenuItem("Close");

        // Meniul Edit: Cut, Copy, Paste, Find (Find, Replace)
        JMenuItem cutItem = new JMenuItem("Cut");
        JMenuItem copyItem = new JMenuItem("Copy");
        JMenuItem pasteItem = new JMenuItem("Paste");
        JSeparator separator1 = new JSeparator();

        JMenu findMenu = new JMenu("Find");
        JMenuItem findItem = new JMenuItem("Find");
        JMenuItem replaceItem = new JMenuItem("Replace");

        // Meniul Quit
        JMenuItem exitItem = new JMenuItem("Exit");
        JMenuItem aboutItem = new JMenuItem("About");
        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        fileMenu.add(closeItem);
        editMenu.add(cutItem);
        editMenu.add(copyItem);
        editMenu.add(pasteItem);
        editMenu.add(separator1);
        findMenu.add(findItem);
        findMenu.add(replaceItem);
        editMenu.add(findMenu);
        editMenu.add(new JCheckBox("Alege optiunea"));
        quitMenu.add(exitItem);
        quitMenu.add(aboutItem);
        add(fileMenu);
        add(editMenu);
        add(quitMenu);
    }
}
