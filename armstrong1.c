#include <stdio.h>

int digitcounter(int d);
int expo(int a,int b);

int main()
{
    int m,a,r,i,o=0;
    printf("Enter number: ");
    scanf("%d",&r);
    m=r;
    i=digitcounter(r);
    for (int d=1;d<=i;d++)
    {
        a=m%10;
        o=expo(a,i)+o;
        m=m/10;
    }
    if (o==r)
        printf("Armstrong");
    else
        printf("Not armstrong");
    return 0;
}

int digitcounter(int d)
{
    int i=0;
    while (d>=1)
    {
        d=d/10;
        i++;
    }
    return i;
}

int expo(int a,int b)
{
    for(int z=1;z<b;z++)
        a=a*a;
    return a;
}