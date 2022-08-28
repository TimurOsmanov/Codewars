from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    else:
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0:
                return False
        return True
