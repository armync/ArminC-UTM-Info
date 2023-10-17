package com.example.animatiiapp;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.drawable.RippleDrawable;
import android.view.View;
import android.os.Bundle;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    boolean bartIsShowing = false;

    public void animation(View view){

        ImageView imageView = findViewById(R.id.bartImageView);

        if(bartIsShowing==false){
            imageView.setImageResource(R.drawable.hommer);
            bartIsShowing = true;
        } else {
            imageView.setImageResource(R.drawable.bart);
            bartIsShowing = false;
        }
        // ImageView imageView = findViewById(R.id.ImageView);
        // imageView.setImageResource(R.drawable.hommer);

        // imageView.animate().alpha(0).setDuration(2000);
        // imageView.animate().translationXBy(-1500).setDuration(2000);
        // imageView.animate().scaleX(0.5).scaleY(0.5).setDuration(2000);
        imageView.animate().rotation(3600).setDuration(2000);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}