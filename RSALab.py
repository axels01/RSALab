#Implements a function for testing whether a number is prime or not.
def isPrime(a):
    if a < 2:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    
    else:
        for i in range(3, a, 2):
            if a % i == 0:
                return False
            if i > a // 2:
                break
        return True


if __name__ == "__main__":
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 7907
    ]
    not_primes = [
        4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 7908
    ]

    for i in primes:
        print(i, isPrime(i))
    
    for i in not_primes:
        if isPrime(i):
            print(i, isPrime(i))

    

'''
Question 1: What information in RSA an attacker may have access to? And
what makes it practically impossible for the attacker to break the scheme and
retrieve the clear-text message?

    The attacker can get access to the public key, the encrypted message
    and.

    The amount of time it would take to calculate the private key using the
    public key is too long to be pratctical.



Question 2: How many values from 1 to n should be tested before deciding
if n is prime or not? Why?

    You only need to test for all numbers less than, and including, half
    of the number tested. For any test where x is larger than the half of y,
    the result of x/y will be less than 1, thus not a prime number.


Question 3: Alice wants to send m=15 to Bob. She gets Bobs public key
pk=(19,77) by visiting a public repository. If she decides to use RSA for
encryption, what would be the resulting cipher text? (Show your calculation)





'''