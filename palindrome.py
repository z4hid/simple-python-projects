response = input("Enter a String to check if it is a palindrome: ")

var = response[::1]

if response == var:
	print(f"{response} is a palindrome")
else:
	print(f"{response} is not a palindrome")