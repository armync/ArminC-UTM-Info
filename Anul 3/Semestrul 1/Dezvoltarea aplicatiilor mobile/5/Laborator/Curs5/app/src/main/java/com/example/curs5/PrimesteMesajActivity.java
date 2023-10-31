package com.example.curs5;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class PrimesteMesajActivity extends AppCompatActivity {

    public static final String INFO = "mesaj";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_primeste_mesaj);

        // preia intent
        Intent intent = getIntent();

        // se preia info din intent
        String mesaj = intent.getStringExtra("mesaj");

        // se seteaza continutul TextView
        TextView textView = findViewById(R.id.mesajEditText);
        textView.setText(mesaj);
    }
}