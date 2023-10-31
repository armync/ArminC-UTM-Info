package com.example.starbuzzapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;

public class BauturiActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bauturi);

        ListView listaBauturi = findViewById(R.id.bauturiListView);

        ArrayList<String> bauturi = new ArrayList<>();
        bauturi.add("Capuccino");
        bauturi.add("Cafea cu lapte");
        bauturi.add("Cafea filtru");

        ArrayAdapter<String> adapter =
                new ArrayAdapter<>(this, android.R.layout.simple_expandable_list_item_1, bauturi);

        listaBauturi.setAdapter(adapter);

        listaBauturi.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String detalii = "";

                switch (position) {
                    case 0:
                        detalii = "Cafea cu spuma de lapte";
                        break;
                    case 1:
                        detalii = "Cafea cu lapte cald.";
                        break;
                    case 2:
                        detalii = "Bautura din cafea filtrata cu apa fierbinte.";
                        break;
                    default:
                        break;
                }

                Intent intent = new Intent(BauturiActivity.this, DetaliiBautura.class);
                intent.putExtra(DetaliiBautura.INFO, detalii);
                startActivity(intent);
            }
        });
    }
}
