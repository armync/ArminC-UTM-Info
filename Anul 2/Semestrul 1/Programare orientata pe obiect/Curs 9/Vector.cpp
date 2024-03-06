#include<iostream>
#include "vector.h"

using namespace std;

template<class T> Vector<T>::Vector(int n)
{

    this->dim = n;
    this->pv = new T[dim];

    for(int i=0; i< dim; i++)
        cin>>pv[i];
}

template<class T> T& Vector<T>::operator[](int i)
{
    return pv[i];
}

template<class T> void Vector<T>::afisare()
{

    for(int i= 0; i<dim; i++)
        cout<<pv[i]<<" ";
    cout<<endl;
}
