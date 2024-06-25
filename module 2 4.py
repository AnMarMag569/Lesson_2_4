numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers_1 = [2 ,3 , 5, 7, 11, 13]
primes = []
not_primes = []
for i in numbers:
    for j in numbers_1:
            is_prime=bool(i == j)
            if is_prime == True:
                primes.append(i)
not_primes = list(set(numbers) - set(primes))
not_primes.remove(1)

print(primes)
print(not_primes)