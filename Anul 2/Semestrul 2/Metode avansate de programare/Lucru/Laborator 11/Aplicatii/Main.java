import java.io.*;
import java.util.*;
import java.util.function.Consumer;
import java.util.function.Predicate;

class Main {

    public static ArrayList<Concert> filtruConcerte(ArrayList<Concert> concerte, Predicate<Concert> p) {
        var listaNoua = new ArrayList<Concert>();

        for (var concert : concerte) {
            if (p.test(concert)) {
                listaNoua.add(concert);
            }
        }

        return listaNoua;

    }

    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Concert> concerte = new ArrayList<>();

        Scanner sc = new Scanner(new File ("concerte.txt"));

        String concert = null;

        while (sc.hasNextLine()) {
            concert = sc.nextLine();
            var tokens = concert.split(" ");

            Concert concert_tmp = new Concert(tokens[0],
                    tokens[1],
                    Double.parseDouble(tokens[2]),
                    Integer.parseInt(tokens[3]));

            concerte.add(concert_tmp);

        }

        //System.out.println(concerte);

        Predicate<Concert> bucurestiFiltru = x -> x.getLocalitate().equals("Bucuresti");
        Predicate<Concert> clujFiltru = x -> x.getLocalitate().equals("Cluj");
        Consumer<ArrayList<Concert>> show = xs -> System.out.println(xs);
        Consumer<ArrayList<Concert>> sortPretBilete = xs -> Collections.sort(xs,
                (ob1,ob2)-> Double.compare(ob2.getPretBilet(),ob1.getPretBilet()));

        var listaBucuresti = filtruConcerte(concerte, bucurestiFiltru);
        var listaCluj = filtruConcerte(concerte, clujFiltru);

        //pct A

        //sortPretBilete.andThen(show).accept(listaBucuresti);

        //pct B


        TreeSet<String> localitati = new TreeSet<>((x,y)->y.compareTo(x));

        for (var x : concerte) {
            localitati.add(x.getLocalitate());
        }

        //System.out.println(localitati);

        //pct C
        Predicate<Concert> gr500 = x -> x.getNumarLocuri() > 500;

        //show.accept(filtruConcerte(concerte,gr500));

        //pct D

        var map = new HashMap<String, List<Concert>>();

        for (var x : concerte) {
            if (map.get(x.getLocalitate()) == null) {
                map.put(x.getLocalitate(), new ArrayList<>());
            }
            map.get(x.getLocalitate()).add(x);
        }

        /*
        for (var x : map.entrySet()) {
            System.out.println(x.getKey() + ":" + x.getValue());
        }
        */

        concerte.stream().filter(bucurestiFiltru).forEach(System.out::println);

        //System.out.println(listaBucuresti);

    }
}