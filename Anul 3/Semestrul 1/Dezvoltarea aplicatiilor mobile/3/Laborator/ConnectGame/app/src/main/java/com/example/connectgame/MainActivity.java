package com.example.connectgame;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    // 0 = yellow
    // 1 = red
    // 2 = empty
    int activePlayer = 0;

    int[] gameState = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2};

    int[][] winPositions = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
    public void dropIn(View view) {
        ImageView imageView = (ImageView) view;
        int tagIndex = Integer.parseInt(imageView.getTag().toString());

        if (gameState[tagIndex] == 2) {

            gameState[tagIndex] = activePlayer;

            imageView.setTranslationY(-1500);

            if (activePlayer == 0) {
                ((ImageView) view).setImageResource(R.drawable.yellow);
                activePlayer = 1;
            } else {
                ((ImageView) view).setImageResource(R.drawable.red);
                activePlayer = 0;
            }
            imageView.animate().translationYBy(1500).setDuration(1000);

            for(int[] win:winPositions){
                if(gameState[win[0]]==gameState[win[1]] && gameState[win[1]]==gameState[win[2]] && gameState[win[0]]!=2){
                    Toast.makeText(this,"Someone has won!", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}