# RSA Key Encryption Algorithm

# calculates GCD of a and d
def gcd(a, b): 
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

# calculates modulo inverse of a for mod m 
def modinv(a, m): 
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# calculates all possible co-prime numbers with a
def coprimes(a): 
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x, phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l
 
# encrypts a single block
def encrypt_block(m): 
    c = m ** e % n
    return c

# decrypts a single block
def decrypt_block(c): 
    m = c ** d % n
    return m

# applies encryption
def encrypt_string(s): 
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])

# applies decryption
def decrypt_string(s): 
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])


p = int(input('p : '))
q = int(input('q : '))

n = p * q
print("n = " + str(n) + "\n")

phi = (p - 1) * (q - 1)
print("Phi (n) : " + str(phi) + "\n")


print("Choose `e` :\n")
print(str(coprimes(phi)) + "\n")

e = int(input("Enter e : "))

# calculates the decryption key d
d = modinv(e, phi)
print("\nPublic key e = " + str(e) + ", n = " + str(n))
print("Private key d = " + str(d) + ", n = " + str(n))

s = input("\nMessage : ")

enc = encrypt_string(s)
print("Encrypted Message: ", enc, "\n")

dec = decrypt_string(enc)
print("Decrypted Message: " + dec + "\n")