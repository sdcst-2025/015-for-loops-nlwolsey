#! python3

"""
A tuple or list is a variable type that contains multiple pieces of data. To access the members of a tuple or list, you can use a for x in y: loop or try to call the individual members using an "index" An index is an integer in a set of [] following the tuple name.  The numbers in the index start at 0 and increase as integers
"""
print("===================")
print(" tuples and lists  ")
print("===================")
print("\n\n")
# this is how a tuple is defined
myFriends = ("Carol","Christine","Dan","Richard")

# this is how a list is defined
otherFriends = ["Oscar","Benjamin","Casey","Chessy"]

# we can print out the entire list or tuple using its name
print(myFriends)
print(otherFriends)


# to reference members of the tuple or list, use an index inside the square bracket:
# the index starts at 0 and increases by 1
print(myFriends[1] + " is one of the people that I have known the longest!")
print(f"{otherFriends[0]} is a good friend!")
print("\n")
# we can easily change the value of a list item:
otherFriends[2] = "Chessy"
print(otherFriends)

print("\n")
# if we try to change the value of a tuple item, we get an error:
# TypeError: 'tuple' object does not support item assignment
myFriends[3] = "Ricky"