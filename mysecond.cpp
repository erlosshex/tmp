#include <iostream>

using namespace std;

void init_window(void);
char init_menu(void);


int main(int argc, char **argv)
{
  init_window();
  char c=init_menu();
  cin.get();
  while(c=='a'){
    init_window();
    c=init_menu();
    cin.get();
  }
  return 0;
}

void init_window(void)
{
  int max_iter=100;
  for(int i=0;i<max_iter;++i)
    cout<<'\n';
  cout<<endl;
}

char init_menu(void)
{
  cout<<"please choose a choice from below:"<<endl;
  cout<<"eixt    -- q"<<endl;
  cout<<"another -- a"<<endl;
  return cin.get();
  
}
