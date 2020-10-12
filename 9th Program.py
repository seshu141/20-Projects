# Write a program to swap two numbers

x = input('Enter value of x : ')
y = input('Enter value of y : ')
temp = x
x = y
y = temp
print()
print('After swapping The value of x is : {}'.format(x))
print('After swapping The value of y is : {}'.format(y))
print()


x = input('Enter value of x: ')
y = input('Enter value of y: ')
x, y = y, x
print()
print('After swapping The value of x is : {}'.format(x))
print('After swapping The value of y is : {}'.format(y))