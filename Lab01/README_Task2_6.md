# Task 2.6 – Phân tích tần suất và tấn công Vigenère Cipher (C++)

## Giới thiệu

Chương trình này cài đặt phương pháp **phân tích mật mã (cryptanalysis)** để phá mã **Vigenère Cipher** bằng ngôn ngữ **C++**.

Chương trình sử dụng các kỹ thuật:

- **Chuẩn hóa văn bản**
- **Index of Coincidence (IC)** để dự đoán độ dài khóa
- **Chi-squared test** để tìm khóa tốt nhất
- **Caesar decryption** cho từng nhóm ký tự

Mục tiêu của chương trình là **tìm khóa và giải mã ciphertext mà không cần biết trước khóa**.

---

## Nguyên lý hoạt động

Việc phá mã Vigenère Cipher thường gồm 3 bước chính:

### 1. Chuẩn hóa văn bản

- Loại bỏ ký tự không phải chữ cái
- Chuyển toàn bộ sang chữ hoa

Ví dụ:

```
Hello World!
→ HELLOWORLD
```

---

### 2. Dự đoán độ dài khóa

Chương trình sử dụng **Index of Coincidence (IC)**.

IC đo mức độ trùng lặp ký tự trong văn bản.

Công thức:

```
IC = Σ f_i (f_i - 1) / (N (N - 1))
```

Trong đó:

- **fᵢ**: số lần xuất hiện của ký tự i
- **N**: tổng số ký tự

Nếu IC gần với **0.067** → văn bản giống tiếng Anh → độ dài khóa có thể đúng.

---

### 3. Tìm khóa bằng Chi-Squared Test

Sau khi biết độ dài khóa:

- Chia ciphertext thành các nhóm ký tự
- Mỗi nhóm tương đương với **Caesar Cipher**

Chương trình thử **26 phép dịch chuyển** và tính:

```
Chi-Squared Score
```

Công thức:

```
Σ (observed - expected)² / expected
```

Khóa có **điểm chi-square nhỏ nhất** được chọn.

---

## Chức năng của chương trình

Chương trình cung cấp các chức năng:

1. **Nhập ciphertext từ bàn phím**

2. **Đọc ciphertext từ file**

3. **Dự đoán độ dài khóa**

4. **Tìm khóa của Vigenère Cipher**

5. **Giải mã văn bản**

6. **Hiển thị bản rõ dự đoán**

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

### Hàm `clean_text()`

Chức năng:

- Chuẩn hóa văn bản đầu vào.

Xử lý:

- Loại bỏ ký tự không phải chữ cái
- Chuyển thành chữ hoa

---

### Hàm `get_index_of_coincidence()`

Chức năng:

- Tính **Index of Coincidence (IC)** của văn bản.

Dùng để:

- Phân tích xem văn bản có giống tiếng Anh hay không.

---

### Hàm `find_key_length()`

Chức năng:

- Dự đoán **độ dài khóa**.

Nguyên lý:

- Chia ciphertext thành nhiều chuỗi con
- Tính IC trung bình
- Chọn độ dài khóa có IC gần **0.067** nhất.

---

### Hàm `chi_squared_score()`

Chức năng:

- Tính **chi-square score** dựa trên tần suất chữ cái tiếng Anh.

Dùng để:

- Xác định phép dịch Caesar tốt nhất.

---

### Hàm `decrypt_caesar()`

Chức năng:

- Giải mã Caesar Cipher với một **shift** xác định.

---

### Hàm `crack_vigenere()`

Chức năng:

- Phá mã Vigenère Cipher.

Các bước:

1. Chuẩn hóa ciphertext  
2. Tìm độ dài khóa  
3. Phân tích từng nhóm ký tự  
4. Tìm shift tốt nhất  
5. Ghép lại thành khóa  
6. Giải mã toàn bộ văn bản

---

## Cách biên dịch và chạy chương trình

### Biên dịch

```
g++ Task2_6.cpp -o Task6.exe
```

---

### Chạy chương trình

Linux / Mac

```
./Task6
```

Windows

```
Task6.exe
```

---

## Ví dụ chạy chương trình

```
=== Vigenere Cipher Breaker ===

Ban muon nhap tu (1) Ban phim hay (2) File? 1

Nhap ciphertext:
RIJVSUYVJN

------------------------------
PHAN TICH HOAN TAT
Do dai khoa du doan: 3
Khoa tim duoc: KEY
------------------------------

Ban ro du doan:
HELLOWORLD
```

---

## Ưu điểm

- Có thể phá mã **Vigenère Cipher tự động**
- Áp dụng các kỹ thuật **cryptanalysis thực tế**
- Hoạt động tốt với ciphertext dài

---

## Hạn chế

- Cần ciphertext đủ dài để phân tích chính xác
- Nếu văn bản quá ngắn → khó xác định đúng khóa
- Giả định văn bản là **tiếng Anh**

---

## Mục đích của bài tập

Bài tập giúp:

- Hiểu cách **phá mã Vigenère Cipher**
- Làm quen với các kỹ thuật **cryptanalysis**
- Áp dụng **Index of Coincidence và Chi-Squared test**
- Thực hành lập trình mật mã bằng **C++**
