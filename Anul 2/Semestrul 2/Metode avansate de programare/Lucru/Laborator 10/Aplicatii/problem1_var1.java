import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
        TreeSet<Integer> grila = new TreeSet<Integer>(
                new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        return o2 - o1;
                    }
                }
        );

        BufferedReader bf = new BufferedReader(
                new FileReader("date.in"));

        String linie;
        while ((linie = bf.readLine()) != null) {

            var token = linie.split(",");

            grila.add(Integer.parseInt(token[token.length-1]));

        }

        for (var elem : grila)
            System.out.println(elem);

    }
}