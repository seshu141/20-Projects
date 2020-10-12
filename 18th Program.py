#Sort list items without using sort() or sorted() functions

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

new_list = []
while NumList:
    min = NumList[0]
    for x in NumList:
        if x < min:
            min = x
    new_list.append(min)
    NumList.remove(min)

print("Element After Sorting List in Ascending Order is : ", new_list)

# ********* second pro ************** #
print()
NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)