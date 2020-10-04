#include<iostream>
using namespace std;
int main()
{
  int n;
  cout<<"Array Size: ";
  cin>>n;
  int a[n];
  for(int i=0;i<n;i++)
  	cin>>a[i];
  cout<<"Element to Search: ";
  int x;
  cin>>x;
  for(int i=0;i<n;i++)
  {
    if(a[i]==x)
    {
      cout<<"Element found at position "<<i+1<<endl;
      return 0;
    }
  }
  cout<<"Element not found"<<endl;
  return 0;
}
