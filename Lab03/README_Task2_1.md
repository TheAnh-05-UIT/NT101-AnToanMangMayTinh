# Task2.1: MMã hóa khóa công khai RSA

Chương trình Python này được xây dựng để mô phỏng toàn diện nguyên lý hoạt động của hệ mật mã bất đối xứng RSA. Code giải quyết từ các bài toán cơ sở như sinh khóa, mã hóa số nguyên đến các kỹ thuật nâng cao như mã hóa chuỗi văn bản bằng cơ chế **Chia Khối (Block Cipher)**.

## Tính năng nổi bật

- **Tự động sinh khóa lớn:** Áp dụng thuật toán Miller-Rabin để sinh số nguyên tố lớn ngẫu nhiên nếu không cung cấp sẵn $p, q$.
- **Toán học chính xác:** Sử dụng thuật toán Euclid mở rộng để tính nghịch đảo module (tìm khóa riêng $d$).
- **Mã hóa đa dạng:** - Đảm bảo **Tính bảo mật (Confidentiality)**: Mã hóa bằng Public Key, giải mã bằng Private Key.
  - Đảm bảo **Tính xác thực (Authentication)**: Đóng vai trò chữ ký số (Mã hóa bằng Private Key, giải mã bằng Public Key).
- **Cơ chế Block Cipher:** Tự động cắt nhỏ dữ liệu thành các khối vừa với kích thước của module $N$, giúp mã hóa được các chuỗi văn bản dài mà không bị lỗi "Message too large".
- **Hỗ trợ nhiều định dạng:** Có khả năng tự động tiền xử lý và giải mã các bản mã dưới dạng `Base64`, `Hexadecimal (Hex)` và `Binary`.

---

## Yêu cầu hệ thống (Prerequisites)

Chương trình chỉ sử dụng các thư viện tiêu chuẩn (Built-in) của Python, không cần cài đặt thêm bất kỳ thư viện bên ngoài nào qua `pip`.

- **Môi trường:** Python 3.6 trở lên.
- **Thư viện sử dụng:** `math`, `random`, `base64`.

---

## Hướng dẫn cài đặt và chạy trên VS Code

**1. Môi trường yêu cầu:**
- Python 3.x

**2. Cách chạy chương trình:**
```bash
cd Lab03
python Task2_1.py
```

---

## Chức năng theo từng Yêu cầu Bài tập

Chương trình sẽ tự động thực thi và in ra kết quả cho 4 yêu cầu:

1. **Yêu cầu 1:** Xác định Khóa công khai (PU) và Khóa riêng (PR) từ 3 bộ thông số $p, q, e$ cho trước (bao gồm cả định dạng Thập phân và Thập lục phân).
2. **Yêu cầu 2:** Dùng Bộ khóa 1 ($p=11, q=17$) để mã hóa và giải mã số $M=5$ theo 2 mô hình Bảo mật và Xác thực.
3. **Yêu cầu 3:** Dùng kỹ thuật Block Cipher kết hợp Bộ khóa 3 để mã hóa chuỗi văn bản `"The University of Information Technology"` và xuất ra định dạng Base64.
4. **Yêu cầu 4:** Brute-force tự động (dùng 3 bộ khóa PR hiện có) để dò và giải mã 4 chuỗi bản mã phức tạp (Base64, Hex, Binary) về lại bản rõ là văn bản có nghĩa.

---

## Cấu trúc Mã nguồn

- `is_prime()` & `generate_large_prime()`: Kiểm tra và sinh số nguyên tố ngẫu nhiên.
- `mod_inverse()`: Tìm nghịch đảo module để tạo khóa $d$.
- `rsa_keygen()`: Hàm tổng hợp sinh cặp khóa PU và PR.
- `encrypt_number()` & `decrypt_number()`: Mã hóa/giải mã số học cơ bản.
- `rsa_encrypt_string()` & `rsa_decrypt_blocks()`: Cơ chế mã hóa chia khối an toàn cho chuỗi văn bản.
- `main()`: Hàm thực thi trung tâm, in ra kết quả theo định dạng trực quan.

---
## Kết quả chạy chương trình
```
============================================================
Yêu cầu 1: Xác định khóa công khai PU và khóa riêng PR
============================================================

Bộ 1:
 PU = (7, 187)
 PR = (23, 187)

Bộ 2:
 PU = (17, 13588476140342208394395166469647627226674348541791)
 PR = (7993221259024828467291262184080358019185876599873, 13588476140342208394395166469647627226674348541791)

Bộ 3 (Hex -> Dec):
 PU = (886979, 101776877529005912638346811918779931246783058062684819617574643018368103302097)
 PR = (24212225287904763939160097464943268930139828978795606022583874367720623008491, 101776877529005912638346811918779931246783058062684819617574643018368103302097)

============================================================
Yêu cầu 2: Mã hóa/giải mã bản rõ M = 5 (bộ 1)
============================================================
Bảo mật (Confidentiality):
 - Mã hóa (Dùng PU): 146
 - Giải mã (Dùng PR): 5

Xác thực (Authentication):
 - Mã hóa/Ký (Dùng PR): 180
 - Giải mã/Xác minh (Dùng PU): 5

============================================================
Yêu cầu 3: Mã hóa chuỗi
============================================================
Bản rõ: The University of Information Technology
Bản mã dùng Bộ 3 (Base64): R9n3NredoQsUmSGNXJ5GDnzxJccF6mqXvGjYuWJOl8rBOYtJFgefuZ2UiSDeV9Q4sa5Fk2TnWquyMD6d9vS54Q==

============================================================
Yêu cầu 4: Tìm bản mã của các bản rõ
============================================================

--- Giải mã Bản mã 1 (BASE64) ---
Không thể giải mã thành văn bản hợp lệ bằng các khóa hiện tại.

--- Giải mã Bản mã 2 (HEX) ---
Không thể giải mã thành văn bản hợp lệ bằng các khóa hiện tại.

--- Giải mã Bản mã 3 (BASE64) ---
[Thành công] Dùng Key 1 (Block Cipher) - Bản rõ Text: Vietnam National University - Ho Chi Minh City

--- Giải mã Bản mã 4 (BIN) ---
Không thể giải mã thành văn bản hợp lệ bằng các khóa hiện tại.
```