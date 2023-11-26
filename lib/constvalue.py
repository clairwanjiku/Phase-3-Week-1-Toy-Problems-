def solve(word):
    vowels = "aeiou"
    max_value = current_value = 0

    for letter in word:
        if letter not in vowels:
            current_value += ord(letter) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    return max(max_value, current_value)
