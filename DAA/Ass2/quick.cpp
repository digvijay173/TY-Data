#include <iostream>
using namespace std;

int partition(int l,int r,int a[])
{
  int pivot=a[l],i,j;
  i=l;
  j=r;
  while (i<j) {
    while(a[i]<=pivot) {
      i++;
    }
    while(pivot<a[j]) {
      j--;
    }
    if (i<j) {
      int temp1;
      temp1=a[j];
      a[j]=a[i];
      a[i]=temp1;
    }
  }
  int temp2;
  temp2=a[j];
  a[j]=a[l];
  a[l]=temp2;
  return j;
}

void quicksort(int l,int r,int a[])
{
  if(l<r)
  {
    int p = partition(l,r,a);
    quicksort(l,p-1,a);
    quicksort(p+1,r,a);
  }
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  std::cout << "Enter Size : ";
  cin>>n;
  int a[n];
  std::cout << "Enter Array : ";
  for (int i = 0; i < n; i++) {
    cin>>a[i];
  }
  quicksort(0,n-1,a);
  std::cout << "Sorted Array : ";
  for (int i = 0; i < n; i++) {
    std::cout << a[i]<<" ";
  }
  std::cout<< '\n';
}
