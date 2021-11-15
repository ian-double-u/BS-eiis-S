# Libraries
from numpy import lcm
from math import gcd
import collections
import itertools

# Functions
def encoding(x):
    if type(x) == str:
        return [ord(c)+100 for c in x]
    
    if type(x) == list:
        x = "".join(map(str,x))
        return "".join([chr(int(x[y:(y+3)])-100) for y in range(0,len(x),3)])
    
def sieve_of_Eratosthenes(n): 
    """returns all primes under n"""
    A = [True]*n
    for i in range(2,int(n**(0.5))+1): 
        if A[i] == True:
            j = i**2
            while j < n:
                A[j] = False
                j += i                  
    return [i for i in range(len(A)) if A[i] == True][2:]

def phi(n):
    return len([x for x in range(1,n+1) if gcd(n,x) == 1])

def trial_division(n):
    divisors = []
    
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
        
    x = 3
    while x * x <= n:
        if n % x == 0:
            divisors.append(x)
            n //= x
        else:
            x += 2
            
    if n != 1: 
        divisors.append(n)
        
    return divisors

def divisors(n):
    x = trial_division(n)
    y = collections.Counter(x)
    z = [[factor ** i for i in range(count + 1)] for factor, count in y.items()]
    
    return sorted(list(set(list(map(lambda x: x[0]*x[1], list(itertools.product(*z)))))))

def generate_keys(m):
    p, q = sieve_of_Eratosthenes(m)[-1], sieve_of_Eratosthenes(m)[-2]
    
    m = lcm(p-1,q-1)
    e = 2
    while gcd(e,m) != 1:
        e += 1
    
    divs = divisors(phi(m))
    i = 0
    
    while True:
        k = divs[i]
        
        if (e**k) % m == 1:
            d = e**(divs[i]-1) % m
            break
            
        else:
            i += 1
        
    return {"public-key": {"n": p*q, "e": e}, "private-key": {"d": d}}


def encrypt(m, public_key):
    return [(i**public_key["e"]) % public_key["n"] for i in encoding(m)]   


def decrypt(m,keys):
    return encoding([(i**keys["private-key"]["d"]) % keys["public-key"]["n"] for i in m])
