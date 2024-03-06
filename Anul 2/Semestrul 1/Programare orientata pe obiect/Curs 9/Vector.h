template<class T> class Vector
{
    int dim;
    T* pv;

public:
    Vector(int n);
    void afisare();
    T& operator[](int i);

};
