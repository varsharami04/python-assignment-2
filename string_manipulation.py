# string_manipulator.py

# Taking input from user
sentence = input("Enter a sentence: ")

# Original
print(f"Original: {sentence}")

# Total characters (with spaces)
print(f"Characters (with spaces): {len(sentence)}")

# Total characters (without spaces)
no_spaces = sentence.replace(" ", "")
print(f"Characters (without spaces): {len(no_spaces)}")

# Total words
words = sentence.split()
print(f"Words: {len(words)}")

# Uppercase
print(f"UPPERCASE: {sentence.upper()}")

# Lowercase
print(f"lowercase: {sentence.lower()}")

# Title Case
print(f"Title Case: {sentence.title()}")

# First word
if len(words) > 0:
    print(f"First word: {words[0]}")
else:
    print("First word: ")

# Last word
if len(words) > 0:
    print(f"Last word: {words[-1]}")
else:
    print("Last word: ")

# Reversed sentence
print(f"Reversed: {sentence[::-1]}")