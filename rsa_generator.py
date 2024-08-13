import math, random

def coprimos(a, b):
    if a == 1 or a == 0:
        return False
    else:
        return math.gcd(a, b) == 1

def generate_key(p, q):
    n = p * q
    totiente = (p - 1) * (q - 1)
    e = 0
    for i in range(totiente):
        if coprimos(i, totiente):
            e = i
            break
    mod = False
    d = 1
    while mod == False:
        ed = e * d
        if ed % totiente == 1:
            mod = True
        else:
            d += 1

    return e,n,d

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def miller_rabin(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin(a):
            return False
        
    return True

def encrypt(e, n, plaintext):
    return (plaintext**e) % n
    
def decrypt(d, n, ciphertext):   
    return (ciphertext**d) % n

def generate_prime(bits):
    while True:
        random_number = random.getrandbits(bits)
        if random_number % 2 == 0:
            random_number += 1
        if is_prime(random_number):
            return random_number

def main():
    while True:
        print('[0] Generate a key pair\n[1] Encrypt\n[2] Decrypt\n[3] Quit\n')
        option = int(input('Choose one option: '))
        match option:
            case 3:
                break
            case 0:
                q = generate_prime(11)
                p = generate_prime(11)
                key = generate_key(q, p)
                print('\n\n\n\n\nYour public key: (', key[0],',', key[1], ')' '\nYour private key: (', key[2],',', key[1], ')\n\n')
            case 1:
                public_key = input('Enter your public key ex: 7,5636 : ').split(',')
                message = int(input('\nEnter a short number to encrypt: '))
                ciphertext = encrypt(int(public_key[0]), int(public_key[1]), message)
                print('\nYour ciphertex: ', ciphertext, '\n')
            case 2:
                private_key = input('Enter your private key ex: 34323,5636 : ').split(',')
                ciphertext = int(input('\nEnter your ciphertext: '))
                plaintext = decrypt(int(private_key[0]), int(private_key[1]), ciphertext)
                print('\nYour plaintext is: ', plaintext, '\n')
if __name__ == "__main__":
    
    main()

