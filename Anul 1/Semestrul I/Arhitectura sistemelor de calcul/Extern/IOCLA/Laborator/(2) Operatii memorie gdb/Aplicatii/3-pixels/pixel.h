/* SPDX-License-Identifier: BSD-3-Clause */

#ifndef __PIXEL_H__
#define __PIXEL_H__

typedef struct Pixel {
	unsigned char R;
	unsigned char G;
	unsigned char B;
} Pixel;

typedef struct Picture {
	int height;
	int width;
	Pixel **pix_array;
} Picture;

Picture *generatePicture(int height, int width, Pixel **pix_array)
{
	Picture *pic = malloc(sizeof(*pic));

	if (pic == NULL) {
		perror("malloc");
		exit(1);
	}

	pic->height = height;
	pic->width = width;

	pic->pix_array = malloc(pic->height * sizeof(*pic->pix_array));
	if (pic->pix_array == NULL) {
		perror("malloc");
		exit(1);
	}

	for (int i = 0; i < pic->height; ++i) {
		pic->pix_array[i] = malloc(pic->width * sizeof(**pic->pix_array));
		if (pic->pix_array[i] == NULL) {
			perror("malloc");
			exit(1);
		}
	}

	for (int i = 0; i < pic->height; ++i)
		for (int j = 0; j < pic->width; ++j)
			pic->pix_array[i][j] = pix_array[i][j];

	return pic;
}

Pixel generatePixel (const unsigned char R,
					const unsigned char G, const unsigned char B)
{
	Pixel pixel;

	pixel.R = R;
	pixel.G = G;
	pixel.B = B;

	return pixel;
}

void printPicture(Picture *pic)
{
	for (int i = 0; i < pic->height; ++i) {
		for (int j = 0; j < pic->width; ++j) {
			printf("%u %u %u ", pic->pix_array[i][j].R,
						pic->pix_array[i][j].G, pic->pix_array[i][j].B);
			if (j != pic->width - 1)
				printf(" | ");
		}
		printf("\n");
	}
}

Pixel **generatePixelArray(int height, int width)
{
	Pixel **pix_array = malloc(height * sizeof(*pix_array));

	if (pix_array == NULL) {
		perror("malloc");
		exit(1);
	}

	for (int i = 0; i < height; ++i) {
		pix_array[i] = malloc(width * sizeof(**pix_array));
		if (pix_array[i] == NULL) {
			perror("malloc");
			exit(1);
		}
	}

	time_t t;

	srand((unsigned int) time(&t));

	for (int i = 0; i < height; ++i)
		for (int j = 0; j < width; ++j)
			pix_array[i][j] = generatePixel(rand() % 256,
				rand() % 256, rand() % 256);

	return pix_array;
}

void freePixelArray(Pixel ***pix_array, int height, int width)
{
	(void) width;

	for (int i = 0 ; i < height ; ++i)
		free((*pix_array)[i]);

	free(*pix_array);
}

void freePicture(Picture **pic)
{
	freePixelArray(&(*pic)->pix_array, (*pic)->height, (*pic)->width);
	free(*pic);
}

#endif // __PIXEL_H__
