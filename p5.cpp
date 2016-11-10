#include <iostream>

double celsToFahr(double);

int main(int argc, char **argv)
{
  using namespace std;
  cout<<"Please enter a Celsius value: ";
  int cels;
  cin>>cels;
  cout<<cels<<" degrees Celsius is "<<celsToFahr(cels)<<" degrees Fahrenheit."<<endl;
  return 0;
}

double celsToFahr(double num)
{
  return 1.8*num+32.0;
}
