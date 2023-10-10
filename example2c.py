
"""
if you want to break out of the for loop, you can use break at any point
in the block.  All future iterations are skipped and the loop exits at
the current point

The else statement can also be used with a for loop.
Commands in the else block will be run if the for loop
reaches it's end.
"""

players = ("Guile", "Cammy", "Ryu", "Ken", "Chun-Li")

"""
here, i is the indexing variable. 
All the tuple members will take turns being i
"""
for i in players:
    # this will check if the current tuple member is Ryu and then break out of the loop if it is
    if i == "Boris":
        break
    print("===")
    print( i + " is going to the mall")
    print("---")
    print("\n")
else:
    print("The name was not found")
