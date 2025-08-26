#Let's code with str variable
'''
a = "Hello, World!"
print(a)
'''
'''
Variables in python 
a = "Shanto" (str)
b = 15 (int)
c = 15.66 (float)
d = 10>5 (conditional statement/ boolean{True/False})

Operators in Python
1. Arithmetic Operator:
+ = Addition =      a+b
- = Subtraction =   a-b
* = Multiplication= a*b
/ = Division =      a/b
% = Modulus =       a%b
**= Exponents =     a**b
//= Floor Division= a//b

1.
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

output is
30
-10
200
0.5
10
100000000000000000000
0
'''

'''
2.
pen_number = 14
student_number = 3
# Compute the number of pens each student will get and print it
# Hint: find the quotient
Pens_for_each_student = pen_number//student_number
print(f"Pens for each student: {Pens_for_each_student}") 
# Compute and print the number of remaining pens
# Hint: find the remainder
Remaining_pens = pen_number%student_number
print(f"Remaining pens: {Remaining_pens}")

output is :-
Pens for each student: 4
Remaining pens: 2

3.
tuition_fees = 1536
discount_percentage = 10
# Compute discount and assign it to the discount variable
discount_amm = (discount_percentage / 100) * tuition_fees
after_discount_tuition_fee_is = tuition_fees - discount_amm

# Compute and print the fee you have to pay
print(after_discount_tuition_fee_is)

output is : 1382.4

var = "25.0"

number = float(var)
result = number - 15

print(result)

#######
# Get two floating-point numbers as inputs
num1 = input("Enter a number:")
num2 = input("Enter a another number:")
# Add the numbers
n = float(num1) + float(num2)
# Print the square of result
print(n**2)


####
# Replace ___ with your code below

# Get three sides of a triangle
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

# Compute the semipermeter
s = float(a+b+c)/2

# Compute area and print it
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
''' 