'''
	File Name: errors.py
	Author: Mansoor Muhammad
	Date Created: March 29, 2019
	Date Last Edited: Sept 23, 2024
'''

# From input, recieve two integers from the user and add them together.  Output the result.
def q1():
  num1 = input("Input a number: ")
  num2 = input("Input a number: ")
  num1 = int(num1)
  num2 = int(num2)
  print(num1 + num2)

# From input recieve two integers.  Output the quotient rounded down.

def q2():
  won3 = input("Input a number: ")
  one2 = input("Input a number: ")
  won3 = int(won3)
  one2 = int(one2)
  print (int(won3 / one2))

# Output the phrase "hello Mr. Kalisz have you seen my work yet?"

def q3():
  print ("hello Mr. Kalisz have you seen my work yet?")

# From input recieve two numbers (can be decimal fractions).  
# Output their result multiplied together.  Then round down to the nearest whole number

def q4():
  nimb1 = input("Input a number: ")
  num2 = input("Input a number: ")
  nimb1 = float(nimb1)
  num2 = float(num2)
  print (int(nimb1 * num2))
'''
q1()
q2()
q3()
q4()
'''