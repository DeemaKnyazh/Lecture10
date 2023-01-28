package com.example.w23comp1008lhw2;

import java.util.ArrayList;
import java.util.List;

public class DeckOfCards {

    //THis is the instance variable that holds all of the card objects
    //You can think of it sort of like the box that holds all the card's

    private ArrayList<Card> deck;

    /**
     * This is the constructor. It will allocate system memory for the
     * ArrayList to hold Card objects. It will also create 52 Card objects
     * and put them in the ArrayList
     */
    public DeckOfCards(){
        deck = new ArrayList<>();
        List<String> suits = Card.getValidSuits();
        List<String> faceName = Card.getFaceNames();
    }
}
