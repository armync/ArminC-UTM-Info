// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#include "pixel.h"

#define GET_PIXEL(a, i, j) (*(*(a + i) + j))

void colorToGray(Picture *pic)
{
	for (int i = 0; i < pic->height; ++i)
		for (int j = 0; j < pic->width; ++j) {
			GET_PIXEL(pic->pix_array, i, j).R *= 0.3;
			GET_PIXEL(pic->pix_array, i, j).G *= 0.59;
			GET_PIXEL(pic->pix_array, i, j).B *= 0.11;
		}
}

void swapRows(Pixel *row1, Pixel *row2, int width)
{
	// Interschimbăm fiecare element din cele 2 linii.
	for (int i = 0; i < width; ++i) {
		Pixel temp = row1[i];

		row1[i] = row2[i];
		row2[i] = temp;
	}
}

void reversePic(Picture *pic)
{
	for (int i = 0; i < pic->height / 2; ++i)
		swapRows(pic->pix_array[i], pic->pix_array[pic->height - 1 - i],
				pic->height);
}

int main(void)
{
	int height, width;

	scanf("%d%d", &height, &width);
	Pixel **pix_array = generatePixelArray(height, width);
	Picture *pic = generatePicture(height, width, pix_array);

	printPicture(pic);
	printf("\n");
	colorToGray(pic);
	printPicture(pic);
	printf("\n");
	reversePic(pic);
	printPicture(pic);

	freePicture(&pic);
	freePixelArray(&pix_array, height, width);

	return 0;
}
