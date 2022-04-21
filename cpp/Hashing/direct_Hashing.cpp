//Direct Address Hashing Function
#include <iostream>
#include "limits.h"

using namespace std;

void cr8_Hash(int *directHash,int array[])
{
    for (int i = 0 ; i < 100 ; ++i)
        *(directHash+array[i])=i;
        //cout<<directHash+array[i]<<' '<<*(directHash+array[i])<<endl;
}

void find(int *hash_table,int n)
{   
    if (*(hash_table+n)==INT_MIN)
        cout<<"Element Not Found !"<<endl;
    else
        cout<<"Element Found !"<<endl;
}

int main()
{

    //Create an array
    int samArray[100];
    for (int i = 0; i < 100; ++i)
        samArray[i] = 300 - i*10;
        
    //Create HashTable
    int *hash_table;
    hash_table= new int[500];
    for (int i = 0 ; i < 500 ; ++i)
        hash_table[i]=INT_MIN;
    cr8_Hash(hash_table,samArray);

    //Find an element in an array
    find(hash_table,55);

    delete []hash_table;
    
    return 0;
}