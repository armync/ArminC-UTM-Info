package com.example.demo;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.effect.Glow;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Interfata extends Application {

    private TextField expressionField;
    private Label resultLabel;
    private Timeline errorAnimationTimeline;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Calculator validare regex");

        expressionField = new TextField();
        expressionField.setPromptText("Introduceti o expresie matematica");
        expressionField.setStyle("-fx-font-size: 16px;");

        resultLabel = new Label("Rezultat: ");
        resultLabel.setStyle("-fx-font-weight: bold; -fx-font-size: 16px;");

        Button calculateButton = new Button("Calculeaza");
        calculateButton.setOnAction(e -> handleCalculateButton());
        calculateButton.setStyle("-fx-background-color: #007bff; -fx-text-fill: white; -fx-font-size: 14px;");

        Button resetButton = new Button("Reseteaza");
        resetButton.setOnAction(e -> handleResetButton());
        resetButton.setStyle("-fx-background-color: #dc3545; -fx-text-fill: white; -fx-font-size: 14px;");

        VBox vbox = new VBox(10);
        vbox.setPadding(new Insets(10, 10, 10, 10));
        vbox.getChildren().addAll(expressionField, resultLabel, createButtonBox(calculateButton, resetButton));

        Scene scene = new Scene(vbox, 350, 150);

        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private HBox createButtonBox(Button calculateButton, Button resetButton) {
        HBox buttonBox = new HBox(10);
        buttonBox.getChildren().addAll(calculateButton, resetButton);
        return buttonBox;
    }

    private void handleCalculateButton() {
        String expression = expressionField.getText();

        Pattern pattern = Pattern.compile("^[\\d\\.\\-+*/^%()]+$");
        Matcher matcher = pattern.matcher(expression);

        if (!matcher.matches()) {
            resultLabel.setText("Expresie invalida");
            animateError(resultLabel);
            return;
        }

        double result;
        try {
            result = calculeazaExpresie(expression);
            resultLabel.setText("Rezultat: " + result);
        } catch (Exception e) {
            resultLabel.setText("Eroare: " + e.getMessage());
            animateError(resultLabel);
        }
    }

    private void handleResetButton() {
        expressionField.clear();
        resultLabel.setText("Rezultat: ");
        if (errorAnimationTimeline != null) {
            errorAnimationTimeline.stop();
        }
        resultLabel.setEffect(null);
    }

    private void animateError(Label label) {
        Glow glow = new Glow();
        glow.setLevel(0.5);
        glow.setInput(new Glow());

        Timeline timeline = new Timeline(
                new KeyFrame(Duration.ZERO, e -> label.setEffect(glow)),
                new KeyFrame(Duration.seconds(1), e -> label.setEffect(null))
        );
        timeline.setCycleCount(2);
        timeline.setAutoReverse(true);

        errorAnimationTimeline = timeline;
        timeline.play();
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
        return switch (operator) {
            case '+', '-' -> 1;
            case '*', '/' -> 2;
            case '^', '%' -> 3;
            default -> -1;
        };
    }

    private static double calculeazaRezultat(double operand1, double operand2, char operator) {
        return switch (operator) {
            case '+' -> operand1 + operand2;
            case '-' -> operand1 - operand2;
            case '*' -> operand1 * operand2;
            case '/' -> {
                if (operand2 == 0) {
                    throw new IllegalArgumentException("Impartire la zero");
                }
                yield operand1 / operand2;
            }
            case '^' -> Math.pow(operand1, operand2);
            case '%' -> operand1 % operand2;
            default -> throw new IllegalArgumentException("Operator invalid: " + operator);
        };
    }
}
