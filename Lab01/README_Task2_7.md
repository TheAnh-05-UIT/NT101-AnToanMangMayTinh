# Task 2.7 – Hill Cipher (C++)

## Giới thiệu

Chương trình này cài đặt thuật toán **Hill Cipher** bằng ngôn ngữ **C++**.

Hill Cipher là một thuật toán mã hóa cổ điển thuộc nhóm **mã hóa thay thế theo khối (block cipher)**, sử dụng **đại số tuyến tính và phép nhân ma trận** để mã hóa văn bản.

Trong bài này sử dụng **ma trận khóa 2×2**, nghĩa là văn bản sẽ được mã hóa theo từng **cặp ký tự**.

---

## Nguyên lý hoạt động

Hill Cipher hoạt động dựa trên **phép nhân ma trận modulo 26**.

Mỗi ký tự được chuyển thành số:

```
A = 1
B = 2
...
Z = 26
```

Ví dụ:

```
HELLO → HE LL OX
```

Nếu ma trận khóa:

```
| a  b |
| c  d |
```

và vector plaintext:

```
| p1 |
| p2 |
```

thì ciphertext được tính bằng:

```
| c1 |   | a  b | | p1 |
| c2 | = | c  d | | p2 | mod 26
```

---

## Điều kiện của khóa

Ma trận khóa phải **khả nghịch modulo 26**.

Điều này nghĩa là:

```
gcd(det(key), 26) = 1
```

Trong đó:

```
det(key) = ad - bc
```

Nếu định thức không có **nghịch đảo modulo 26** thì không thể giải mã.

---

## Ví dụ

Key matrix:

```
3 3
2 5
```

Plaintext:

```
HELP
```

Ciphertext:

```
HIAT
```

---

## Chức năng của chương trình

Chương trình cung cấp các chức năng:

1. **Nhập ma trận khóa 2×2**

2. **Chuẩn hóa văn bản**
   - Loại bỏ ký tự không phải chữ cái
   - Chuyển thành chữ hoa

3. **Encrypt**
   - Mã hóa văn bản bằng Hill Cipher

4. **Decrypt**
   - Giải mã văn bản bằng **ma trận nghịch đảo của khóa**

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

### Hàm `mod26()`

Chức năng:

- Thực hiện phép **modulo 26** để đảm bảo kết quả nằm trong bảng chữ cái.

---

### Hàm `normalize()`

Chức năng:

- Chuẩn hóa văn bản đầu vào.

Xử lý:

- Loại bỏ ký tự không phải chữ cái
- Chuyển thành chữ hoa

Ví dụ:

```
Hello World!
→ HELLOWORLD
```

---

### Hàm `encrypt()`

Chức năng:

- Mã hóa văn bản bằng **Hill Cipher**.

Xử lý:

1. Chia plaintext thành các cặp ký tự  
2. Chuyển ký tự thành số  
3. Nhân với ma trận khóa  
4. Lấy **mod 26**  
5. Chuyển lại thành ký tự

Nếu độ dài văn bản lẻ → thêm **X** vào cuối.

---

### Hàm `modInverse()`

Chức năng:

- Tìm **nghịch đảo modulo 26** của một số.

Điều này cần thiết để tính **ma trận nghịch đảo của key**.

---

### Hàm `inverseKey()`

Chức năng:

- Tính **ma trận nghịch đảo của key**.

Các bước:

1. Tính **định thức của ma trận**
2. Tìm **nghịch đảo modulo của định thức**
3. Tính **ma trận nghịch đảo**

---

### Hàm `decrypt()`

Chức năng:

- Giải mã ciphertext.

Nguyên lý:

- Sử dụng **ma trận nghịch đảo của key** để nhân với ciphertext.

---

## Cách biên dịch và chạy chương trình

### Biên dịch

```
g++ Task2_7.cpp -o Task7
```

---

### Chạy chương trình

Linux / Mac

```
./Task7
```

Windows

```
Task7.exe
```

---

## Ví dụ chạy chương trình

```
Enter key matrix (2x2):
3 3
2 5

Enter plaintext: HELLO

Choose an option:
1. Encrypt
2. Decrypt
Enter your choice: 1

Ciphertext: HIATWS
```

---

## Ưu điểm

- Mạnh hơn các cipher đơn giản như Caesar
- Sử dụng **toán học (ma trận)** trong mật mã
- Mã hóa theo **khối ký tự**

---

## Hạn chế

- Nếu biết đủ plaintext → có thể phá bằng **linear algebra**
- Phải chọn **ma trận khóa khả nghịch**
- Không được sử dụng trong hệ thống mật mã hiện đại

---

## Mục đích của bài tập

Bài tập giúp:

- Hiểu cách hoạt động của **Hill Cipher**
- Áp dụng **đại số tuyến tính trong mật mã**
- Thực hành lập trình thuật toán mật mã bằng **C++**