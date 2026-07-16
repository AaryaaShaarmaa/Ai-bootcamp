# Check Palindrome Number or Word

text = input("Enter a number or word: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")