package com.example.test1prep;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCart {
    public static List<VideoGame> cart = new ArrayList<>();

    public static void addGame(VideoGame vg){
        cart.add(vg);

    }

    public static void removeGame(VideoGame vg){
        cart.remove(vg);
    }



    public double getTotalPrice() {
        double totalPrice = 0;
        for (VideoGame vg : cart) {
            totalPrice += vg.getPrice();
        }
        return totalPrice;
    }
}
