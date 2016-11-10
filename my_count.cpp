#include <iostream>
#include <map>
#include <vector>

int main(int argc, char **argv)
{
  using namespace std;

  map<int,int> my_map;
  vector<int> my_vector={1,1,1,1,1,1,2,2,2,3,4,4,5,5};
  cout<<"vector --"<<endl;
  for(vector<int>::iterator i=my_vector.begin();i!=my_vector.end();++i)
  {
    cout<<*i<<" ";
    
    if(my_map.end()==my_map.find(*i))  my_map.insert(my_map.begin(),pair<int,int>(*i,1));
    else my_map[*i]=my_map[*i]+1;
  }
  cout<<endl;
  cout<<"map --"<<endl;
  for(map<int,int>::iterator i=my_map.begin();i!=my_map.end();++i)
  {
    cout<<(*i).first<<" --> "<<(*i).second<<endl;
  }
  return 0;
}
