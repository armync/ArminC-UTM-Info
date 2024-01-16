module com.example.curs7 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;


    opens com.example.curs7 to javafx.fxml;
    exports com.example.curs7;
}