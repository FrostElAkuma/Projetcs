#include <cs50.h>
#include <stdio.h>

int main(void)
{

 int start;
 int years =0;

  do
  {
      start = get_int("Please inter a starting population number that is equal or greater than 9: ");
  }
  while (start < 9);  // TODO: Prompt for start size

     int end;
  do
  {
      end = get_int("Please inter an end population size that is larger or equal to the starting one: ");
  }

  while (end < start); // TODO: Prompt for end size

  while (start<end)
  {
     int born = start/3;  // TODO: Calculate number of years until we reach threshold
     int dead = start/4;
     start = start + born - dead;
     years++;
  }

  printf("Years: %i\n", years);
    // TODO: Print number of years
}
