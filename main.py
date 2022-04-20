Str = input()
lens = len(Str)
Del = ""
for i in range(lens - 1, -1, -1):
    Del += Str[i]
print("Result is: ", Del)
if (Del == Str):
    print("Palindrome")
else:
    print("Not palindrome")