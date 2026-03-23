from Crypto.Cipher import DES

def to_bits(data):
    return bin(int.from_bytes(data, 'big'))[2:].zfill(64)

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def avalanche_test():
    key = b'24520115' # 8 byte
    p1 = b'STAYHOME'
    p2 = b'STAYHOMA'

    cipher = DES.new(key, DES.MODE_ECB)

    c1 = cipher.encrypt(p1)
    c2 = cipher.encrypt(p2)

    b1 = to_bits(c1)
    b2 = to_bits(c2)

    diff = hamming_distance(b1, b2)
    percent = diff / 64 * 100

    print("Bit khác nhau:", diff)
    print("Tỷ lệ:", percent, "%")

avalanche_test()