package com.example.weatherapp01;

import com.google.gson.annotations.SerializedName;

public class Values {

    @SerializedName("cloudCoverAvg")
    private double cloudCoverAvg;

    @SerializedName("humidityAvg")
    private double humidityAvg;

    @SerializedName("precipitationProbabilityAvg")
    private double precipitationProbabilityAvg;

    @SerializedName("temperatureAvg")
    private double temperatureAvg;

    @SerializedName("windSpeedAvg")
    private double windSpeedAvg;

    @SerializedName("snowIntensity")
    private double snowIntensity;

    public Values() {
    }

    public double getCloudCoverAvg() {
        return cloudCoverAvg;
    }

    public double getHumidityAvg() {
        return humidityAvg;
    }

    public double getPrecipitationProbabilityAvg() {
        return precipitationProbabilityAvg;
    }

    public double getTemperatureAvg() {
        return temperatureAvg;
    }

    public double getWindSpeedAvg() {
        return windSpeedAvg;
    }

    public double getSnowIntensity() {
        return snowIntensity;
    }

}
