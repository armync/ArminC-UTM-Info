package com.example.weatherapp01;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface WeatherApiService {

    // Manipulare URL
    @GET("forecast")
    Call<WeatherResponse> getWeatherData(
            @Query("location") String city,
            @Query("timesteps") String timesteps,
            @Query("units") String units,
            @Query("apikey") String apiKey
    );
}


