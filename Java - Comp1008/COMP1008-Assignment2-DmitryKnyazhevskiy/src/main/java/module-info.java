module com.example.comp1008assignment2dmitryknyazhevskiy {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.comp1008assignment2dmitryknyazhevskiy to javafx.fxml;
    exports com.example.comp1008assignment2dmitryknyazhevskiy;
}