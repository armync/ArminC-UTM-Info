#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <SFML/Graphics.h>

#define EPS_X 30
#define EPS_Y 60

const int WIDTH = 1280;
const int HEIGHT = 720;
const int P1_X = 30;
const int P2_X = WIDTH - 2*P1_X;
const int P_Y = 100;
const int PSIZE_X = 30;
const int PSIZE_Y = 100;
const int BALL_RADIUS = 25;

unsigned int player1_score;
unsigned int player2_score;
bool game_end, help, pause;

sfVector2f pos_player1, player1_pos_start = {P1_X, (HEIGHT - PSIZE_Y) / 2};
sfVector2f pos_player2, player2_pos_start = {P2_X, (HEIGHT - PSIZE_Y) / 2};
sfVector2f pos_ball, dir_ball;
sfVector2f pos_ball_start = {WIDTH / 2 - BALL_RADIUS, HEIGHT / 2 - BALL_RADIUS};
sfVector2f dir_ball_start = {-10, 0};

void init() {
    pos_player1 = player1_pos_start;
    pos_player2 = player2_pos_start;
    pos_ball = pos_ball_start;
    dir_ball = dir_ball_start;
    game_end = help = pause = false;
    player1_score = player2_score = 0;
}

int main()
{
    // https://www.sfml-dev.org/tutorials/2.5/
    // https://www.sfml-dev.org/documentation/2.5.1/
    // https://epitech-2022-technical-documentation.readthedocs.io/en/latest/csfml.html
    sfVideoMode mode = {WIDTH, HEIGHT, 24};  // 24 bit depth, "true" color, 16 mil colors
    sfRenderWindow *window = sfRenderWindow_create(mode, "Pong", sfResize | sfClose, NULL);
    sfRenderWindow_setFramerateLimit(window, 60);  // 60 frames per second

    sfRectangleShape *player1 = sfRectangleShape_create();
    sfRectangleShape *player2 = sfRectangleShape_create();

    sfVector2f size_player = {PSIZE_X, PSIZE_Y};
    sfRectangleShape_setSize(player1, size_player);
    sfRectangleShape_setSize(player2, size_player);

    int player_speed = 30;

    sfCircleShape *ball = sfCircleShape_create();
    sfCircleShape_setRadius(ball, BALL_RADIUS);
    sfCircleShape_setFillColor(ball, sfYellow);

    ////////////////////////////////////////////////////////////////
    /// initializations for middle bar, walls, score and fonts
    /// fileu
    const int dist_points = 30;
    int n_points = (HEIGHT / dist_points) - 1; /// -1 because of the walls
    sfRectangleShape **middle = malloc(n_points * sizeof(sfRectangleShape*));
    for(int i = 0; i < n_points; i++) {
        middle[i] = sfRectangleShape_create();
        // -5 correction to be exactly in the middle
        // 25 because the wall is 10 px and we need a bit of extra space
        sfVector2f pos_mid = {WIDTH / 2 - 5, dist_points * i + 25};
        sfVector2f size_mid = {10, 10};
        sfRectangleShape_setPosition(middle[i], pos_mid);
        sfRectangleShape_setSize(middle[i], size_mid);
    }

    sfRectangleShape *walls = sfRectangleShape_create();
    const int wall_thickness = 10;
    sfVector2f pos_wall = {wall_thickness, wall_thickness};
    sfVector2f size_wall = {WIDTH - 2*wall_thickness, HEIGHT - 2*wall_thickness};
    sfRectangleShape_setFillColor(walls, sfTransparent);
    sfRectangleShape_setPosition(walls, pos_wall);
    sfRectangleShape_setSize(walls, size_wall);
    sfRectangleShape_setOutlineThickness(walls, wall_thickness);
    sfRectangleShape_setOutlineColor(walls, sfBlack);

    const char *font_file = "Digital7Mono-B1g5.ttf";
    sfFont *score_font = sfFont_createFromFile(font_file);
    if(!score_font) {
        printf("Error! File %s not found!\n", font_file);
        return 1;
    }

    const int score_width_offset = 200;
    const int score_height_offset = 20;
    sfText *score_text1 = sfText_create();
    sfText *score_text2 = sfText_create();
    sfText_setFont(score_text1, score_font);
    sfText_setFont(score_text2, score_font);

    sfVector2f pos_score1 = {WIDTH / 2 - score_width_offset, score_height_offset};
    // acel 25 e hardcoded... trebuie sa scadem cat ocupa scorul pe x
    sfVector2f pos_score2 = {WIDTH / 2 + score_width_offset - 25, score_height_offset};
    sfText_setPosition(score_text1, pos_score1);
    sfText_setPosition(score_text2, pos_score2);

    const int score_size = 72;
    sfText_setCharacterSize(score_text1, score_size);
    sfText_setCharacterSize(score_text2, score_size);

    const int score_buf_size = 20;
    char player1_score_buf[score_buf_size];
    char player2_score_buf[score_buf_size];

    unsigned int target_score = 5;
    char main_text_buf[300];
    sfText *main_text = sfText_create();
    sfText_setFont(main_text, score_font);
    sfText_setCharacterSize(main_text, score_size);

    init();
    /// end initializations for middle bar, walls, score and fonts
    ////////////////////////////////////////////////////////////////

    while(sfRenderWindow_isOpen(window)) {
        sfEvent event;
        while (sfRenderWindow_pollEvent(window, &event))
        {
            if (event.type == sfEvtClosed) {
                sfRenderWindow_close(window);
            }
            else if(event.type == sfEvtKeyPressed) {
                /// keyboard events
                switch(event.key.code) {
                case sfKeyEscape:
                    sfRenderWindow_close(window);
                    break;
                case sfKeyW:
                    if(pos_player1.y > player_speed)  /// check bounds
                        pos_player1.y -= player_speed;
                    break;
                case sfKeyS:
                    if(pos_player1.y < HEIGHT - size_player.y - player_speed)
                        pos_player1.y += player_speed;
                    break;
                case sfKeyI:
                    if(pos_player2.y > player_speed)
                        pos_player2.y -= player_speed;
                    break;
                case sfKeyK:
                    if(pos_player2.y < HEIGHT - size_player.y - player_speed)
                        pos_player2.y += player_speed;
                    break;
                case sfKeyP:
                    pause = !pause;
                    break;
                case sfKeyR:
                    if(event.key.control) {
                        init();
                    }
                    break;
                case sfKeyH:
                    pause = true;
                    help = !help;
                    break;
                default:
                    break;
                }
                /// end keyboard events
            }
        }

        if(pause) {
            strcpy(main_text_buf, "Game paused");
            if(help)
                strcat(main_text_buf,
                       "\n\nW - Left player up"
                       "\n\nS - Left player down"
                       "\n\nI - Right player up"
                       "\n\nK - Right player down"
                       "\n\nP - Toggle pause"
                       "\n\nCtrl+R - Reset game"
                       "\n\nH - Toggle help and pause"
                       "\n\nEsc - Quit"
                      );
        }
        else if(player1_score >= target_score) {
            strcpy(main_text_buf, "Left player won!");
            game_end = true;
        }
        else if(player2_score >= target_score) {
            strcpy(main_text_buf, "Right player won!");
            game_end = true;
        }
        if(pause || game_end) {
            sfRenderWindow_clear(window, sfColor_fromRGB(160, 160, 160));

            int pos_text_width = (WIDTH - 30*strlen(main_text_buf)) / 2;
            int pos_text_height = HEIGHT / 2 - 100;
            if(help) {
                pos_text_width = 100;
                pos_text_height = 20;
            }
            sfVector2f pos_main_text = {pos_text_width, pos_text_height};
            sfText_setPosition(main_text, pos_main_text);
            sfText_setString(main_text, main_text_buf);
            sfRenderWindow_drawText(window, main_text, NULL);
            sfRenderWindow_display(window);
            continue;
        }

        const int dir_multiplier = 2;
        if(fabs(pos_ball.x - pos_player1.x) < EPS_X && fabs(pos_ball.y - pos_player1.y) < EPS_Y) {
            dir_ball.x = -dir_ball.x;  /// left player hits the ball
            /// ball reflects on the y axis proportionally with the collision point
            /// of the ping pong paddle relative to the middle
            dir_ball.y += dir_multiplier * (pos_ball.y - pos_player1.y) / PSIZE_Y;
        }
        else if(fabs(pos_ball.x - pos_player2.x) < EPS_X && fabs(pos_ball.y - pos_player2.y) < EPS_Y) {
            dir_ball.x = -dir_ball.x;
            dir_ball.y += dir_multiplier * (pos_ball.y - pos_player2.y) / PSIZE_Y;
        }

        if(pos_ball.x > 0 && pos_ball.x < WIDTH - 50)
            pos_ball.x += dir_ball.x;
        else {
            if(pos_ball.x < WIDTH / 2)
                player2_score++;
            else
                player1_score++;

            pos_ball = pos_ball_start;
            dir_ball.y = 0;
        }

        pos_ball.y += dir_ball.y;
        if(pos_ball.y < 20 || pos_ball.y > HEIGHT - 50)
            dir_ball.y = -dir_ball.y;  /// collision with top and bottom

        /// update positions
        sfRectangleShape_setPosition(player1, pos_player1);
        sfRectangleShape_setPosition(player2, pos_player2);
        sfCircleShape_setPosition(ball, pos_ball);

        /// update text scores
        sprintf(player1_score_buf, "%u", player1_score);
        sprintf(player2_score_buf, "%u", player2_score);
        sfText_setString(score_text1, player1_score_buf);
        sfText_setString(score_text2, player2_score_buf);

        ////////////////////////////////////////////////////////////////
        /// rendering
        sfRenderWindow_clear(window, sfColor_fromRGB(60, 60, 60));
        /// fileu
        for(int i = 0; i < n_points; i++) {
            sfRenderWindow_drawRectangleShape(window, middle[i], NULL);
        }
        sfRenderWindow_drawRectangleShape(window, walls, NULL);
        sfRenderWindow_drawText(window, score_text1, NULL);
        sfRenderWindow_drawText(window, score_text2, NULL);
        sfRenderWindow_drawRectangleShape(window, player1, NULL);
        sfRenderWindow_drawRectangleShape(window, player2, NULL);
        sfRenderWindow_drawCircleShape(window, ball, NULL);
        sfRenderWindow_display(window);
        /// end rendering
        ////////////////////////////////////////////////////////////////
    }

    sfRectangleShape_destroy(player1);
    sfRectangleShape_destroy(player2);
    sfCircleShape_destroy(ball);

    /// fileu
    for(int i = 0; i < n_points; i++)
        sfRectangleShape_destroy(middle[i]);
    free(middle);

    sfRectangleShape_destroy(walls);
    sfText_destroy(score_text1);
    sfText_destroy(score_text2);
    sfText_destroy(main_text);
    sfFont_destroy(score_font);

    sfRenderWindow_destroy(window);
    return 0;
}
