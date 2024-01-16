package com.example.curs7;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class CalculMinim extends Application {

    Stage window;
    Button Calculeaza;
    Button Next;
    Label rez = new Label();
    TextField a = new TextField();
    TextField b = new TextField();
    TextField c = new TextField();
    TextField d = new TextField();

    Label N1 = new Label("Nr 1:");
    Label N2 = new Label("Nr 2:");
    Label N3 = new Label("Nr 3:");
    Label N4 = new Label("N. 4:");
    int min = 0;

    @Override
    public void start(Stage primaryStage) {
        window = primaryStage;
        window.setTitle("MINIM");
        Calculeaza = new Button("Calculeaza");
        Next = new Button("Next");

        GridPane pane = new GridPane();
        pane.setAlignment(Pos.BASELINE_LEFT);
        pane.setHgap(10);
        pane.setVgap(10);
        pane.setPadding(new Insets(25, 25, 25, 25));

        a.setPrefColumnCount(14);
        b.setPrefColumnCount(14);
        c.setPrefColumnCount(14);
        d.setPrefColumnCount(14);

        pane.add(N1, 0, 1);
        pane.add(a, 1, 1);
        pane.add(N2, 0, 2);
        pane.add(b, 1, 2);
        pane.add(N3, 0, 3);
        pane.add(c, 1, 3);
        pane.add(N4, 0, 4);
        pane.add(d, 1, 4);

        pane.add(Calculeaza, 1, 8);
        pane.add(rez, 1, 9);

        pane.add(Next, 2, 8);

        BorderPane borderPane = new BorderPane();
        borderPane.setCenter(pane);

        Calculeaza.setOnAction(e -> {
            min = Integer.parseInt(a.getText());
            int B1 = Integer.parseInt(b.getText());
            int C1 = Integer.parseInt(c.getText());
            int D1 = Integer.parseInt(d.getText());
            if (B1 <= min)
                min = B1;
            if (C1 <= min)
                min = C1;
            if (D1 <= min)
                min = D1;
            rez.setTextFill(Color.rgb(32, 36, 200));

            rez.setText("Elementul minim este " + min);
        });
        Scene scene = new Scene(borderPane, 400, 400);

        Next.setOnAction(e -> {
            ColorfulCircles colorfulcircles = new ColorfulCircles();
            colorfulcircles.start(new Stage());
            primaryStage.close();
        });
        window.setScene(scene);
        window.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}