#include <iostream>
using namespace std;

int linear_search(int a[], int l, int key) {
    for (int i = 0; i < l; i++) {
        if (a[i] == key) {  // если элемент в массиве совпадает с искомым значением
            return i;  // возвращаю индекс найденного элемента
        }
    }
    return -1;
}

int max_search(int a[], int l) {
    // int max = INT_MIN; <- константа, которая хранит первое число из диапазона значений INT - -2147836648
    // int max = 0; <- мы берем 0 как наибольшее число в массиве (если в массиве ТОЛЬКО отрицательные числа, то 0 будет наибольшим)
    int max = a[0];  // самым большим элементом в массиве принимается первый элемент по счету
    for (int i = 1; i < l; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;
}


void find_range(int a[], int l, int min, int max) {
    for (int i = 0; i < l; i++) {
        if ((a[i] > min) && (a[i] < max)) {
            cout << a[i] << " ";
        }
    }
    cout << endl;
}

int lists_hw1() {
    int array[] { 4, 3130, 12, 8, 90, 15, 78, 22, 98, 100, 215, 74, 14, 17, 8, 2, 3, 10, 7, 999 };
    int res = max_search(array, 20);
    cout << "Max element of array is: " << res << endl;
    find_range(array, 20, 1, 10);
    return 0;
}