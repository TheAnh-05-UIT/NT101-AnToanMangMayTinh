import math
import random
import base64

# PHẦN 1: CÁC HÀM TOÁN HỌC CƠ SỞ

def is_prime(n, k=5):
    """
    Kiểm tra tính nguyên tố của một số n bằng thuật toán xác suất Miller-Rabin.
    - k: Số lần thử nghiệm (càng cao càng chính xác).
    """
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_large_prime(bits=512):
    """Sinh ngẫu nhiên một số nguyên tố lớn với số bit chỉ định."""
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1 # Đảm bảo số sinh ra là số lẻ và đủ số bit
        if is_prime(p): return p

def mod_inverse(e, phi):
    """
    Tính nghịch đảo modulo d của e theo modulo phi (Tìm khóa riêng d).
    Sử dụng hàm pow() của Python hoặc thuật toán Euclid mở rộng.
    """
    try:
        return pow(e, -1, phi)
    except ValueError:
        def egcd(a, b):
            if a == 0: return (b, 0, 1)
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
        g, x, y = egcd(e, phi)
        if g != 1: raise Exception("Không có nghịch đảo modular")
        return x % phi

# PHẦN 2: HÀM SINH KHÓA RSA

def rsa_keygen(p=None, q=None, e=None, bits=1024):
    """
    Sinh cặp khóa RSA (Public Key, Private Key).
    Nếu không cung cấp p và q, hệ thống sẽ tự động sinh ngẫu nhiên số nguyên tố lớn.
    """
    if p is None or q is None:
        p = generate_large_prime(bits)
        q = generate_large_prime(bits)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if e is None:
        e = 65537 # Giá trị e tiêu chuẩn (Fermat thứ 4), tối ưu cho tốc độ và bảo mật
        if math.gcd(e, phi) != 1:
            e = 3
            while math.gcd(e, phi) != 1: e += 2
            
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# PHẦN 3: CÁC HÀM MÃ HÓA & GIẢI MÃ

def encrypt_number(m, pub_key):
    """Mã hóa một số nguyên m: C = M^e mod n"""
    e, n = pub_key
    return pow(m, e, n)

def decrypt_number(c, priv_key):
    """Giải mã một số nguyên c: M = C^d mod n"""
    d, n = priv_key
    return pow(c, d, n)

def rsa_encrypt_string(message, public_key):
    """
    Mã hóa chuỗi ký tự dài bằng kỹ thuật Chia Khối (Block Cipher).
    Tránh lỗi "Message too large" khi bản rõ M lớn hơn module N.
    """
    e, n = public_key
    n_byte_len = (n.bit_length() + 7) // 8
    block_size = max(1, n_byte_len - 1) # Khối dữ liệu phải nhỏ hơn module n
    
    msg_bytes = message.encode('utf-8')
    cipher_bytes = b''
    
    for i in range(0, len(msg_bytes), block_size):
        chunk = msg_bytes[i:i+block_size]
        m_int = int.from_bytes(chunk, byteorder='big')
        c_int = pow(m_int, e, n)
        # Đồng bộ kích thước khối mã hóa bằng đúng n_byte_len
        cipher_bytes += c_int.to_bytes(n_byte_len, byteorder='big')
        
    return base64.b64encode(cipher_bytes).decode('utf-8')

def rsa_decrypt_blocks(cipher_bytes, private_key):
    """Giải mã chuỗi dữ liệu đã được chia khối."""
    d, n = private_key
    n_byte_len = (n.bit_length() + 7) // 8
    
    if len(cipher_bytes) % n_byte_len != 0: return None, None
        
    decrypted_bytes = b''
    for i in range(0, len(cipher_bytes), n_byte_len):
        chunk = cipher_bytes[i:i+n_byte_len]
        c_int = int.from_bytes(chunk, byteorder='big')
        if c_int >= n: return None, None
        
        m_int = pow(c_int, d, n)
        chunk_length = (m_int.bit_length() + 7) // 8
        decrypted_bytes += m_int.to_bytes(chunk_length, byteorder='big')
        
    try:
        return decrypted_bytes.decode('utf-8'), decrypted_bytes.hex()
    except:
        return None, decrypted_bytes.hex()

def rsa_decrypt_single_int(c_int, private_key):
    """Giải mã dữ liệu nếu bản mã là một số nguyên duy nhất (không chia khối)."""
    d, n = private_key
    if c_int >= n: return None, None
    m_int = pow(c_int, d, n)
    chunk_length = (m_int.bit_length() + 7) // 8
    m_bytes = m_int.to_bytes(chunk_length, byteorder='big')
    try:
        return m_bytes.decode('utf-8'), m_bytes.hex()
    except:
        return None, m_bytes.hex()

# PHẦN 4: THỰC THI YÊU CẦU ĐỀ BÀI=

def main():
    print("="*60)
    print("Yêu cầu 1: Xác định khóa công khai PU và khóa riêng PR")
    print("="*60)
    
    # Minh họa tính năng: Nếu không có p, q -> Tự tạo khóa cực lớn
    PU_rand, PR_rand = rsa_keygen(bits=1024)
    
    # 1.1 Khởi tạo Bộ 1
    p1, q1, e1 = 11, 17, 7
    PU1, PR1 = rsa_keygen(p1, q1, e1)
    print(f"\nBộ 1:\n PU = {PU1}\n PR = {PR1}")
    
    # 1.2 Khởi tạo Bộ 2
    p2, q2, e2 = 20079993872842322116151219, 676717145751736242170789, 17
    PU2, PR2 = rsa_keygen(p2, q2, e2)
    print(f"\nBộ 2:\n PU = {PU2}\n PR = {PR2}")
    
    # 1.3 Khởi tạo Bộ 3 (Chuyển Hex sang Decimal)
    p3 = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
    q3 = int("E85CED54AF57E53E092113E62F436F4F", 16)
    e3 = int("0D88C3", 16)
    PU3, PR3 = rsa_keygen(p3, q3, e3)
    print(f"\nBộ 3 (Hex -> Dec):\n PU = {PU3}\n PR = {PR3}")
    
    keys = [("Key 1", PR1), ("Key 2", PR2), ("Key 3", PR3)]

    print("\n" + "="*60)
    print("Yêu cầu 2: Mã hóa/giải mã bản rõ M = 5 (bộ 1)")
    print("="*60)
    M = 5
    # Trường hợp 1: Mã hóa cho tính bảo mật
    C_conf = encrypt_number(M, PU1)
    M_conf = decrypt_number(C_conf, PR1)
    print(f"Bảo mật (Confidentiality):\n - Mã hóa (Dùng PU): {C_conf}\n - Giải mã (Dùng PR): {M_conf}")
    
    # Trường hợp 2: Mã hóa cho tính xác thực (Chữ ký số)
    C_auth = encrypt_number(M, PR1)
    M_auth = decrypt_number(C_auth, PU1)
    print(f"\nXác thực (Authentication):\n - Mã hóa/Ký (Dùng PR): {C_auth}\n - Giải mã/Xác minh (Dùng PU): {M_auth}")

    print("\n" + "="*60)
    print("Yêu cầu 3: Mã hóa chuỗi")
    print("="*60)
    message = "The University of Information Technology"
    print(f"Bản rõ: {message}")
    # Dùng bộ 3 để mã hóa vì N đủ lớn, kết quả xuất ra Base64
    c_base64 = rsa_encrypt_string(message, PU3)
    print(f"Bản mã dùng Bộ 3 (Base64): {c_base64}")

    print("\n" + "="*60)
    print("Yêu cầu 4: Tìm bản mã của các bản rõ")
    print("="*60)
    
    ciphertexts = [
        {"type": "base64", "data": "raUcesUlOkx/8ZhgodMoo0Uu18sC20yXlQFevSu7W/FDxIy0YRHMyXcHdD9PBvIT2aUft5fCQEGomiVVPv4I"},
        {"type": "hex", "data": "C87F570FC4F699CEC24020C6F54221ABAB2CE0C3"},
        {"type": "base64", "data": "Z2BUSkJcg0w4XEpgm0JcMExEQmBlVH6dYEpNTHpMHptMQ7NgTHlgQrNMQ2BKTQ=="},
        {"type": "bin", "data": "001010000001010011111111101101110010111011001010111011000110011110111111001111110110100011001111001100001001010001010100111101010100110011101110111011110101101100000100"}
    ]
    
    for i, item in enumerate(ciphertexts):
        print(f"\n--- Giải mã Bản mã {i+1} ({item['type'].upper()}) ---")
        
        # Tiền xử lý dữ liệu đầu vào tùy theo định dạng
        if item["type"] == "base64":
            data = item["data"].replace(' ', '+')
            data += "=" * ((4 - len(data) % 4) % 4)
            c_bytes = base64.b64decode(data)
            c_int = int.from_bytes(c_bytes, byteorder='big')
        elif item["type"] == "hex":
            c_int = int(item["data"], 16)
            c_bytes = bytes.fromhex(item["data"])
        elif item["type"] == "bin":
            c_int = int(item["data"], 2)
            byte_len = (len(item["data"]) + 7) // 8
            c_bytes = c_int.to_bytes(byte_len, byteorder='big')
            
        found = False
        for key_name, PR in keys:
            # Phương pháp 1: Giải mã nguyên khối (Single Int)
            m_text, m_hex = rsa_decrypt_single_int(c_int, PR)
            # Phương pháp 2: Giải mã theo cơ chế chia khối (Block Cipher)
            m_text_block, m_hex_block = rsa_decrypt_blocks(c_bytes, PR)
            
            if m_text and m_text.isprintable():
                print(f"[Thành công] Dùng {key_name} (Single Int) - Bản rõ Text: {m_text}")
                found = True
            elif m_text_block and m_text_block.isprintable():
                print(f"[Thành công] Dùng {key_name} (Block Cipher) - Bản rõ Text: {m_text_block}")
                found = True
                
        if not found:
            print("Không thể giải mã thành văn bản hợp lệ bằng các khóa hiện tại.")

if __name__ == "__main__":
    main()