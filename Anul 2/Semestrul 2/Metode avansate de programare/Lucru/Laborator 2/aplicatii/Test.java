package aplicatii;

import java.util.Arrays;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("n = ");
        int n = input.nextInt();

        int a[][] = new int[n][];

        for(int i = 0; i < n; i++)
        {
            a[i] = new int[i+1];
            for(int j = 0; j <= i; j++)
                a[i][j] = j+1;
        }

//        System.out.println(Arrays.deepToString(a));
        for(var linie : a) {
            for (var elem : linie)
                System.out.print(elem + " ");
            System.out.println();
        }

    }
}
