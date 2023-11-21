package com.example.moonplanet;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //ListView de viewList legatura
        ListView listView = findViewById(R.id.planetListView);

        // Sursa de date
        ArrayList<PlanetModel> list = new ArrayList<>();
        list.add(new PlanetModel("Earth", "1", R.drawable.earth));
        list.add(new PlanetModel("Mars", "2", R.drawable.mars));
        list.add(new PlanetModel("Jupiter", "3", R.drawable.jupiter));
        list.add(new PlanetModel("Neptune", "4", R.drawable.neptune));
        list.add(new PlanetModel("Mercury", "5", R.drawable.mercury));
        list.add(new PlanetModel("Pluto", "6", R.drawable.pluto));

        // Definim un adaptor pentru lista cu planete
        MyAdaptorList adaptor = new MyAdaptorList(this, R.layout.item_list_layout, list);

        listView.setAdapter(adaptor);
    }
}