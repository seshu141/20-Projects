# ::::----  Find number of even numbers and odd numbers in a list		::::::::
A=list()
n=int(input("Enter the Range : "))

def split(A):
    evenlist = []
    oddlist = []
    for i in A:
        if (i % 2 == 0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even lists:", evenlist)
    print("Odd lists:", oddlist)
for i in range(int(n)):
    k = int(input(""))
    A.append(k)
split(A)