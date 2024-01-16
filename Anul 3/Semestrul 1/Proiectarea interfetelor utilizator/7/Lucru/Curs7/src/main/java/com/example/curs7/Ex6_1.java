package com.example.curs7;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class Ex6_1 extends Application {

    // launch the application
    public void start(Stage stage)
    {

        try {

            // set title for the stage
            stage.setTitle("VBox");

            // create a VBox
            VBox vbox = new VBox(15);
            // create a label
            Label label = new Label("Label");
            // add label to vbox
            vbox.getChildren().add(label);
            // add buttons to VBox
            for (int i = 0; i < 5; i++)
            {
                vbox.getChildren().add(new Button("Button " + (int)(i + 1)));
            }
            // create a scene
            Scene scene = new Scene(vbox, 300, 300);
            // set the scene
            stage.setScene(scene);
            stage.show();
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    // Main Method
    public static void main(String[] args)
    {
        // launch the application
        launch(args);
    }
}
