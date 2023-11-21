package com.example.exercitiujavafx;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.control.Button;
import javafx.scene.Scene;

public class Ex1 extends Application {

    public static void main(String[] args) {

        Application.launch(args);
    }

    public void start(Stage primaryStage) {

        primaryStage.setTitle(" JavaFx Exemplu 1_1");

        Button btn = new Button("JavaFx Button");
        btn.setLayoutX(100);
        btn.setLayoutY(100);

        Button btn2 = new Button("JavaFx Button 2");
        btn2.setLayoutX(200);
        btn2.setLayoutY(100);

        Group group = new Group();
        group.getChildren().add(btn);
        group.getChildren().add(btn2);

        Scene scene = new Scene(group, 700, 200);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
