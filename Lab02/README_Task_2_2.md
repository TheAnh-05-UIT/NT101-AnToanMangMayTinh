# Task 2.3 – Mode of Operation - Chế độ hoạt động

## Giới thiệu

Chương trình này sử dụng thư viện **PyCryptodome** để thực hiện thuật toán mã hóa hiện đại **AES (Advanced Encryption Standard)**. 
Trọng tâm của bài tập là phân biệt sự khác nhau giữa hai chế độ vận hành khối (Block Cipher Modes): **ECB (Electronic Codebook)** và **CBC (Cipher Block Chaining)** khi xử lý dữ liệu có tính lặp lại.

---

## Nguyên lý hoạt động

### 1. Chế độ ECB (Electronic Codebook)
Đây là chế độ đơn giản nhất. Mỗi khối bản rõ được mã hóa độc lập với cùng một khóa.
- **Đặc điểm**: Nếu hai khối bản rõ giống nhau, bản mã tạo ra sẽ giống hệt nhau.
- **Công thức**: $C_i = E_k(P_i)$

### 2. Chế độ CBC (Cipher Block Chaining)
Mỗi khối bản rõ trước khi mã hóa sẽ được XOR với khối bản mã trước đó. Khối đầu tiên được XOR với một vectơ khởi tạo (**IV - Initialization Vector**).
- **Đặc điểm**: Cùng một khối bản rõ nhưng sẽ cho ra các bản mã khác nhau, giúp che dấu cấu trúc dữ liệu.
- **Công thức**: $C_i = E_k(P_i \oplus C_{i-1})$

---

## Cấu trúc chương trình

Chương trình thực hiện mã hóa một chuỗi văn bản có tính lặp lại cao:
`"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_"` (gồm các cụm "UIT_LAB" lặp lại).

### Các thành phần chính:
- **Key (16 bytes)**: `b'1234567890123456'` (Tương ứng với AES-128).
- **Plaintext**: Bản rõ có độ dài 32 bytes (vừa đủ 2 khối AES).
- **IV (16 bytes)**: Vectơ khởi tạo dùng riêng cho chế độ CBC để đảm bảo tính ngẫu nhiên.

---

## Kết quả và Phân tích

Khi chạy chương trình, ta thu được kết quả (dạng Hex):

Phần giải thích kết quả nằm bên trong báo cáo

```
ECB: 02b0647de210da452e3bdcadc415814e02b0647de210da452e3bdcadc415814e
CBC: 47747530a46ebd156c1da8763c54be1b46807a7ec513e5e69d9256881a0f0c09
```

### Đối với ECB:
Sẽ thấy bản mã có **quy luật lặp lại**. 16 byte đầu và 16 byte sau của chuỗi Hex sẽ giống hệt nhau vì bản rõ đầu vào là hai khối giống nhau.
> **Nguy cơ**: Kẻ tấn công có thể nhận diện được cấu trúc của dữ liệu dù không biết khóa.

### Đối với CBC:
Mặc dù bản rõ lặp lại, nhưng 16 byte đầu và 16 byte sau của bản mã sẽ **hoàn toàn khác nhau**.
> **Ưu điểm**: Bảo mật cao hơn, chống lại các cuộc tấn công dựa trên việc phân tích tần suất hoặc cấu trúc dữ liệu.

---

## Cách cài đặt và chạy

### Yêu cầu
- Máy tính đã cài đặt **Python 3.x**.

### Cài đặt thư viện
Chương trình yêu cầu thư viện `pycryptodome`:
```bash
pip install pycryptodome
```

### Thực thi
Sử dụng terminal hoặc Command Prompt:

```bash
python Task2_2.py
```