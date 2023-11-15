def is_prime(number):
    is_prime = True

    if number < 2 or number > 1000:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

    return is_prime

# Example usage:
number_to_check = 5
result = is_prime(number_to_check)
print(f"{number_to_check} is prime: {result}")