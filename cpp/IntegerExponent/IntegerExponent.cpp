//Output x^n with complexity of O(n)
//Input:x^n

#include <iostream>

using namespace std;

double BinaryExponent(double x,int n)
{   
    double y = 1;
    while (n>0)
    {
        if (n % 2 == 1)
            y*=x;
        x*=x;
        n/=2;
    }
    return y;
}

int main()
{
    double x,result;
    int n;
    char a;

    cin>>x>>a>>n;
    
    result = BinaryExponent(x,n);
    cout << "Output : " << result <<endl ;

    system("pause");
    return 0;
}