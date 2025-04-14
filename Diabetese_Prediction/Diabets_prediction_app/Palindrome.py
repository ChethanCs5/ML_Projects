def is_palindrome(string):
    # Check if the string is the same when reversed
    return string == string[::-1]

input_string = input('Enter the word: ')
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome!')
else:
    print(f'"{input_string}" is not a palindrome.')