def is_prime(n):
    # TODO Implement this function
    if n % 2 == 0:
        return False
    elif n == 2:
        return True
    else :
        return True
    
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i in range(n + 1) if is_prime[i]]

num = int(input("Please enter a number: "))
if is_prime(num):
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")
    print(sieve(num))
    