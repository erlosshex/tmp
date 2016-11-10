#include <iostream>

int main(int argc, char **argv)
{
  using namespace std;
  int long_num,ma_num;
  int change_num=220;
  cout<<"input a number(long) : ";
  cin>>long_num;
  ma_num=long_num*change_num;
  cout<<"output a number(ma)  : ";
  cout<<ma_num<<endl;
  return 0;
}
