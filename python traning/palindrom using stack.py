def is_palindrome(s):
    stack = []

    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    # Compare characters from the original string to those popped from the stack
    for char in s:
        if char != stack.pop():
            return False
    return True

# Read input from the user
user_input = input("Enter a string to check if it is a palindrome: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
