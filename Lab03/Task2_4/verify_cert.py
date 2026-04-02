import hashlib

n_hex = "A567708DD0568164151761CDB906D4AD19908C2650379816639254DBD9CC840593ECD3EC081BA0605143487D2BC748969EB42DDA9DC8273B57A19FABF0D60ED40E30CA6F9BB1D1D6A49D323E584E356F4558687117FC3ED85D82A02FB2516CB01A5DB859CE3565C88BA1AF1037FFE39C5DC2491734FF8C2B8B8DF0BC712C930C1D05C4BAC7CDAAC95E7CD1C901F79C03F6FC0A5DF4DA7BE6DB764270EBF44D22DA00776FD6C95F17FDDA752EA5570CF6EA5CB6E073A568CFA174E275827E109FC1F5A2EB01E938B10A44CCD3C289F54935820A34B31CE988C2474E820E0A36F0474F8AF1290475DACDE19A5CFF5E9D9895BA9A43D04AA21705010430D332B38F" # Giá trị Modulus lấy ở Bước 2

n = int(n_hex, 16)
e = 65537  # Giá trị Exponent lấy ở Bước 2

# ĐỌC CHỮ KÝ TỪ SIGNATURE.TXT VÀ LÀM SẠCH
try:
    with open("signature.txt", "r") as f:
        raw_signature = f.read()
        
    # Tự động dọn dẹp các dấu :, khoảng trắng, và dấu xuống dòng nếu có
    clean_signature = raw_signature.replace(":", "").replace(" ", "").replace("\n", "")
    
    # Chuyển chuỗi hex sạch thành số nguyên
    S = int(clean_signature, 16)
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file signature.txt. Hãy kiểm tra lại tên file.")
    exit()

# Giải mã chữ ký bằng Khóa công khai CA: EM' = S^e mod n
EM_prime = pow(S, e, n)

# Chuyển kết quả về hex, lấp đầy chữ số 0 ở đầu cho đủ chiều dài modulus
EM_hex = hex(EM_prime)[2:].zfill(len(n_hex))
print("[*] Chuỗi giải mã từ chữ ký (EM_hex):")
print(EM_hex[-64:])

# BĂM LẠI PHẦN THÂN CHỨNG CHỈ (TBS)
# Đọc file c0_body.bin đã tạo
try:
    with open("c0_body.bin", "rb") as f:
        tbs_data = f.read()
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file c0_body.bin. Hãy kiểm tra lại.")
    exit()
    
# Tính băm SHA-256
calculated_hash = hashlib.sha256(tbs_data).hexdigest()
print("\n[*] Mã băm SHA-256 tự tính từ c0_body.bin:")
print(calculated_hash)

# SO SÁNH EM_hex VỚI MÃ BĂM TỰ TÍNH
# Kiểm tra xem chuỗi EM_hex có chứa mã băm tự tính ở phần đuôi không
if EM_hex.endswith(calculated_hash):
    print("valid!")
else:
    print("invalid!")
