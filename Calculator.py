#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      samirrayma
#
# Created:     17-07-2023
# Copyright:   (c) samirrayma 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first=(input)("enter first number:")
operator=input("enter oprator (+,-,*,/,%):")
second =(input) ("enter second number:")
first= int(first)
second=int(second)

if operator =="+":
    print(first + second)

elif operator =="-":
    print(first - second)
elif operator =="*":
    print(first * second)
elif operator =="/":
    print(first / second)
elif operator =="%":
    print(first % second)

else:
    print("invalid opration")