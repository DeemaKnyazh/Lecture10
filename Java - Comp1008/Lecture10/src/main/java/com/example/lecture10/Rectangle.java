package com.example.lecture10;

public class Rectangle {

    private double height, width;

    public Rectangle(double height, double width) {
        this.height = height;
        this.width = width;
    }

    public double getHeight() {
        return height;
    }

    public double getWidth() {
        return width;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public boolean isSquare(){
        return true;
    }
    public double getArea(){
        //30*20 should return 600
        return height*width;
    }
    public double getPerimeter(){
        return 0.0;
    }

}
