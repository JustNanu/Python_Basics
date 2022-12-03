#program to find a palindrome
word = input("Enter any Word: ")

reverse = word[::-1]

if( word == reverse ):
    print("Entered word is a Palindrome")

else:
    print("Entered word is Not a Palindrome")