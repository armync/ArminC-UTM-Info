// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

char *delete_first(char *s, char *pattern)
{
	char *found = strstr(s, pattern);

	// Tratăm cazul în care pattern-ul nu apare în șirul de caractere.
	if (!found)
		return strdup(s);

	// numărul de caractere înainte de prima apariție a pattern-ului
	int nbefore = found - s;
	// numărul de caractere ce vor fi eliminate
	int nremoved = strlen(pattern);
	// Alocăm exact cât avem nevoie.
	char *result = malloc(strlen(s) + 1 - nremoved);

	// Verificăm dacă alocarea a funcționat.
	if (result == NULL) {
		perror("malloc");
		exit(1);
	}

	// Construim rezultatul.
	strncpy(result, s, nbefore);
	strcpy(result + nbefore, found + nremoved);

	return result;
}

int main(void)
{
	/*
	 * Înlocuim *s cu s[], deoarece *s aloca șirul intr-o zona de memorie
	 * read-only (.rodata), iar funcția delete_first() trebuie să modifice
	 * sirul s.
	 */
	char s[] = "Ana are mere";
	char *pattern = "re";

	printf("%s\n", delete_first(s, pattern));

	return 0;
}
