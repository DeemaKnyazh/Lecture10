package com.example.test1prep;

public class Main {

    public static void main(String[] args)
    {

        VideoGame vg1 = new VideoGame("sci-fi", "Space Adventures", 35.2, 123);
        VideoGame vg2 = new VideoGame("Horror", "Monster Manor", 12, 400);
        VideoGame vg3 = new VideoGame("racing", "Speedsters", 57.4, 500);
        VideoGame vg4 = new VideoGame("Puzzle", "Impossible Challenge", 67, 634);
        VideoGame vg5 = new VideoGame("Strategy", "War of Kings", 12, 999);

        ShoppingCart cost = new ShoppingCart();

        ShoppingCart.addGame(vg1);
        ShoppingCart.addGame(vg2);
        ShoppingCart.addGame(vg4);
        ShoppingCart.addGame(vg5);

        ShoppingCart.removeGame(vg5);

        System.out.println("Cart" + ShoppingCart.cart);

        System.out.println("Price" + " $" + cost.getTotalPrice());

    }

}
