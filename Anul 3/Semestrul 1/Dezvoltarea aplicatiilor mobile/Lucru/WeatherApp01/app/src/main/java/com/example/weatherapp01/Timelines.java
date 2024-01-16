package com.example.weatherapp01;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Timelines {

    @SerializedName("daily")
    private List<Daily> daily;

    public List<Daily> getDaily() {
        return daily;
    }

}
