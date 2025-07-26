# Palindrome check
text = input("Enter your text: ")

#remove space and make lowercase
cleaned_text = text.replace("","").lower()

palindrome = cleaned_text == cleaned_text[::-1]

print("Is palindrome?", palindrome)