import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {

        TreeMap<Integer, ArrayList<String>> grila = new TreeMap<>(
                new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        return o2-o1;
                    }
                }
        );


        BufferedReader bf = new BufferedReader(
                new FileReader("date.in"));

        String linie;
        while ((linie = bf.readLine()) != null) {

            var token = linie.split(",");

            var salariu = Integer.parseInt(token[token.length-1]);
            String nume = token[1] +  " " + token[0];

            ArrayList<String> listaNume = null;

            if (!grila.containsKey(salariu)) {
                listaNume = new ArrayList<String>();
            } else {
                listaNume = grila.get(salariu);
            }

            listaNume.add(nume);
            grila.put(salariu, listaNume);

        }

        for (var elem : grila.entrySet())
            System.out.println(elem);

    }
}