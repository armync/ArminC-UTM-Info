package com.example.moonplanet;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.ArrayList;

public class MyAdaptorList extends ArrayAdapter<PlanetModel> {
    ArrayList<PlanetModel> listPlanets;
    Context context;

    public MyAdaptorList(Context context, int resource, ArrayList<PlanetModel> listPlanets){
        super(context, resource, listPlanets);
        this.listPlanets = listPlanets;
        this.context = context;
    }

    // componente de tip View din resursa layout custom

    public static class HolderView
    {
        ImageView imageViewPlanet;
        TextView textViewPlanet;
        TextView textViewMoon;
    }

    // redefinire a metodei getView care returneaza intreg view-ul pentru un item din lista

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent){
        HolderView holderView = new HolderView();

        PlanetModel planet = getItem(position);

        if(convertView == null) {

            // instantiate the HolderView to set the value for each view from item
            holderView = new HolderView();
            convertView = LayoutInflater.from(context).inflate(R.layout.item_list_layout, parent, false);
            holderView.imageViewPlanet = convertView.findViewById(R.id.planetImage);
            holderView.textViewMoon = convertView.findViewById(R.id.moonTextView);
            holderView.textViewPlanet = convertView.findViewById(R.id.planetNameTextView);

            convertView.setTag(holderView);
        } else {
            holderView = (HolderView) convertView.getTag();
        }
        holderView.textViewPlanet.setText(planet.getNamePlanet());
        holderView.textViewMoon.setText(planet.getMoons());
        holderView.imageViewPlanet.setImageResource(planet.getIdImage());

        return convertView;
    }
}