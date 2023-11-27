def solve(word):
    vowels = "aeiou"
    max_value = current_value = 0
    
        # Loop through each letter 

    for letter in word:
        # If the letter is a consonant, add its value to the current value
        if letter not in vowels:
            current_value += ord(letter) - ord('a') + 1
          # Update the maximum value and reset current value when a vowel is encountered   
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    # Return the maximum value found
    return max(max_value, current_value)
