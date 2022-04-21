//To list all prime number from 2~N which N is given by user
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main()
{
    int limit,times =0;
    cout<<"Please enter a number: ";
    cin>>limit;

    bool prime[limit];
    for(int i=0 ; i <= limit ; i++){
        prime[i]=true;
    }

    for (int i = 2 ; i < sqrt(limit)+1 ; i++){
        if (prime[i]){
            for (int j = i*i ; j <= limit ; j+=i){
                times++;
                prime[j]=false;}
        }
    }
    cout<<"Times :"<<times<<endl;
    for (int i = 2 ; i <= limit ; i++){
        if (prime[i])
            cout<< i << "\t";
    }

    system("pause");
    return 0;
}
