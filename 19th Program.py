# 19th program Find second biggest number of a list
print(" enter the range of no. and stop")
def Range(list1):
    largest = list1[0]
    largest2 = None
    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
    print("Largest element is:", largest)
    print("Second Largest element is:", largest2)
# Driver Code
# try block to handle the exception
try:
    my_list = []
    while True:
        my_list.append(int(input()))
    # if the input is not-integer, just print the list
except:
    print(" The Range of no u enter are : ", my_list)
Range(my_list)