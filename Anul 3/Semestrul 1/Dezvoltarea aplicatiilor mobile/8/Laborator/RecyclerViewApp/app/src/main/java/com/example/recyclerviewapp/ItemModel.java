package com.example.recyclerviewapp;

public class ItemModel {
    private int idImage;
    private String title;
    private String des;

    public ItemModel(int idImage, String title, String des) {
        this.idImage = idImage;
        this.title = title;
        this.des = des;
    }

    public int getIdImage() {
        return idImage;
    }

    public void setIdImage(int idImage) {
        this.idImage = idImage;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDes() {
        return des;
    }

    public void setDes(String des) {
        this.des = des;
    }
}
