import colectii.Student;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        TreeMap<String,String> agenda = new TreeMap<>(
                new Comparator<String>() {
                    @Override
                    public int compare(String o1, String o2) {
                        return o1.compareTo(o2);
                    }
                });

        BufferedReader bf = new BufferedReader(
                new FileReader("agendaTelefonica.txt"));

        String linie;
        while ((linie = bf.readLine()) != null) {

            var token = linie.split(",");

            agenda.put(token[0],token[1]);

        }

        for (var contact : agenda.entrySet())
            System.out.println(contact);

    }
}