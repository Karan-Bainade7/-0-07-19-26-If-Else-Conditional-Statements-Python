# If Else Conditional
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.


age=int(input("enter your age:"))
print("your age is:",age);

if age >18:
    print("you can drive car")
else:
    print("you can't drive car")



a = 33
b = 200

if b > a:
  print("b is greater than a")

else:
   print("not") 



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
