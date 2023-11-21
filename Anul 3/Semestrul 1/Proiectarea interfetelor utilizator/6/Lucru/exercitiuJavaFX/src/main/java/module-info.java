module com.example.exercitiujavafx {
    requires javafx.controls;
    requires javafx.fxml;

    requires com.dlsc.formsfx;

    opens com.example.exercitiujavafx to javafx.fxml;
    exports com.example.exercitiujavafx;
}