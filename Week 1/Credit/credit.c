#include <cs50.h>
#include <stdio.h>

int main(void)
{

 long creditNumber;
 int noMultiply = 0, multiply = 0, extra1 = 0, extra2= 0, afterMultiply = 0;


  do
  {
      creditNumber = get_long("Please inter a valid credit card number: ");     // getting the credit card number
  }
  while (creditNumber < 0);  // To make sure that the Credit card number is a posotive number

long testCreditNumber = creditNumber; //to keep a copy of the orignal credit card number 

 while (testCreditNumber > 0)  // Luhn Algorithm
 {
  noMultiply += testCreditNumber % 10;
  testCreditNumber /= 10;
  multiply = testCreditNumber % 10 * 2;
  extra1 = multiply % 10;
  extra2 = multiply / 10;
  afterMultiply += extra1 + extra2;
  testCreditNumber /= 10;

 }

//checking the type of creditcard and see if its VALID

if ((afterMultiply + noMultiply) % 10 == 0) { 
  if (creditNumber / 1000000000000000 == 4 || creditNumber / 100000000000000 == 4 || creditNumber / 10000000000000 == 4 || creditNumber / 1000000000000 == 4) {
 printf("VISA\n");}
 
 else if (creditNumber / 100000000000000 == 51 || creditNumber / 100000000000000 == 52 || creditNumber / 100000000000000 == 53 || creditNumber / 100000000000000 == 54 || creditNumber / 100000000000000 == 55) {
 printf("MASTERCARD\n");}
 
 else if (creditNumber / 10000000000000 == 34 || creditNumber / 10000000000000 == 37){
 printf("AMEX\n");}
 
 else {
 printf("INVALID\n");
}
}
 else {
 printf("INVALID\n");
}
 
}


 





