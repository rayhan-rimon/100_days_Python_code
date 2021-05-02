def is_prime_number(num):
    if num == 1:
        return False # 1 is not prime number

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


#=========== Test Function =======
for num in range(1, 100):
    print(num, is_prime_number(num))