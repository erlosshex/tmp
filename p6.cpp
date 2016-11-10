#include <iostream>

double change(double);

int main(int argc, char **argv)
{
  using namespace std;
  cout<<"Enter the number of light years: ";
  double num;
  cin>>num;
  cout<<num<<" light years = "<<change(num)<<" astronomical units."<<endl;
  return 0;
}

double change(double num)
{
  return 63240*num;
}
