#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
	int n = 1000000, * v;
	double t;

	v = new int[n];

	srand(time(NULL));

	// srand(100);

	t = clock();

	for (int i = 0; i < n; i++) {
		v[i] = rand();
	}

	/*
	cout << "Tabolul initial: " << endl;
	for (int i = 0; i < n; i++) {
		cout << v[i] << " ";
	}
	*/

	cout << endl;

	t = clock();

	sort(v, v + n);

	t = clock() - t;

	cout << endl;

	/*
	cout << "Tabloul sortat:" << endl;
	for(int i = 0; i < n; i++)
	cout << v[i] << " ";
	cout << endl;
	*/

	cout << endl;

	cout << "Timp de executare: " << t / CLOCKS_PER_SEC << "s" << endl;
	
	delete[]v;

	return 0;
}