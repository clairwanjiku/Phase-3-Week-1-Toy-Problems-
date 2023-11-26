def exactly_two_positive(a, b, c):
    count_positive = sum(x > 0 for x in [a, b, c])
    return count_positive == 2
