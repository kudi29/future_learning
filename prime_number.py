def get_primes(start, end):

    prime_numbers = []

    if start <= 1:

        start = 2

    prime = [True] * (end + 1)

    for p in range(start, end + 1):

        if (prime[p]):

            prime_numbers.append(p)

            for i in range(p, end + 1, p):

                prime[i] = False

    return prime_numbers


print(get_primes(1, 100))
