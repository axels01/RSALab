#Arvid Albinsson, Leo Asa, Furqan Ali Butt, Axel Östergren 10/4-2023

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


#Implements the extended euclidan algorithm with a recursive callback
#ax + by = gcd(a, b)
def extendedEuclid(a, b):
    #When a is 0 it means b must be gcd, thus return.    
    if a == 0:
        return b, 0, 1

    #Runs recursively until a is 0
    else:
        gcd, x, y = extendedEuclid(b % a, a)
        return (gcd, y - (b // a) * x, x)

#Calculates number of positive intagers relatively prime to n and smaller than n
def eulerPhi(n):
    phi = 1
    #Loops each intager i between 1 and n-1, if i is relatively primt to n
    #extendedEuclid will have 1 in the 0'th position of its return value 
    for i in range(1, n-1):
        if (extendedEuclid(i, n)[0] == 1):
            phi += 1
    return phi

def modInv(e, mod):
    gcd, x, y = extendedEuclid(e, mod)
    #If gcd is not equal to one, a mod invers doesn't exist
    if gcd != 1:
        return None
    #If the mod invers exist, calculate it by 
    else:
        return (x % mod + mod) % mod


#Simple UI
def UI():
    print("Welcome to our RSA toolkit!")
    print("Choose a function:")
    print("1 isPrime")
    print("2 extendedEuclid")
    print("3 eulerPhi")
    print("4 modInv")

    choices = ["1","2","3","4"]

    choice = input()

    if choice not in choices:
        return ("Invalid input")

    if (choice == "1"):
        print("Function: isPrime, enter number to check:")
        num = input()
        try: 
            num = int(num)
        except:
            return("Input is not int")
        return "Return: "  + str(isPrime(num))

    elif (choice == "2"):
        print("Function: extendedEuclid, enter two numbers in format \"a,b\" without spaces:")
        nums = input()
        a = nums.split(",")[0]
        b = nums.split(",")[1]
        try:
            a = int(a)
            b = int(b)
        except:
            return("One or more none int")
        return"Return: " + str(extendedEuclid(a,b))

    elif (choice == "3"):
        print("Function: eulerPhi, enter number to check:")
        num = input()
        try:
            num = int(num)
        except:
            return("Input is not int")
        return"Return: " + str(eulerPhi(num))

    elif (choice == "4"):
        print("Function: modInv, enter two numbers in format \"e,mod\" without spaces:","\n")
        nums = input()
        e = nums.split(",")[0]
        try:
            mod = nums.split(",")[1]
        except:
            return("Invalid input, input shall contain one \",\" but no spaces or \"")
        try:
            e = int(e)
            mod = int(mod)
        except:
            return("One or more none int")
        return "Return: " + str(modInv(e,mod))
        

if __name__ == "__main__":
    #while True:   
        #print(UI())
        #input("Press Enter to continue...\n")

        #print("--------------------------------------")
        pass

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
    
    N = 19 x 77 = 1463

    phi = 18 * 76 = 1368

    gcd(5, 1368) = 1

    c = m^e mod N = 15^5 mod 1463 = 78

    cipher = 78

'''
