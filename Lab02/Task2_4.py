from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Số byte trong một block của AES
BLOCK = 16

# Hàm đảo bit tại vị trí byte_index và bit_index
def flip_bit(data, byte_index, bit_index):
    corrupted = bytearray(data)
    corrupted[byte_index] ^= (1 << bit_index)
    return bytes(corrupted)

# Hàm đếm số block bị hỏng
def count_corrupted_blocks(p1, p2):
    blocks = len(p1) // BLOCK
    count = 0
    for i in range(blocks):
        if p1[i*BLOCK:(i+1)*BLOCK] != p2[i*BLOCK:(i+1)*BLOCK]:
            count += 1
    return count

# Test từng chế độ mã hóa AES-128
def test_mode(mode):
    print("\nMode:", mode)

    # 1. tạo dữ liệu 1000 byte
    data = b'A' * 1000
    data = pad(data, BLOCK)

    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    # 2. mã hóa
    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == "CBC":
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif mode == "CFB":
        cipher = AES.new(key, AES.MODE_CFB, iv)
    elif mode == "OFB":
        cipher = AES.new(key, AES.MODE_OFB, iv)

    ciphertext = cipher.encrypt(data)

    # 3. đảo 1 bit tại byte thứ 26
    corrupted = flip_bit(ciphertext, 25, 0)

    # 4. giải mã
    if mode == "ECB":
        cipher2 = AES.new(key, AES.MODE_ECB)
    elif mode == "CBC":
        cipher2 = AES.new(key, AES.MODE_CBC, iv)
    elif mode == "CFB":
        cipher2 = AES.new(key, AES.MODE_CFB, iv)
    elif mode == "OFB":
        cipher2 = AES.new(key, AES.MODE_OFB, iv)

    decrypted = cipher2.decrypt(corrupted)

    # đếm block bị lỗi
    corrupted_blocks = count_corrupted_blocks(data, decrypted)

    print("Số block bị lỗi:", corrupted_blocks)

for m in ["ECB", "CBC", "CFB", "OFB"]:
    test_mode(m)