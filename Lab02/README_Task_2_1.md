# Task 2.1 - Cấu trúc Feistel và Sự lan truyền thay đổi

## Giới thiệu

Chương trình này mô phỏng cấu trúc của **Mạng Feistel (Feistel Network)** bằng ngôn ngữ **Python**.  
Mục tiêu chính của bài tập là thực hiện mã hóa khối cơ bản và quan sát **hiệu ứng lan truyền (avalanche effect)** – một tính chất quan trọng trong mật mã học, nơi một sự thay đổi nhỏ ở đầu vào tạo ra sự thay đổi lớn ở đầu ra.

---

## Nguyên lý hoạt động

Mạng Feistel hoạt động bằng cách chia khối dữ liệu thành hai nửa $L$ (Trái) và $R$ (Phải). Qua mỗi vòng, các nửa được biến đổi và hoán đổi vị trí cho nhau.



Công thức tổng quát cho mỗi vòng:

$$L_{i+1} = R_i$$
$$R_{i+1} = L_i \oplus F(R_i, K_i)$$

Trong đó:
- **$F$**: Hàm vòng (Round function) thực hiện biến đổi phi tuyến.
- **$\oplus$**: Phép toán XOR bitwise.
- **$K_i$**: Khóa con (subkey) cho vòng thứ $i$.

---

## Chức năng của chương trình

Chương trình thực hiện các bước xử lý sau:

1. **Khởi tạo dữ liệu**
   - Chia thông điệp 8-bit thành hai phần 4-bit ($L$ và $R$).
2. **Tạo khóa con**
   - Từ một khóa chính, sinh ra 4 khóa con khác nhau cho 4 vòng mã hóa.
3. **Mã hóa 4 vòng**
   - Thực hiện biến đổi Feistel liên tiếp qua 4 giai đoạn.
4. **Theo dõi Avalanche**
   - In ra trạng thái bit của từng vòng để so sánh sự khác biệt khi thay đổi dữ liệu đầu vào.

---

## Cấu trúc chương trình

Chương trình bao gồm các hàm cốt lõi:

### Hàm `F(right, subkey)`
- **Chức năng**: Hàm biến đổi chính của mỗi vòng.
- **Xử lý**: Thực hiện `(right XOR subkey)` và sử dụng phép toán `AND 0x0F` để đảm bảo kết quả luôn nằm trong phạm vi 4 bit (nibble).

---

### Hàm `feistel_round()`
- **Chức năng**: Thực hiện một vòng lặp Feistel hoàn chỉnh.
- **Xử lý**: Tính toán giá trị $R$ mới thông qua hàm $F$ và thực hiện việc gán lại các giá trị $L, R$ cho vòng kế tiếp.

---

### Hàm `track_avalanche()`
- **Chức năng**: Điều phối quá trình mã hóa và hiển thị log chi tiết.
- **Xử lý**:
    - Tách byte đầu vào thành 2 nibble (4-bit).
    - Thực hiện vòng lặp mã hóa qua 4 vòng.
    - Xuất kết quả dưới dạng nhị phân (`04b`) để dễ dàng quan sát sự thay đổi từng bit.

---

## Cách chạy chương trình

### Yêu cầu
- Máy tính đã cài đặt **Python 3.x**.

### Thực thi
Sử dụng terminal hoặc Command Prompt:

```bash
python Task2_1.py
```

## Kết quả khi chạy chương trình

Phần giải thích kết quả nằm bên trong báo cáo

```
--- Mã hóa M1 (0xAB) ---
Khởi tạo: L=1010, R=1011
Vòng 1: L=1011, R=0011
Vòng 2: L=0011, R=1001
Vòng 3: L=1001, R=1001
Vòng 4: L=1001, R=0100

--- Mã hóa M2 (0xAC) ---
Khởi tạo: L=1010, R=1100
Vòng 1: L=1100, R=0100
Vòng 2: L=0100, R=1001
Vòng 3: L=1001, R=1110
Vòng 4: L=1110, R=0011
```