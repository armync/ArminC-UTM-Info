package com.example.curs5;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class TrimiteMesajActivity extends AppCompatActivity {

    String mesaj;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_trimite_mesaj);

        Button button = findViewById(R.id.trimiteButton);
        EditText editText = findViewById(R.id.mesajEditText);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // se deschide un nou intent
                Intent intent = new Intent(TrimiteMesajActivity.this, PrimesteMesajActivity.class);

                // preia informatia din EditText (mesaj)
                mesaj = editText.getText().toString();
                // se adauga informatia pentru noul intent
                intent.putExtra(PrimesteMesajActivity.INFO, mesaj);

                startActivity(intent);
            }
        });
    }
}