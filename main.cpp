#include <iostream>
using namespace std;


void sort(int a[], int length) {
    for (int i = 0; i < length - 1; i++) {
        for (int j = 0; j < length - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                // swap(a[j], a[j + 1]);  // меняю местами числа - только в C++
                int temp = a[j];  // сохраняю во временной переменной значение текущего элемента
                a[j] = a[j + 1];  // присваиваю текущему значение следующего
                a[j + 1] = temp;  // следующему присваиваю значение предыдущего
            }
        }
    }
}


int main() {
    int a[6] { 9, 3, 6, 2, 10, 1 };
    sort(a, 6);
    for (int key : a) {
        cout << key << " ";
    }
    return 0;
}