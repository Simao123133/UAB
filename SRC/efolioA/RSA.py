from math import gcd as bltin_gcd
import random

def coprime2(a, b):
    return bltin_gcd(a, b) == 1


def getCoprimes2(num):
    coPrimes2 = []
    for num_i in range(2, num):
        if coprime2(num, num_i):
            coPrimes2.append(num_i)
    return coPrimes2

def getConstants(p, q):
    n = p*q
    phi_n = (p-1)*(q-1)
    coPrimes2 = getCoprimes2(phi_n)
    e = random.choice(coPrimes2)
    e = 7 #this one always works
    d = 2
    while ((phi_n + 1) % (d*e) != 0) and d < phi_n:
        d += 1
    if (phi_n + 1) % (d*e) != 0:
        print("d not found")    
    else:
        print("d is " + str(d))

    return n, d, e


def encryptMessage(message, e, n):
    return ''.join([chr((ord(char) ** e) % n) for char in message])


def decryptMessage(d, n, message):
    decryptedMessage = ""
    for letter in message:
        decryptedMessage += chr((ord(letter) ** d) % n)
    return decryptedMessage


def main():
    p = 17
    q = 11
    originalMessage = "ninguemvaidescobrir"
    print("Original Message ", originalMessage)
    n, d, e = getConstants(p, q)
    encryptedMessage = encryptMessage(originalMessage, e, n)
    print("Encrypted Message ", encryptedMessage)
    message = decryptMessage(d, n, encryptedMessage)
    print("Decrypted Message ", message)



if __name__ == "__main__":
    main()