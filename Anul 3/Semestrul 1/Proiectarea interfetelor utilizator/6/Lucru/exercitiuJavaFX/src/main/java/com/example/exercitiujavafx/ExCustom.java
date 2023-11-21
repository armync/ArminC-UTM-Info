package com.example.exercitiujavafx;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.stage.Stage;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.CubicCurveTo;
import javafx.scene.shape.Box;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;

public class ExCustom extends Application {
    @Override
    public void start(Stage stage) {
        Path path;
        path = new Path();

        MoveTo moveTo = new MoveTo(432, 12);

        LineTo line1 = new LineTo(321, 161);

        CubicCurveTo cubicTo = new CubicCurveTo();

        cubicTo.setX(100.0f);
        cubicTo.setY(50.0f);

        LineTo line2 = new LineTo(126,232);

        LineTo line3 = new LineTo(400,-500);

        Box box = new Box(50, 50, 50);
        box.setTranslateX(200);
        box.setTranslateY(150);

        PhongMaterial material = new PhongMaterial();
        material.setDiffuseColor(Color.GREEN);
        box.setMaterial(material);

        Button bt1 = new Button();
        bt1.setText("Box");
        bt1.setLayoutX(183);
        bt1.setLayoutY(138);

        //Adding all the elements to the path
        path.getElements().add(moveTo);
        path.getElements().add(cubicTo);

        path.getElements().addAll(line1, line2,line3);

        //Creating a Group object
        Group root = new Group(path, box, bt1);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 300);

        //Setting title to the Stage
        stage.setTitle("Signature with a box");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }
    public static void main(String[] args){
        launch(args);
    }
}
