//Find Maximum Sum in an  Array

#include <iostream>
#include <climits>
using namespace std;

int maxSubArraySum(int *a, int size)
{
    int max_so_far = INT_MIN, max_ending_here = 0;

    for (int i = 0; i < size; i++)
    {
        max_ending_here = max_ending_here + a[i];
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;
        if (max_ending_here < 0)
            max_ending_here = 0;
    }
    return max_so_far;
}

int *getInput(int &n)
{
    int *A;
    cout << "Enter Quantity of Numbers : ";
    cin>> n ;
    A = new int[n];
    cout << "Enter a set of Numbers : " << endl;
    for (int i = 0 ; i < n ; ++i)
        cin>>A[i];

    return A;
}

int main()
{
    int *array;
    int total = 0;

    array=getInput(total);

    int max_sum = maxSubArraySum(array, total);
    cout << "Maximum contiguous sum is " << max_sum << endl;
    
    system("PAUSE");
    return 0;
}
