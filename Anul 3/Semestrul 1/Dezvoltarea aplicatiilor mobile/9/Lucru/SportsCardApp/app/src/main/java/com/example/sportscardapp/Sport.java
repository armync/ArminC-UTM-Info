package com.example.sportscardapp;

public class Sport {
    private String sportName;
    private int sportImage;

    public Sport(String sportName, int sportImage) {
        this.sportName = sportName;
        this.sportImage = sportImage;
    }

    public String getSportName() {
        return sportName;
    }

    public int getSportImage() {
        return sportImage;
    }
}