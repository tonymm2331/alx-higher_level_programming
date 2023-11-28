def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if index is out of bounds

    return input_str[:n] + input_str[n + 1:]

# Example usage:
original_str = "Hello, World!"
result_str = remove_char_at(original_str, 7)
print(result_str)

