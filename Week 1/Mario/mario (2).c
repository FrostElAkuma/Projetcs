#include <cs50.h>
#include <stdio.h>


int oneEight(void);

int main (void)
{
    
 int n = oneEight();

 for (int i = 0; i < n; i++)
 {
    
   int m1 = n-1;
   int space = n-i;
   int hash = n+i-m1;
    
   printf("%*s", space, "");
   printf("%.*s", hash, "########");
   printf("  ");
   printf("%.*s", hash, "########");
   printf("\n");
  
 }

}

int oneEight(void)
{
 int o; 
   do
    {
      o = get_int("Please inter a value form 1-8: ");
    }
 while (o<1 || o>8); 
 
return o;     

}

