package com.example.weatherapp01;

import com.google.gson.annotations.SerializedName;

public class Daily {

    @SerializedName("time")
    private String time;

    @SerializedName("values")
    private Values values;

    public String getTime() {
        return time;
    }

    public Values getValues() {
        return values;
    }
}
