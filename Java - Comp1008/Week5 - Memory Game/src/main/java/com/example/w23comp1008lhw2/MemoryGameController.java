package com.example.w23comp1008lhw2;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.FlowPane;

import java.net.URL;
import java.util.ResourceBundle;

public class MemoryGameController implements Initializable {

    @FXML
    private Label correct;

    @FXML
    private FlowPane cardFlowPane;

    @FXML
    private Label guesses;

    @FXML
    void playAgain(ActionEvent event) {

    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        flipAllCards();
    }

    /**
    * This will check if a MemoryCard is matched or not. If it is not matched, it will display
    * the back of the card
     */
    private void flipAllCards()
    {
        Image backOfCard = new Image(MemoryCard.class.getResourceAsStream("images/back_of_card.png"));

        //loop over all the imageview objects in the flowpane
        //and set their image to be the back of a card
        for (int i=0; i<cardFlowPane.getChildren().size();i++)
        {
            //casting the generic Node object to an ImageView object
            ImageView imageView = (ImageView) cardFlowPane.getChildren().get(i);
            imageView.setImage(backOfCard);
        }
    }
}
