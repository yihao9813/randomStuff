#include <iostream>

using namespace std;

int BiSearch(int array[], int min, int max, int target)
{
    int mid;
    mid = (max - min) / 2 + min;
    if (min > max)
        return -1;
    if (array[mid] == target)
        return mid;
    if (target > array[mid])
        BiSearch(array, mid + 1, max, target);
    else
        BiSearch(array, min, mid - 1, target);
}

int main()
{
    int array[100];
    for (int i = 0; i < 100; ++i)
        array[i] = i;

    int target = 37;
    int x = BiSearch(array, 0, 99, target);
    if (x == -1)
        cout << "Element Not Found !" << endl;
    else
        cout << "Elemtn found at index " << x << endl;
    system("pause");
    return 0;
}
