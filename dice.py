'''def dice(n):
    #return ((6-n)+1)
    return (7-n)


n=int(input("Enter the side"))
print(dice(n))'''


def prime_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

start = 1
end = 50
primes = prime_range(start, end)
print(primes)
