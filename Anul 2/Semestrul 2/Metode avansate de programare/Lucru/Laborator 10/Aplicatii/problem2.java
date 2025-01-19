import colectii.Student;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        ArrayList<Student> studenti = new ArrayList<>();

        BufferedReader bf = new BufferedReader(
                new FileReader("student.txt"));

        String linie;
        while ((linie = bf.readLine()) != null) {

            var token = linie.split(",");

            studenti.add(new Student(
               token[0],
               Integer.parseInt(token[1]),
               Integer.parseInt(token[2]),
               Float.parseFloat(token[3])
            ));

        }

        Collections.sort(studenti);

        for (var student : studenti)
            System.out.println(student);

    }
}