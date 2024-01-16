package com.example.curs7;

import javafx.animation.PathTransition;
import javafx.application.Application;
import javafx.event.EventHandler;

import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

import javafx.scene.shape.Circle;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Ex5_2 extends Application {
    @Override
    public void start(Stage stage) {
        //Drawing a Circle
        Circle circle = new Circle();

        //Setting the position of the circle
        circle.setCenterX(300.0f);
        circle.setCenterY(135.0f);

        //Setting the radius of the circle
        circle.setRadius(25.0f);

        //Setting the color of the circle
        circle.setFill(Color.BROWN);

        //Setting the stroke width of the circle
        circle.setStrokeWidth(20);

        //Creating a Path
        Path path = new Path();

        //Moving to the staring point
        MoveTo moveTo = new MoveTo(208, 71);

        //Creating 1st line
        LineTo line1 = new LineTo(421, 161);

        //Creating 2nd line
        LineTo line2 = new LineTo(226,232);

        //Creating 3rd line
        LineTo line3 = new LineTo(332,52);


        //Adding all the elements to the path
        path.getElements().add(moveTo);
        path.getElements().addAll(line1, line2, line3);

        //Creating the path transition
        PathTransition pathTransition = new PathTransition();

        //Setting the duration of the transition
        pathTransition.setDuration(Duration.millis(1000));

        //Setting the node for the transition
        pathTransition.setNode(circle);

        //Setting the path for the transition
        pathTransition.setPath(path);

        //Setting the orientation of the path
        //pathTransition.setOrientation(  PathTransition.OrientationType.ORTHOGONAL_TO_TAN GENT);

        //Setting the cycle count for the transition
        pathTransition.setCycleCount(50);

        //Setting auto reverse value to true
        pathTransition.setAutoReverse(false);

        //Creating play button
        Button playButton = new Button("Play");
        playButton.setLayoutX(300);
        playButton.setLayoutY(250);

        circle.setOnMouseClicked (new EventHandler<javafx.scene.input.MouseEvent>() {
            @Override
            public void handle(javafx.scene.input.MouseEvent e) {
                System.out.println("Hello World");
                circle.setFill(Color.DARKSLATEBLUE);
            }
        });
        playButton.setOnMouseClicked((new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                System.out.println("Hello World");
                pathTransition.play();
            }
        }));

        //Creating stop button
        Button stopButton = new Button("stop");
        stopButton.setLayoutX(250);
        stopButton.setLayoutY(250);

        stopButton.setOnMouseClicked((new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                System.out.println("Hello World");
                pathTransition.stop();
            }
        }));
        //Creating a Group object
        Group root = new Group(circle, playButton, stopButton);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 300);
        scene.setFill(Color.LAVENDER);

        //Setting title to the Stage
        stage.setTitle("Ex 5b");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }
    public static void main(String[] args){
        launch(args);
    }
}
