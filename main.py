import math
import random
import os

p = int(os.getenv("p1"))
q = int(os.getenv("p2"))

n = p * q
phi = (p - 1) * (q - 1)
g = 1 + n
lamda = phi * 1
mu = pow(phi, -1, n)

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def get_coprime(y):
    r = random.randint(0, n)
    while math.gcd(r, y) != 1:
        r = random.randint(0, n)
    return r

def lx(x):
    y = (x-1)//n
    assert y % 1 == 0
    return y

def encrypt(m):
    r = get_coprime(n)
    c = pow(g, m, n * n) * pow(r, n, n * n) % (n * n)
    return c

def decrypt(c):
    p = ((lx(pow(c, lamda, n*n)) *mu) % n)
    return p

def encrypt_message(message):
    message = encrypt(message)
    return(message)


print(124556)
print(encrypt_message(124556))
print(decrypt(encrypt_message(124556)))
