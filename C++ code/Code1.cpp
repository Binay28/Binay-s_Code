#include <iostream>
using namespace std;
main()
{
  int agetot=0,nop=0,age;
  cout<<"Enter the first person's age or -1 to quit"<<endl;
  cin>>age;
  while(age !=-1)
    {
      agetot+=age;
      nop++;
       cout<<"Enter the Person's age or -1 to quit"<<endl;
      cin>>age;
    }
  cout<<"number of people entered"<<nop<<endl;
  cout<<"total age:"<<agetot<<endl;
}
