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

int count_el(int a[], int l, int elem) {
    int count = 0;  // в переменной буду считать количество вхождений элемента elem в массив a
    for (int i = 0; i < l; i++) {
        if (a[i] == elem) {  // если какое-то число в массиве совпадает с искомым
            count++;  // увеличиваю счетчик на 1
        }
    }
    return count;
}

bool is_sorted(int a[], int l) {
    for (int i = 1; i < l; i++) {
        if (a[i] < a[i - 1]) {
            return false;
        }
    }
    return true;
}

bool is_sorted_v2(int a[], int l) {
    for (int i = 0; i < l; i++) {  // внешний цикл НЕ РАБОТАЕТ, пока не закончит работу внутренний
        for (int j = i; j < l - 1; j++) {
            if (a[i] > a[j]) {
                return false;
            }
        }
    }
    return true;
}

int arrays_start() {
    const int len = 10;
    int arr[len] = { 4, 12, 89, 2, 6, 4, 17, 4, 2, 74 };
    int arr2[len] = { 10, 23, 56, 78, 94, 101, 374, 428, 490, 621 };

    for (int i = 0; i < len; i++) {
        cout << arr[i] << endl;
    }

    int key = 120;
    cout << "Index: " << linear_search(arr, len, key) << endl;
    cout << "How many 89: " << count_el(arr, len, 89) << endl;
    cout << "Is sorted: " << is_sorted(arr2, len) << endl;
    cout << "Is sorted: " << is_sorted(arr, len) << endl;

    return 0;
}