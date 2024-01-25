def is_prime(number):

    if number == 1:
        return False
    if number == 2:
        return True
    if number > 1:
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                return False
            else:
                return True
                       
# Test cases
print(is_prime(11))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(2))  # Expected output: True
print(is_prime(1))  # Expected output: False