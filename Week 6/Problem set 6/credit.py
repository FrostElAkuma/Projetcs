from cs50 import get_int
import math


noMultiply = 0
multiply = 0
extra1 = 0
extra2 = 0
afterMultiply = 0

list1 = [51, 52, 53, 54, 55]
list2 = [34, 37]


flag = True

while flag:
    creditNumber = get_int("Number: ")
    if creditNumber > 0: #To make sure that the Credit card number is a positive number
        flag = False


testCreditNumber = creditNumber #to keep a copy of the original credit card number

while (testCreditNumber > 0): #Luhn Algorithm

    noMultiply += testCreditNumber % 10 #module to get the last number
    testCreditNumber = math.floor(testCreditNumber / 10) #math.floor to get rid of the last number cuz python needs rounding
    multiply = testCreditNumber % 10 * 2
    extra1 = multiply % 10
    extra2 = math.floor(multiply / 10)
    afterMultiply += extra1 + extra2
    testCreditNumber = math.floor(testCreditNumber / 10)

#checking the type of creditcard and see if it is VALID

if ((afterMultiply + noMultiply) % 10 == 0):
    if math.floor(creditNumber / 1000000000000000) == 4 or math.floor(creditNumber / 100000000000000) == 4 or math.floor(creditNumber / 10000000000000) == 4 or math.floor(creditNumber / 1000000000000) == 4:
        print("VISA")

    elif math.floor(creditNumber / 100000000000000) in list1:
        print("MASTERCARD")

    elif math.floor(creditNumber / 10000000000000) in list2:
        print("AMEX")

    else:
        print("INVALID")

else:
    print("INVALID")