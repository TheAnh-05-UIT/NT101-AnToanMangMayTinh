# Task 2.4 – Playfair Cipher (C++)

## Giới thiệu

Chương trình này cài đặt thuật toán **Playfair Cipher** bằng ngôn ngữ **C++**.  
Playfair Cipher là một phương pháp mã hóa cổ điển sử dụng **ma trận 5×5** và thực hiện mã hóa **theo cặp ký tự (digraph)** thay vì từng ký tự riêng lẻ như Caesar Cipher.

Thuật toán này giúp tăng mức độ bảo mật so với các phương pháp thay thế đơn giản.

---

## Nguyên lý hoạt động

Playfair Cipher sử dụng một **ma trận 5×5 chứa các chữ cái từ A–Z (gộp I và J)** được tạo từ một **khóa (key)**.

Ví dụ với khóa:

```
KEYWORD
```

Ma trận tạo ra có thể như sau:

```
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z
```

---

## Quy tắc mã hóa

Văn bản được chia thành **các cặp ký tự**.

Có 3 trường hợp:

### 1. Hai ký tự cùng hàng

Lấy ký tự **bên phải** của mỗi ký tự.

Ví dụ:

```
AB → BC
```

---

### 2. Hai ký tự cùng cột

Lấy ký tự **bên dưới** mỗi ký tự.

Ví dụ:

```
AR → FM
```

---

### 3. Hai ký tự khác hàng và khác cột

Tạo thành **hình chữ nhật**, lấy ký tự ở **góc đối diện cùng hàng**.

Ví dụ:

```
HI → BM
```

---

## Chuẩn hóa văn bản

Trước khi mã hóa, văn bản cần được chuẩn hóa:

- Loại bỏ khoảng trắng
- Chuyển thành chữ hoa
- Thay **J → I**
- Nếu hai chữ giống nhau trong một cặp → chèn **X**
- Nếu độ dài lẻ → thêm **X** vào cuối

Ví dụ:

```
HELLO
→ HELXLO
```

---

## Chức năng của chương trình

Chương trình cung cấp các chức năng:

1. **Encrypt**
   - Mã hóa văn bản bằng Playfair Cipher.

2. **Decrypt**
   - Giải mã văn bản bằng khóa đã cho.

3. **Hiển thị ma trận khóa**
   - In ra bảng Playfair 5×5 để người dùng kiểm tra.

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

### Hàm `generateMatrix()`

Chức năng:

- Tạo **ma trận 5×5** từ khóa.

Xử lý:

- Loại bỏ khoảng trắng
- Chuyển sang chữ hoa
- Thay **J → I**
- Điền các chữ cái còn lại của bảng chữ cái

---

### Hàm `printMatrix()`

Chức năng:

- In ma trận Playfair ra màn hình.

Ví dụ:

```
Playfair Matrix:
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z
```

---

### Hàm `findPosition()`

Chức năng:

- Tìm vị trí của một ký tự trong ma trận.

Trả về:

```
(row, column)
```

---

### Hàm `prepareText()`

Chức năng:

- Chuẩn hóa văn bản trước khi mã hóa.

Bao gồm:

- Loại bỏ khoảng trắng
- Chuyển chữ hoa
- Chèn **X** nếu hai ký tự giống nhau
- Thêm **X** nếu độ dài lẻ

---

### Hàm `encrypt()`

Chức năng:

- Mã hóa văn bản theo **quy tắc Playfair Cipher**.

Xử lý theo 3 trường hợp:

- Cùng hàng
- Cùng cột
- Hình chữ nhật

---

### Hàm `decrypt()`

Chức năng:

- Giải mã văn bản.

Quy tắc ngược lại so với mã hóa:

- Cùng hàng → dịch trái
- Cùng cột → dịch lên
- Hình chữ nhật → giữ nguyên quy tắc hoán đổi cột

---

## Cách biên dịch và chạy chương trình

### Biên dịch

```
g++ Task2_4.cpp -o Task4.exe
```

---

### Chạy chương trình

Linux / Mac

```
./Task4
```

Windows

```
Task4.exe
```

---

## Ví dụ chạy chương trình

```
1. Encrypt
2. Decrypt
Choose: 1

Enter key: KEYWORD

Playfair Matrix:
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z

Enter text: HELLO

Prepared text: HELXLO
Ciphertext: GYIZSC
```

---

## Ưu điểm

- Bảo mật hơn Caesar Cipher
- Mã hóa theo **cặp ký tự**
- Giảm khả năng phân tích tần suất đơn giản

---

## Hạn chế

- Vẫn có thể bị phá bằng **frequency analysis**
- Không phù hợp cho hệ thống bảo mật hiện đại
- Phụ thuộc vào **quản lý khóa**

---

## Mục đích của bài tập

Bài tập giúp:

- Hiểu nguyên lý hoạt động của **Playfair Cipher**
- Làm quen với **mã hóa theo digraph**
- Thực hành lập trình thuật toán mật mã bằng **C++**