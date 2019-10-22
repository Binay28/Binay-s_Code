#include <iostream>
//#include <cstdio>
//#include<string>
using namespace std;

int main() {
    // Complete the code.
    int a,b;
    char w[9][10]={"one","two","three","four","five","six","seven","eight","nine"};
    //cin>>a>>b;
    cout<<"enter the start :";
    cin>>a;
    cout<<"enter the end :";
    cin>>b;
    if(a<=9 && b<=9)
    {
      for (int i = a; i <= b; i++) 
	puts(w[i-1]);
    }
    else if(a<=9 && b>9)
    {
      for (int i = a; i <= 9; i++)
        puts(w[i - 1]);
      for(int i=10;i<=b;i++)
       {
           if(i%2==0)
	     cout<<"even"<<endl;
           else
	     cout<<"odd"<<endl;
       }
    }
    else
    {
        for(int i=a;i<=b;i++)
        {
            if(i%2==0)
            cout<<"even";
            else
            cout<<"odd";
        }
    }
    return 0;
}

