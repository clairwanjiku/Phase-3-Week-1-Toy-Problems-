## Python Code Challenges
Overview
This repository contains Python solutions to three coding challenges aimed at handling time conversion, determining positive integers, and evaluating consonant substrings.

## Challenge 1: Converting 12-hour time to 24-hour time
Problem Statement
The task involves converting time from the 12-hour clock format (e.g., "8:30 am" or "8:30 pm") to the 24-hour clock format (e.g., "0830" or "2030").

Approach and Solution
The solution involves implementing a function convert_to_24_hour(hour, minute, period) that accepts three parameters: hour (ranging from 1 to 12), minute (ranging from 0 to 59), and period ("am" or "pm"). The function returns a four-digit string representing the time in the 24-hour format.

The logic uses conditional statements to check whether the time is in the "am" or "pm" period and adjusts the hour accordingly to convert it to the 24-hour format.


## Challenge 2: Two numbers are positive
Problem Statement
The objective is to determine whether exactly two out of three given integers are positive.

Approach and Solution
The solution involves implementing a function exactly_two_positive(a, b, c) that takes three integer arguments: a, b, and c. The function returns True if exactly two out of the three integers are positive; otherwise, it returns False. The solution uses the sum() function to count the number of positive integers in the given set of numbers.

## Challenge 3: Consonant value
Problem Statement
The challenge is to find the highest value of consonant substrings in a given lowercase string.

Approach and Solution
The solution involves implementing a function solve(word) that accepts a lowercase string containing only alphabetic characters and no spaces. The function calculates the highest value of consonant substrings, excluding vowels ("aeiou"), using ASCII values. It iterates through the characters, accumulates the value of consonant substrings, and keeps track of the maximum value found.

## Author
Clair Karanja

## License
This project is licensed under the MIT License.