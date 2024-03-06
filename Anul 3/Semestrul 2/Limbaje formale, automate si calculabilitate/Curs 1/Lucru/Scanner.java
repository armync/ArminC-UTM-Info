import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Scanner {

    private static final java.util.Scanner scanner = new java.util.Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.print("Introduceti o expresie matematica: ");
            String expresie = scanner.nextLine();

            Pattern pattern = Pattern.compile("^[\\d\\.\\-+*/^%()]+$");
            Matcher matcher = pattern.matcher(expresie);

            if (!matcher.matches()) {
                System.out.println("Expresie invalida");
                continue;
            }

            double rezultat = 0;
            try {
                rezultat = calculeazaExpresie(expresie);
            } catch (Exception e) {
                System.out.println("Eroare la calculul: " + e.getMessage());
                continue;
            }

            System.out.println("Rezultatul expresiei este: " + rezultat);
        }
    }

    private static double calculeazaExpresie(String expresie) {
        Stack<Double> stivaOperanzi = new Stack<>();
        Stack<Character> stivaOperatori = new Stack<>();

        StringBuilder numar = new StringBuilder();
        for (char caracter : expresie.toCharArray()) {
            if (Character.isDigit(caracter) || caracter == '.') {
                numar.append(caracter);
            } else {
                if (!numar.isEmpty()) {
                    stivaOperanzi.push(Double.parseDouble(numar.toString()));
                    numar.setLength(0);
                }
                if (isOperator(caracter)) {
                    while (!stivaOperatori.isEmpty() && getPrecedenta(caracter) <= getPrecedenta(stivaOperatori.peek())) {
                        double operand2 = stivaOperanzi.pop();
                        double operand1 = stivaOperanzi.pop();
                        char operator = stivaOperatori.pop();
                        double rezultat = calculeazaRezultat(operand1, operand2, operator);
                        stivaOperanzi.push(rezultat);
                    }
                    stivaOperatori.push(caracter);
                } else if (caracter == '(') {
                    stivaOperatori.push(caracter);
                } else if (caracter == ')') {
                    while (!stivaOperatori.isEmpty() && stivaOperatori.peek() != '(') {
                        double operand2 = stivaOperanzi.pop();
                        double operand1 = stivaOperanzi.pop();
                        char operator = stivaOperatori.pop();
                        double rezultat = calculeazaRezultat(operand1, operand2, operator);
                        stivaOperanzi.push(rezultat);
                    }
                    if (!stivaOperatori.isEmpty() && stivaOperatori.peek() == '(') {
                        stivaOperatori.pop();
                    } else {
                        throw new IllegalArgumentException("Paranteza in plus");
                    }
                }
            }
        }
        if (!numar.isEmpty()) {
            stivaOperanzi.push(Double.parseDouble(numar.toString()));
        }
        while (!stivaOperatori.isEmpty()) {
            double operand2 = stivaOperanzi.pop();
            double operand1 = stivaOperanzi.pop();
            char operator = stivaOperatori.pop();
            double rezultat = calculeazaRezultat(operand1, operand2, operator);
            stivaOperanzi.push(rezultat);
        }
        if (stivaOperanzi.size() != 1) {
            throw new IllegalArgumentException("Expresie invalida");
        }
        return stivaOperanzi.pop();
    }

    private static boolean isOperator(char caracter) {
        return caracter == '+' || caracter == '-' || caracter == '*' || caracter == '/' || caracter == '^' || caracter == '%';
    }

    private static int getPrecedenta(char operator) {
        switch (operator) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
            case '%':
                return 3;
            default:
                return -1;
        }
    }

    private static double calculeazaRezultat(double operand1, double operand2, char operator) {
        switch (operator) {
            case '+':
                return operand1 + operand2;
            case '-':
                return operand1 - operand2;
            case '*':
                return operand1 * operand2;
            case '/':
                if (operand2 == 0) {
                    throw new IllegalArgumentException("Impartire la zero");
                }
                return operand1 / operand2;
            case '^':
                return Math.pow(operand1, operand2);
            case '%':
                return operand1 % operand2;
            default:
                throw new IllegalArgumentException("Operator invalid: " + operator);
        }
    }
}