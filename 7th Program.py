# :::::::: - - - Count number of vowels in a string 			::::::::

string = input("Enter the String : ")
vowels = 0
for i in string:
    if (
            i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
print("No. of vowels :", vowels)

print()


def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count)


str = input("Enter the String : ")
vowel_count(str)
