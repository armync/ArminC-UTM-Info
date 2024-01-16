package com.example.weatherapp01;

import android.animation.ObjectAnimator;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager2.widget.ViewPager2;

import com.google.android.material.button.MaterialButton;

public class MainActivity extends AppCompatActivity {

    private ViewPager2 viewPager;
    private CityPagerAdapter cityPagerAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        viewPager = findViewById(R.id.viewPager);
        cityPagerAdapter = new CityPagerAdapter(this);
        viewPager.setAdapter(cityPagerAdapter);

        ImageView leftArrow = findViewById(R.id.arrow1);
        ImageView rightArrow = findViewById(R.id.arrow2);

        leftArrow.setOnClickListener(view -> handleLeftArrowClick());
        rightArrow.setOnClickListener(view -> handleRightArrowClick());

        MaterialButton addCityButton = findViewById(R.id.addCityButton);
        addCityButton.setOnClickListener(view -> addCity());
    }

    private void handleLeftArrowClick() {
        int currentItem = viewPager.getCurrentItem();
        if (currentItem > 0) {
            viewPager.setCurrentItem(currentItem - 1);
            animateArrowClick(findViewById(R.id.arrow1));
        }
    }

    private void handleRightArrowClick() {
        int currentItem = viewPager.getCurrentItem();
        if (currentItem < cityPagerAdapter.getItemCount() - 1) {
            viewPager.setCurrentItem(currentItem + 1);
            animateArrowClick(findViewById(R.id.arrow2));
        }
    }

    private void animateArrowClick(View arrowView) {
        ObjectAnimator animator = ObjectAnimator.ofFloat(arrowView, "translationY", 0f, -20f, 0f);
        animator.setDuration(300);
        animator.start();
    }

    public void addCity() {
    EditText cityNameEditText = findViewById(R.id.cityNameEditText);
        String newCityName = cityNameEditText.getText().toString().trim();

        if (!newCityName.isEmpty()) {
            cityPagerAdapter.addCity(newCityName);
            viewPager.setCurrentItem(cityPagerAdapter.getItemCount() - 1);

            Log.d("CityAdded", "Added city: " + newCityName);
        } else {
            Toast.makeText(this, "Please enter a city name", Toast.LENGTH_SHORT).show();
        }
        cityNameEditText.setText("");
    }

}