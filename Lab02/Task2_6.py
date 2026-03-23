import random

# 1. Miller-Rabin (kiểm tra nguyên tố)
def miller_rabin(n, k=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # n-1 = 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


# 2. Sinh số nguyên tố ngẫu nhiên
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # đảm bảo đủ bit và là số lẻ
        if miller_rabin(num):
            return num

# 3. Tìm 10 số nguyên tố nhỏ hơn Mersenne thứ 10
def find_primes_below_mersenne(count=10):
    mersenne_10 = 2**89 - 1
    primes = []
    num = mersenne_10 - 1

    while len(primes) < count:
        if miller_rabin(num):
            primes.append(num)
        num -= 1

    return primes


# 4. GCD (Euclid)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 5. Lũy thừa modulo
def mod_exp(a, x, p):
    result = 1
    a = a % p

    while x > 0:
        if x % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        x //= 2

    return result


# MAIN
if __name__ == "__main__":
    print("1. Sinh số nguyên tố")
    prime8 = generate_prime(8)
    prime16 = generate_prime(16)
    prime64 = generate_prime(64)
    
    print("Prime 8-bit :", prime8)
    print("Prime 16-bit:", prime16)
    print("Prime 64-bit:", prime64)
    
    print("\n2. 10 số nguyên tố < 2^89 - 1")
    primes = find_primes_below_mersenne()
    for i, p in enumerate(primes, 1):
        print(f"{i}: {p}")

    print("\n3. Kiểm tra số nguyên tố")
    test_num = int(input("Nhập số cần kiểm tra: "))
    if miller_rabin(test_num):
        print("=> Là số nguyên tố")
    else:
        print("=> Không phải số nguyên tố")

    print("\n4. GCD")
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("GCD =", gcd(a, b))

    print("\n5. Lũy thừa modulo")
    a = int(input("Nhập a: "))
    x = int(input("Nhập x: "))
    p = int(input("Nhập p: "))
    print(f"{a}^{x} mod {p} =", mod_exp(a, x, p))