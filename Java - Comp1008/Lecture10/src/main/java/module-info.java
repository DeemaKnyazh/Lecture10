module com.example.lecture10 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lecture10 to javafx.fxml;
    exports com.example.lecture10;
}