a = str(input("Enter your string: "))
print(a)
b = len(a)
is_palindrome = True

for i in range(b):
    if a[i] != a[b - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
