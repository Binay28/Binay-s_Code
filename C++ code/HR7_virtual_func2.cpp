#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
public:
  int age;
  string name;
  virtual void getdata() {}
  virtual void putdata() {}
};
class Professor : public Person {
public:
  int publications, cur_id;
  static int cur_id_p;
  Professor() {
    cur_id_p++;
    cur_id = cur_id_p;
  }
  void getdata() { cin >> name >> age >> publications; }
  void putdata() {
    cout << name << " " << age << " " << publications << " " << cur_id << endl;
  }
};
class Student : public Person {
public:
  int marks[6], sum, cur_id;
  Student() {
    sum = 0;
    cur_id_s++;
    cur_id = cur_id_s;
  }
  static int cur_id_s;
  void getdata() {
    cin >> name >> age;
    for (int i = 0; i < 6; i++) {
      cin >> marks[i];
      sum += marks[i];
    }
  }
  void putdata() {
    cout << name << " " << age << " " << sum << " " << cur_id << endl;
  }
};
int Professor::cur_id_p = 0;
int Student::cur_id_s = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
