

def display_prime(number):

    if number == 2:
        return "It is a prime number"
    if number == 3:
        return "It is a prime number"
    if number % 2 == 0:
        return "It is not a prime number"
    if number % 3 == 0:
        return "It is not a prime number"

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return "It is not a prime number"

        i += w
        w = 6 - w

    return "It is a prime number"