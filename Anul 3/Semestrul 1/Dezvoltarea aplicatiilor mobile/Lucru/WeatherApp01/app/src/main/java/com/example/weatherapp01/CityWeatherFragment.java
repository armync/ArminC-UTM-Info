package com.example.weatherapp01;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.cardview.widget.CardView;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Locale;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CityWeatherFragment extends Fragment {

    private TextView cityNameTextView;
    private LinearLayout weatherDetailsContainer;

    private String cityName;

    public static CityWeatherFragment newInstance(String cityName) {
        CityWeatherFragment fragment = new CityWeatherFragment();
        Bundle args = new Bundle();
        args.putString("cityName", cityName);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            cityName = getArguments().getString("cityName");
        }
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_city_weather, container, false);

        cityNameTextView = view.findViewById(R.id.cityNameTextView);
        weatherDetailsContainer = view.findViewById(R.id.weatherDetailsContainer);

        cityNameTextView.setText(cityName);

        fetchWeatherData(cityName);

        return view;
    }

    private void fetchWeatherData(String cityName) {
        String apiKey = "CmL1ARjGQXpowzchwtUfs9FBklr1Wxg1";
        // First key: oGNOfks6M5nWf9d5nKehJyN856V98krF
        // Second key: CmL1ARjGQXpowzchwtUfs9FBklr1Wxg1
        // 500 requests per day, 25 requests per hour, 3 requests per second

        if (!isValidApiKey(apiKey)) {
            displayErrorMessage("Invalid API key format. Please provide a valid API key.");
            return;
        }

        WeatherApiService apiService = RetrofitClientInstance.getRetrofitInstance().create(WeatherApiService.class);
        Call<WeatherResponse> call = apiService.getWeatherData(cityName, "1d", "metric", apiKey);

        // Populare lista prin apel
        call.enqueue(new Callback<WeatherResponse>() {
            @Override
            public void onResponse(Call<WeatherResponse> call, Response<WeatherResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    // Extragere si populare lista date meteo zilnice prin raspuns HTTP
                    List<Daily> dailyForecasts = response.body().getTimelines().getDaily();

                    Calendar currentDate = Calendar.getInstance();
                    currentDate.set(Calendar.HOUR_OF_DAY, 0);
                    currentDate.set(Calendar.MINUTE, 0);
                    currentDate.set(Calendar.SECOND, 0);
                    currentDate.set(Calendar.MILLISECOND, 0);

                    // Iterare prognoza pe zile
                    int count = 0;
                    for (Daily daily : dailyForecasts) {
                        try {
                            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
                            Date forecastDate = sdf.parse(daily.getTime().substring(0, 10));

                            if (forecastDate != null && forecastDate.after(currentDate.getTime()) && count < 4) { /* 4 zile */
                                Values values = daily.getValues(); // Accesare detalii meteorolgice
                                displayWeatherDetails(daily.getTime(), values); // Functie carduri dinamice
                                count++;
                            }
                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                    }
                } else {
                    displayErrorMessage("Failed to fetch weather data.");
                }
            }

            @Override
            public void onFailure(Call<WeatherResponse> call, Throwable t) {
                displayErrorMessage("Failed to fetch weather data. Please check your internet connection.");
            }
        });
    }

    private boolean isValidApiKey(String apiKey) {
        return apiKey.matches(".*[a-zA-Z].*") && apiKey.matches(".*\\d.*");
    }

    private void setWeatherBackground(CardView cardView, Values values) {
        double precipitationProbability = values.getPrecipitationProbabilityAvg();
        double temperature = values.getTemperatureAvg();
        double snowIntensity = values.getSnowIntensity();
        double cloudCover = values.getCloudCoverAvg();

        ImageView imageView = new ImageView(getContext());

        imageView.setScaleType(ImageView.ScaleType.CENTER_CROP);

        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT
        );
        imageView.setLayoutParams(layoutParams);

        if (snowIntensity > 0.05) {
            imageView.setImageResource(R.drawable.snowy_background);
        } else if (precipitationProbability > 30) {
            imageView.setImageResource(R.drawable.rainy_background);
        } else if (cloudCover > 60) {
            imageView.setImageResource(R.drawable.cloudy_background);
        } else if (temperature > 20) {
            imageView.setImageResource(R.drawable.sunny_background);
        } else if (temperature <= 20 && temperature >= 0) {
            imageView.setImageResource(R.drawable.normal_background);
        } else if (temperature < 0) {
            imageView.setImageResource(R.drawable.cold_background);
        }

        cardView.addView(imageView);
    }

    // Layout si stilizare carduri dinamice
    private void displayWeatherDetails(String date, Values values) {
        CardView cardView = new CardView(getContext());
        LinearLayout.LayoutParams cardLayoutParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                400
        );
        cardLayoutParams.setMargins(16, 16, 16, 16);
        cardView.setLayoutParams(cardLayoutParams);
        cardView.setCardElevation(8);
        cardView.setRadius(16);

        setWeatherBackground(cardView, values);

        TextView weatherDetailsTextView = new TextView(getContext()); // Creare obiect
        LinearLayout.LayoutParams textLayoutParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        );
        textLayoutParams.setMargins(32, 32, 32, 32);
        weatherDetailsTextView.setLayoutParams(textLayoutParams);
        weatherDetailsTextView.setTypeface(Typeface.createFromAsset(requireActivity().getAssets(), "SF-Pro-Text-Regular.otf"));
        weatherDetailsTextView.setTextColor(ContextCompat.getColor(requireContext(), R.color.textColor));
        weatherDetailsTextView.setShadowLayer(8, 2, 2, Color.DKGRAY);

        // Preluare stringuri
        String weatherDetailsText = getString(R.string.weather_details_format,
                date,
                values.getTemperatureAvg(),
                values.getHumidityAvg(),
                values.getWindSpeedAvg(),
                values.getCloudCoverAvg(),
                values.getPrecipitationProbabilityAvg(),
                values.getSnowIntensity());

        weatherDetailsTextView.setText(weatherDetailsText); // Seteaza cu datele meteo formatate

        cardView.addView(weatherDetailsTextView);
        weatherDetailsContainer.addView(cardView);
    }

    private void displayErrorMessage(String message) {
        TextView errorTextView = new TextView(getContext());
        errorTextView.setLayoutParams(new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));
        errorTextView.setText(message);
        errorTextView.setTextColor(ContextCompat.getColor(requireContext(), R.color.errorColor));
        errorTextView.setGravity(Gravity.CENTER);
        errorTextView.setPadding(16, 16, 16, 16);

        weatherDetailsContainer.addView(errorTextView);
    }
}