    #include<iostream>
    #include<vector>
    using namespace std;
    int main()
    {
      int elements;
      cout << "Enter number of elements in the array:";
      cin >> elements;
      vector<int> array;
      array.resize(elements);
      int sum=0;
      for(int i=0;i<array.size();i++)
      {
         array[i]=i;
         sum=sum+array[i];
      }
      cout<<sum;
    }
