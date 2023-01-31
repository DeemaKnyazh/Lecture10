module com.example.test1prep {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.test1prep to javafx.fxml;
    exports com.example.test1prep;
}