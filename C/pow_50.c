#include<stdio.h>
#include<math.h>
double myPow(double x, int n) {
    double z=pow(x,n);
    return z;
}
int main()
{
    double x;
    int n;
    scanf("%lf%d",&x,&n);
    double k=myPow(x,n);
    printf("%.2lf",k);


}