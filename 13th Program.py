#Python Program to print Numbers Divisible by Another Number
print()
a = int(input("enter the numer : "))
b = int(input("enter the numer : "))
def multiple(a, b):
    return True if a % b == 0 else False

print(multiple(a, b))
print(multiple(b, a))

print()


class Divisibility():
    def __init__(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

    def find_divisibility(self):
        number_list = [self.num1, self.num2,]
        check_num = int(input("Enter a number to check the divisibility test: "))
        result = list(filter(lambda x: (x % check_num == 0), number_list))
        print("Numbers divisible by", check_num, "are", result)
def main():
    print("Enter the two numbers: ")
    num1 = input()
    num2 = input()
    obj_Divisibility = Divisibility(num1, num2,)
    obj_Divisibility.find_divisibility()
if __name__ == "__main__":
    main()
    print()
