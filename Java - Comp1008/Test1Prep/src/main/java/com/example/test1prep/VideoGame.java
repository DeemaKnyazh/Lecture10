package com.example.test1prep;

import java.util.Arrays;
import java.util.List;

public class VideoGame {
    private String genre;

    private String name;

    private double price;

    private int sizeInMb;

    public VideoGame(String genre, String name, double price, int sizeInMb) {
        setGenre(genre);
        setName(name);
        setPrice(price);
        setSizeInMb(sizeInMb);
    }

    public String getGenre() {
        return genre;
    }

    public static List<String> getGenres(){
        return Arrays.asList("RPG", "Adventure", "Sci-fi", "Strategy", "Horror", "Survival", "Sandbox", "Puzzle", "Racing");
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getSizeInMb() {
        return sizeInMb;
    }

    public void setGenre(String genre) {
        //First sets all letters to lowercase and then the first to uppercase
        genre = genre.toLowerCase();
        genre = genre.substring(0,1).toUpperCase() + genre.substring(1);

        List<String> validGenres = getGenres();

        if(validGenres.contains(genre))
            this.genre = genre;
        else{
            throw new IllegalArgumentException(genre+ " was not in the list of " + validGenres);
        }

    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        if(price < 1000){
            this.price = price;
        }
        else{
            throw new IllegalArgumentException(price+ " is too expensive");
        }
    }

    public void setSizeInMb(int sizeInMb) {
        if(sizeInMb > 0 && sizeInMb < 1000){
            this.sizeInMb = sizeInMb;
        }
        else if(sizeInMb <= 0){
            throw new IllegalArgumentException(sizeInMb+ " is nonexistant");
        }
        else{
            throw new IllegalArgumentException(sizeInMb+ " too big for our servers");
        }
    }

    public String toString(){
        return "\r\n" + name + "  |  " + "$" + price + "   Genre:" + genre + "   Size:" + sizeInMb + "Mb";
    }
}
