package com.example.weatherapp01;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.viewpager2.adapter.FragmentStateAdapter;

import java.util.ArrayList;
import java.util.List;

public class CityPagerAdapter extends FragmentStateAdapter {

    private final List<String> cityNames;

    public CityPagerAdapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
        cityNames = new ArrayList<>();
        cityNames.add("Bucharest");
        cityNames.add("Timisoara");
        cityNames.add("Cluj Napoca");
        cityNames.add("Oradea");
        cityNames.add("Constanta");
        cityNames.add("Iasi");
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        String cityName = cityNames.get(position);
        return CityWeatherFragment.newInstance(cityName);
    }

    @Override
    public int getItemCount() {
        return cityNames.size();
    }

    public void addCity(String cityName) {
        cityNames.add(cityName);
        notifyDataSetChanged();
    }
}
