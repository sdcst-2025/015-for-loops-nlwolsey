#!python3
import time

# this command gets the current epoch time, or the number of seconds
# that have passed since Jan 1, 1970
start = time.time()
x = 0
for i in range(2000000):
  x = x + 1
end = time.time()

elapsedTime = end - start
print(f"The final value of x is {x}")
print(f"It took {elapsedTime} seconds to count from 0 to 2 million")

