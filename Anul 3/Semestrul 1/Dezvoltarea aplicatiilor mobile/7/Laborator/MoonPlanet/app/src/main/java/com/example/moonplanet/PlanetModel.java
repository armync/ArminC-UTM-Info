package com.example.moonplanet;

public class PlanetModel {
    private int idImage;
    private String namePlanet;
    private String moon;

    public PlanetModel(String namePlanet, String moon, int idImage) {
        this.namePlanet = namePlanet;
        this.moon = moon;
        this.idImage = idImage;
    }

    public String getNamePlanet() {
        return namePlanet;
    }

    public void setNamePlanet(String namePlanet) {
        this.namePlanet = namePlanet;
    }

    public String getMoons() {
        return moon;
    }

    public void setMoons(String moons) {
        this.moon = moons;
    }

    public int getIdImage() {
        return idImage;
    }

    public void setIdImage(int idImage) {
        this.idImage = idImage;
    }
}
