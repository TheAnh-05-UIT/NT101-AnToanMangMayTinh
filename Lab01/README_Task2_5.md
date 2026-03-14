# Task 2.5 – Vigenère Cipher (C++)

## Giới thiệu

Chương trình này cài đặt thuật toán **Vigenère Cipher** bằng ngôn ngữ **C++**.  
Vigenère Cipher là một phương pháp mã hóa cổ điển thuộc nhóm **polyalphabetic substitution cipher**, trong đó mỗi ký tự của bản rõ được mã hóa bằng một **khóa gồm nhiều chữ cái**.

Thuật toán này an toàn hơn Caesar Cipher vì sử dụng **nhiều phép dịch chuyển khác nhau** thay vì chỉ một khóa cố định.

---

## Nguyên lý hoạt động

Vigenère Cipher sử dụng một **khóa (key)** là một chuỗi ký tự.

Khóa sẽ được **lặp lại** để có độ dài bằng với plaintext.

Ví dụ:

```
Plaintext : HELLOWORLD
Key       : KEY
Generated : KEYKEYKEYK
```

---

## Công thức mã hóa

Mỗi ký tự được chuyển về vị trí trong bảng chữ cái:

```
A = 0
B = 1
...
Z = 25
```

Công thức mã hóa:

```
C = (P + K) mod 26
```

Công thức giải mã:

```
P = (C - K + 26) mod 26
```

Trong đó:

- **P** : ký tự bản rõ (Plaintext)
- **C** : ký tự bản mã (Ciphertext)
- **K** : ký tự khóa (Key)

---

## Ví dụ

```
Plaintext : HELLO
Key       : KEYKE
```

Mã hóa:

```
H + K = R
E + E = I
L + Y = J
L + K = V
O + E = S
```

Kết quả:

```
Ciphertext: RIJVS
```

---

## Chức năng của chương trình

Chương trình cung cấp các chức năng:

1. **Encrypt**
   - Mã hóa văn bản bằng Vigenère Cipher.

2. **Decrypt**
   - Giải mã văn bản khi biết khóa.

3. **Chuẩn hóa văn bản**
   - Loại bỏ ký tự không phải chữ cái.
   - Chuyển tất cả về chữ hoa.

4. **Sinh khóa tự động**
   - Lặp lại key cho đến khi bằng độ dài plaintext.

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

### Hàm `prepareText()`

Chức năng:

- Chuẩn hóa văn bản đầu vào.

Xử lý:

- Loại bỏ khoảng trắng và ký tự đặc biệt
- Chỉ giữ lại **chữ cái**
- Chuyển toàn bộ thành **chữ hoa**

Ví dụ:

```
Hello World!
→ HELLOWORLD
```

---

### Hàm `generateKey()`

Chức năng:

- Tạo **key có độ dài bằng plaintext**.

Nguyên lý:

- Lặp lại khóa ban đầu cho đến khi đạt độ dài của văn bản.

Ví dụ:

```
Key       : KEY
Plaintext : HELLOWORLD

Generated : KEYKEYKEYK
```

---

### Hàm `encrypt()`

Chức năng:

- Mã hóa văn bản bằng công thức Vigenère Cipher.

Xử lý:

```
C = (P + K) mod 26
```

Trong đó:

- P là ký tự plaintext
- K là ký tự key

---

### Hàm `decrypt()`

Chức năng:

- Giải mã ciphertext.

Công thức:

```
P = (C - K + 26) mod 26
```

---

## Cách biên dịch và chạy chương trình

### Biên dịch

```
g++ Task2_5.cpp -o Task5.exe
```

---

### Chạy chương trình

Linux / Mac

```
./Task5
```

Windows

```
Task5.exe
```

---

## Ví dụ chạy chương trình

```
1. Encrypt
2. Decrypt
Choose: 1

Enter key: KEY
Enter text: HELLO WORLD

Prepared text: HELLOWORLD
Generated key: KEYKEYKEYK

Ciphertext: RIJVSUYVJN
```

---

## Ưu điểm

- An toàn hơn Caesar Cipher
- Khó bị phá bằng **frequency analysis đơn giản**
- Sử dụng nhiều khóa dịch chuyển khác nhau

---

## Hạn chế

- Nếu khóa ngắn và lặp lại nhiều → có thể bị phá bằng **Kasiski attack**
- Không còn được sử dụng trong các hệ thống mật mã hiện đại

---

## Mục đích của bài tập

Bài tập giúp:

- Hiểu nguyên lý của **Vigenère Cipher**
- Làm quen với **polyalphabetic substitution**
- Thực hành lập trình thuật toán mật mã bằng **C++**