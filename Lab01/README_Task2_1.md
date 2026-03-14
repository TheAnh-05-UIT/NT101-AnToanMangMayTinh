# Task 2.1 – Caesar Cipher (C++)

## Giới thiệu

Chương trình này cài đặt thuật toán **Caesar Cipher** bằng ngôn ngữ **C++**.  
Ngoài chức năng **mã hóa và giải mã**, chương trình còn thực hiện **tấn công brute-force** để thử tất cả các khóa có thể và tìm ra bản rõ.

Caesar Cipher là một trong những phương pháp mã hóa cổ điển đơn giản nhất, trong đó mỗi chữ cái trong bản rõ được dịch chuyển một số vị trí nhất định trong bảng chữ cái.

---

## Nguyên lý hoạt động

Trong Caesar Cipher, mỗi chữ cái được dịch chuyển theo một **khóa (key)**.

Ví dụ với khóa **key = 3**

```
Plaintext  : HELLO
Ciphertext : KHOOR
```

Công thức mã hóa:

```
C = (P + key) mod 26
```

Công thức giải mã:

```
P = (C - key) mod 26
```

Trong đó:

- P: ký tự bản rõ
- C: ký tự bản mã
- key: số vị trí dịch chuyển

---

## Chức năng của chương trình

Chương trình cung cấp menu với các chức năng:

1. **Encrypt**
   - Mã hóa văn bản bằng Caesar Cipher.

2. **Decrypt**
   - Giải mã văn bản khi biết khóa.

3. **Brute-force attack**
   - Thử tất cả các khóa từ **0 → 25** để tìm bản rõ.

4. **Exit**
   - Thoát chương trình.

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

### Hàm `encrypt()`

Chức năng:

- Mã hóa văn bản bằng Caesar Cipher.

Xử lý:

- Nếu là chữ hoa → dịch chuyển trong bảng chữ cái `A-Z`
- Nếu là chữ thường → dịch chuyển trong bảng chữ cái `a-z`
- Các ký tự khác giữ nguyên.

---

### Hàm `decrypt()`

Chức năng:

- Giải mã văn bản.

Nguyên lý:

- Giải mã bằng cách gọi lại hàm `encrypt()` với khóa:

```
26 - key
```

---

### Hàm `bruteForce()`

Chức năng:

- Thử tất cả các khóa từ **0 đến 25**.
- In ra tất cả các khả năng giải mã.

Ví dụ:

```
Ciphertext: KHOOR

Key 0 : KHOOR
Key 1 : JGNNQ
Key 2 : IFMMP
Key 3 : HELLO
```

---

## Cách biên dịch và chạy chương trình

### Biên dịch

Sử dụng trình biên dịch **g++**

```
g++ Task2_1.cpp -o Task1.exe
```

---

### Chạy chương trình

Linux / Mac

```
./Task1
```

Windows

```
Task1.exe
```

---

## Ví dụ chạy chương trình

```
===== CAESAR CIPHER PROGRAM =====
1. Encrypt
2. Decrypt
3. Brute-force attack
0. Exit
Choose an option: 1

Enter plaintext: HELLO WORLD
Enter key (0-25): 3

Ciphertext: KHOOR ZRUOG
```

---

## Ưu điểm

- Dễ cài đặt
- Dễ hiểu
- Phù hợp để học các khái niệm cơ bản của mật mã học

---

## Hạn chế

- Độ bảo mật rất thấp
- Có thể bị phá dễ dàng bằng **brute-force**
- Không được sử dụng trong các hệ thống bảo mật hiện đại

---

## Mục đích của bài tập

Bài tập giúp:

- Hiểu nguyên lý hoạt động của **Caesar Cipher**
- Thực hành lập trình thuật toán mật mã bằng **C++**
- Hiểu cách hoạt động của **brute-force attack**