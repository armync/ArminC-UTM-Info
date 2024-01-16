package com.example.weatherapp01;

import com.google.gson.annotations.SerializedName;

public class WeatherResponse {

    @SerializedName("timelines")
    private Timelines timelines;

    public Timelines getTimelines() {
        return timelines;
    }

}
