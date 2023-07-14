#7Write a python script to enter any string, replace vowel with its position number.

def replace_vowels_with_position(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ""

    for i, char in enumerate(string):
        if char.lower() in vowels:
            new_string += str(i)
        else:
            new_string += char

    return new_string

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Call the function to replace vowels with position numbers
result = replace_vowels_with_position(user_input)

# Print the modified string
print("Modified string:", result)
