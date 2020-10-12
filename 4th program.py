
#:::::::: - - -  Python Program to Display the multiplication Table - - - ::::::::

# Multiplication table in Python
num1 = int(input("Display multiplication table of :  "))
num2 = int(input("Display multiplication table of :  "))
for i in range(num2+1):
   print(num1, 'x', i, '=', num1*i)
