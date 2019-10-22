#include <iostream>
#include<cmath>
using namespace std;
main()
{
  float a,p=10000,r=0.01;
  for(int day=1;day<=20;day++)
    {
      a=p*pow(1+r,day);
      cout<<day<<"---------"<<a<<endl;
    }
}
