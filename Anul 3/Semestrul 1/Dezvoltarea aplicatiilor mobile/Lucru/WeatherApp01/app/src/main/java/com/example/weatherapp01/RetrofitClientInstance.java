package com.example.weatherapp01;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClientInstance {

    private static Retrofit retrofit;
    private static final String BASE_URL = "https://api.tomorrow.io/v4/weather/"; /* Link-ul de baza al API-ului */

    /* .url("https://api.tomorrow.io/v4/weather/forecast?location=numeOras&timesteps=ora/Zi&apikey=cheie") */

    public static Retrofit getRetrofitInstance() {
        if (retrofit == null) {
            retrofit = new retrofit2.Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create()) // JSON
                    .build();
        }
        return retrofit;
    }
}

