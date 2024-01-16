package com.example.sportscardapp;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class CustomAdaptor extends RecyclerView.Adapter<CustomAdaptor.SportHolder>{
    List<Sport> sportList;

    public CustomAdaptor(List<Sport> sportList) {
        this.sportList = sportList;
    }

    @NonNull
    @Override
    public SportHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.card_item_layout, parent, false);
        return new SportHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull SportHolder holder, int position) {
        Sport crtSport = sportList.get(position);
        holder.titleTextView.setText(crtSport.getSportName());
        holder.imageView.setImageResource(crtSport.getSportImage());
    }

    @Override
    public int getItemCount() {
        return sportList.size();
    }

    public static class SportHolder extends RecyclerView.ViewHolder {
        TextView titleTextView;
        ImageView imageView;

        public SportHolder(@NonNull View itemView) {
            super(itemView);
            titleTextView = itemView.findViewById(R.id.textView);
            imageView = itemView.findViewById(R.id.imageviewCard);
        }
    }
}