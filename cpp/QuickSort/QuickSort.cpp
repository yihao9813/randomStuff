//Sort number with descending order
#include <iostream>

using namespace std;

void swap(int &a, int &b)
{
    int tmp;
    tmp = a;
    a = b;
    b = tmp;
}

int Partition(int A[], int left, int right)
{
    int pivot;
    pivot = right;
    while (left < right)
    {
        while (A[left] >= A[pivot] && left < right)
        {
            left++;
        }
        while (A[right] <= A[pivot] && left < right)
        {
            right--;
        }
        swap(A[left], A[right]);
    }
    swap(A[right], A[pivot]);
    return right;
}

void QuickSort(int A[], int left, int right)
{
    int mid;
    if (left >= right)
        return;
    mid = Partition(A, left, right);
    QuickSort(A, left, mid - 1);
    QuickSort(A, mid + 1, right);
}

void getInput(int *A, int &total)
{
    total = 0;
    cout << "Enter any numbers : (Input 'End' to STOP)" << endl;
    while (cin >> *(A + total))
    {
        ++total;
    }
}

int main()
{
    int total;
    int *A;
    getInput(A, total);
    QuickSort(A, 0, total-1);
    for (int i = 0; i < total; ++i)
    {
        cout << A[i] << ' ';
    }
    system("pause");
    return 0;
}