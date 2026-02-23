# text_analysis_functions.py

import string


# 1. Count words
def count_words(text):
    return len(text.split())


# Helper function (to match sample output logic)
def get_unique_text(text):
    words = text.lower().split()
    unique_words = list(dict.fromkeys(words))  # remove duplicates
    return " ".join(unique_words)


# 2. Count vowels
def count_vowels(text):
    vowels = "aeiou"
    unique_text = get_unique_text(text)
    count = 0
    for char in unique_text:
        if char in vowels:
            count += 1
    return count


# 3. Count consonants
def count_consonants(text):
    vowels = "aeiou"
    unique_text = get_unique_text(text)
    count = 0
    for char in unique_text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


# 4. Reverse text
def reverse_text(text):
    return text[::-1]


# 5. Check palindrome
def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


# 6. Remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


# 7. Word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip(string.punctuation)
        freq[word] = freq.get(word, 0) + 1
    return freq


# 8. Longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# 9. Analyze text
def analyze_text(text):
    print("=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:", ", ".join(f"{word}: {count}" for word, count in freq.items()))


# Run program
if __name__ == "__main__":
    text = input("Enter text: ")
    analyze_text(text)