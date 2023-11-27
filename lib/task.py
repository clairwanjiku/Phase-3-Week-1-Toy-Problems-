def exactly_two_positive(a, b, c):
    
    

    # Count the number of positive integers
    count_positive = sum(x > 0 for x in [a, b, c])
    
     # Return True if exactly two integers are positive
    return count_positive == 2
