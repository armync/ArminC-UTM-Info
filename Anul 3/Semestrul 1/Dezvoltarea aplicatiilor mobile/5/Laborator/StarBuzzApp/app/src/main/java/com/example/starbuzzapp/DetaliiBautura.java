package com.example.starbuzzapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class DetaliiBautura extends AppCompatActivity {

    public static final String INFO = "detalii";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detalii_bautura);

        Intent intent = getIntent();
        String detalii = (String) intent.getExtras().get(INFO);

        TextView textView = findViewById(R.id.detaliiTextView);
        textView.setText(detalii);
    }
}