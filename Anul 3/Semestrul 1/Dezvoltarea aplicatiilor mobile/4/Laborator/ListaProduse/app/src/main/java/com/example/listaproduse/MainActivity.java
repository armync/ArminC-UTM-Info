package com.example.listaproduse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ListView listView = findViewById(R.id.listaProduse);

        ArrayList<String> produse = new ArrayList<>();
        produse.add("Hot Coffee");
        produse.add("Hot Tea");
        produse.add("Iced Teas");
        produse.add("Frappuccino");
        produse.add("Cold Drinks");

        ArrayAdapter<String> adaptorLista =
                new ArrayAdapter<>(this, android.R.layout.simple_expandable_list_item_1, produse);

        listView.setAdapter(adaptorLista);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Toast.makeText(MainActivity.this, "Ati selectat " + produse.get(i), Toast.LENGTH_LONG).show();
            }
        });
    }
}