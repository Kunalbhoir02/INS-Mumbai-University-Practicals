import math

p= int(input("Enter value for p : "))
q = int(input("Enter value for q : "))
n= p * q
print("\n n = ",n)
phi = (p-1)*(q-1)
print("\n Euler's quotient function phi = ",phi)
print("This is list of Co-Primes Arrays for given Prime Numbers : \n")

def gcd(a,b):
    while b != 0 :
        c = a % b
        a = b
        b = c
    return a

def modinv(a,m):
    for x in range(1,m):
        if(a * x) % m ==1:
            return x
    return None

def coprimes(a):
    l = []
    for x in range(2,a):
        if gcd(a,x) == 1 and modinv(x,phi) !=None:
            l.append(x)
    for x in l :
        if x == modinv(x,phi):
            l.remove(x)
    return l
print(str(coprimes(phi)) + "\n")

e = int(input("Choose an value for 'e' or 'co-prime' from a above Co-Primes Array : \t"))
d = modinv(e,phi)

def encrypt(me):
    en = math.pow(me,e)
    ci = en % n
    return ci

def decrypt(me):
    en = math.pow(me,d)
    de = en % n
    return de

message = int(input("Enter the message to be encrypted : "))
print("Original Message is : ",message)
c = encrypt(message)
print("Encrypted Message is : ",c)
d = decrypt(c)
print("Decrypted Message is : ",d)
