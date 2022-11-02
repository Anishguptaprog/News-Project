#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a=1;
    vector<int>b={1, 2, 50};
    for(int i=0;i<b.size();i++)
    {
        if(b[i] == a-1)
        {
            a--;
            continue;
        }
        if(b[i]==a+1)
        {
            a++;
            continue;
        }
    }
    cout<<a+1<<endl;
    return 0;
}