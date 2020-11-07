#include<iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int i,j,k,n,stages,min=9999;
	cout<<"Enter total number of vertices"<<endl;
	cin>>n;
	cout<<"Enter stages"<<endl;
	cin>>stages;
	int cost[n+1],c[n+1][n+1],d[n+1],path[stages+1];
	cost[n]=0;
	path[1]=1;
	path[stages]=n;
	for(i=0;i<=n;i++)
	{
		for(j=0;j<=n;j++)
		{
			c[i][j]=0;
		}
	}
	cout<<"Enter weight of edges"<<endl;
	for(i=0;i<=n;i++)
	{
		for(j=0;j<=n;j++)
		{
			cin>>c[i][j];
		}
	}
	for(i=n-1;i>=1;i--)
	{
		min=9999;
		for(k=i+1;k<=n;k++)
		{
			if(c[i][k]!=0 && cost[k]+c[i][k]<min)
			{
				min=c[i][k]+cost[k];
				d[i]=k;
			}
		}
		cost[i]=min;
	}
	for(i=2;i<stages;i++)
	{
		path[i]=d[path[i-1]];
	}
	cout<<"Cost of given graph = "<<cost[1]<<endl;
	cout<<"Path = ";
	for(i=1;i<stages;i++)
	{
		cout<<path[i]<<"-";
	}
	cout<<path[stages]<<endl;
	return 0;
}	
