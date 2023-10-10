"""
If the for loop runs through the entire list of values,
it will automatically run the else statement as well
range(10) actually represents a tuple that looks like
(0,1,2,3,4,5,6,7,8,9)
and then iterates through the list
"""

for i in range(10):
  print(f"The number right now is {i}")
else:
  print("We are finished!")
