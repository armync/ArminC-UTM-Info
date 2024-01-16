package com.example.curs7;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.sql.*;

public class LoginMenu extends Application {

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("JavaFX Welcome");

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        Scene scene = new Scene(grid, 300, 275);
        primaryStage.setScene(scene);

        Text scenetitle = new Text("Welcome");

        scenetitle.setFont(Font.font("Tahoma", FontWeight.NORMAL, 20));
        grid.add(scenetitle, 0, 0, 2, 1);

        Label userName = new Label("User Name:");
        grid.add(userName, 0, 1);

        TextField userTextField = new TextField();
        grid.add(userTextField, 1, 1);

        Label pw = new Label("Password:");
        grid.add(pw, 0, 2);

        PasswordField pwBox = new PasswordField();
        grid.add(pwBox, 1, 2);

        Button btn = new Button("Sign in");
        HBox hbBtn = new HBox(10);
        hbBtn.setAlignment(Pos.BOTTOM_RIGHT);
        hbBtn.getChildren().add(btn);
        grid.add(hbBtn, 1, 4);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        btn.setOnAction(e -> {
            // preluam casetele text
            String user = userTextField.getText();
            String password = pwBox.getText();

            try {
                Connection con;

                final String tipDB = "postgres"; // "postgres" / "sqlite3"
                final String postgresURL = "jdbc:postgresql://localhost:5432/postgres";
                final String postgresUser = "postgres";
                final String postgresPass = "admin";
                final String sqliteURL = "jdbc:sqlite:C:/Users/ArminC/Desktop/sqlite/conexiune_javafx.db";

                if (tipDB.equals("postgres")) {
                    con = DriverManager.getConnection(postgresURL, postgresUser, postgresPass);
                } else if (tipDB.equals("sqlite3")) {
                    con = DriverManager.getConnection(sqliteURL);
                } else {
                    throw new UnsupportedOperationException("DB ERROR");
                }

                Statement st = con.createStatement();

                ResultSet check = st.executeQuery("SELECT * FROM users WHERE username = '" + user + "' AND password = '" + password + "'");

                if (check.next()) {
                    CalculMinim calculMinim = new CalculMinim();
                    Stage calculMinimStage = new Stage();
                    calculMinim.start(calculMinimStage);

                    userTextField.setText("");
                    pwBox.setText("");
                    primaryStage.close();
                } else {
                    actiontarget.setFill(Color.FIREBRICK);
                    actiontarget.setText("Cont invalid!");
                }

                check.close();
                st.close();
                con.close();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        });

        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
