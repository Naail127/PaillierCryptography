import math
import random
import os

p = int(4541554238500101232552500954782756651386703008262217019716749311659998997105067659483444223523928779)
q = int(9083258364967755778714009204230578095286209015347938511945277809368431387795772440566214471168363613)

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




