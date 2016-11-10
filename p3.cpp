#include <iostream>

void f1(void);
void f2(void);

int main(int argc, char **argv)
{
  for(int i=0;i<2;++i)
    f1();
  for(int i=0;i<2;++i)
    f2();
  return 0;
}

void f1()
{
  using namespace std;
  cout<<"Three blind mice"<<endl;
}
void f2()
{
  using namespace std;
  cout<<"See how they run"<<endl;
}
