"""
To start, we will generate a random integer between 1 and 20, and
based on the result of the random number, we check to see if it falls under certain range
if the number is greater than 15, then the result will be "Cherries"
otherwise if the number is greater than 10, then the result will be "Orange"
otherwise if the number is greater than 5, then the result will be "Plum"
otherwise if the number is greater than 2, then the result will be "Melon"
otherwise if the number is greater than 1, then the result will be "Bell"
otherwise the number is not any of the above, then the result will be "Bar"

we iterate over using a loop three times and print the results to the user. As an example "Plum Cherries Melon"

"""

"""
import random
num = generate random number

if num is greater than 15, 
  then the result will be "Cherries"
otherwise if num > 10, 
  then the result will be "Orange"
otherwise if num > 5, 
  then the result will be "Plum"
otherwise if num > 2, 
  then the result will be "Melon"
otherwise if num > 1 
  then the result will be "Bell"

loop three times 
  print the output (fruit) to the user
"""

import random 

def main():
  for i in range (0, 3):
    spin()

def spin():
  rand_num = random.randint(1, 20)
  output = ""
  if(rand_num > 15):
    output = "Cherries"
  elif(rand_num > 10):
    output = "Orange"
  elif(rand_num > 5):
    output = "Plum"
  elif(rand_num > 2):
    output = "Melon"
  elif(rand_num > 1):
    output = "Bell"
  else:
    output = "Bar"

  print(output, end=" ")

main()