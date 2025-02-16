def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

nums = [1, 4, 2, 3, 5, 6, 22, 42, 42, 10, 15, 17, 23, 24, 29, 31]  #Приймає отакий список чисел
print(filter_primes(nums))
