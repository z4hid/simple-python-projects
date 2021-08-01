def reverse(string):
    """Returns the reversed string"""
    reversed = ""
    n = len(string) - 1
    for _ in string:
        reversed += string[n]
        n -= 1
    return reversed

response = input("Enter a String: ")
print(reverse(response))