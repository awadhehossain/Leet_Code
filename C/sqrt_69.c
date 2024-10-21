#include<stdio.h>
#include<math.h>
int mySqrt(int x) {
    int z=sqrt(x);
    return z;
    
}
int main()
{
    int x;
    scanf("%d",&x);
    int k=mySqrt(x);
    printf("%d",k);

    return 0;


}