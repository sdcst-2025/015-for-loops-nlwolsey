#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""

s = int(input("enter the side of a box (integer less than 10): "))
if s >= 10:
    print("invalid, value is greater than or equal to 10")
else:
    for i in range(s):
        for r in range(s):
            print("*", end= '' )
        print("")