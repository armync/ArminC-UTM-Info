module com.example.curs7 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.curs7 to javafx.fxml;
    exports com.example.curs7;
}