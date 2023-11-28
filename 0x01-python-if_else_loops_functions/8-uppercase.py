def uppercase(input_str):
    for char in input_str:
        uppercase_char = chr(ord(char) - ord('a') + ord('A')) if 'a' <= char <= 'z' else char
        print(uppercase_char, end="")
    print()

# Example usage:
input_string = "Hello, World!"
uppercase(input_string)

