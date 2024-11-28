#! python3
"""
The indexing variable starts with an initial value, and continues until the
indexing value reaches the ending value.

When 2 values are given, the initial value is set to be the first number
This will iterate through the sequence 10, 11, 12, 13, 14

If we wanted to not use 2 values, we can still use 1 and just modify the output
instead.
"""

for i in range(5):
    print(i+10)
else:
    print("We have printed the numbers 10 through 14!")
