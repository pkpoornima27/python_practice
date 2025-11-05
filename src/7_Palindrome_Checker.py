##7. Palindrome Checker

###User enters the word and this program checks if it is Palindrome or not

word = input("Enter the word:")
print("User entered:", word)
l = len(word)
reverse = ""
for i in word:
    reverse = i + reverse
print(reverse)

if word == reverse:
    print(word, "is a palindrome")
else:
    print(word, "is not palindrome")

