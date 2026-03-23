# Task 2.4 – DES Avalanche Effect Analysis (Python)

## Giới thiệu

Chương trình này thực hiện kiểm tra **Hiệu ứng lan truyền (Avalanche Effect)** trên thuật toán mã hóa tiêu chuẩn dữ liệu **DES (Data Encryption Standard)**. 

Mục tiêu là đo lường sự thay đổi ở đầu ra (Ciphertext) khi chỉ thay đổi một lượng nhỏ dữ liệu ở đầu vào (Plaintext). Một thuật toán mã hóa tốt thường có tỷ lệ thay đổi xấp xỉ **50%** số bit khi chỉ thay đổi 1 bit đầu vào.

---

## Nguyên lý hoạt động

### 1. Thuật toán DES
DES là một thuật toán mã hóa khối (block cipher) sử dụng kích thước khối **64-bit** và khóa **56-bit** (được biểu diễn bằng 8 byte). Nó dựa trên cấu trúc mạng Feistel phức tạp với 16 vòng biến đổi.

### 2. Khoảng cách Hamming (Hamming Distance)
Để đo lường hiệu ứng lan truyền, chương trình sử dụng khoảng cách Hamming:
- Đếm số vị trí mà tại đó các bit tương ứng của hai chuỗi khác nhau.
- Công thức tỷ lệ:
$$\text{Avalanche \%} = \frac{\text{Số bit khác nhau}}{\text{Tổng số bit (64)}} \times 100\%$$

---

## Chức năng của chương trình

Chương trình thực hiện các bước sau:
1. **Chuẩn bị dữ liệu**: 
   - Sử dụng cùng một khóa 8-byte: `24520115`.
   - Hai bản rõ gần giống nhau: `STAYHOME` và `STAYHOMA` (chỉ khác nhau ở ký tự cuối).
2. **Mã hóa**: Sử dụng chế độ **DES ECB** để mã hóa cả hai bản rõ.
3. **Chuyển đổi Bit**: Chuyển kết quả bản mã từ dạng byte sang chuỗi nhị phân 64-bit.
4. **Tính toán**: So sánh từng bit giữa hai bản mã để tìm khoảng cách Hamming và tính tỷ lệ phần trăm thay đổi.

---

## Cấu trúc chương trình

Các hàm chính trong mã nguồn:

### Hàm `to_bits(data)`
- **Chức năng**: Chuyển đổi dữ liệu byte thành chuỗi nhị phân.
- **Xử lý**: Sử dụng `zfill(64)` để đảm bảo chuỗi luôn đủ 64 bit ngay cả khi có các số 0 ở đầu.

### Hàm `hamming_distance(a, b)`
- **Chức năng**: So sánh hai chuỗi bit.
- **Xử lý**: Duyệt qua từng cặp ký tự `(x, y)` và đếm các vị trí không trùng khớp.

### Hàm `avalanche_test()`
- **Chức năng**: Hàm thực thi chính.
- **Xử lý**: Khởi tạo DES, thực hiện mã hóa và in kết quả thống kê ra màn hình.

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
python Task2_3.py
```

## Kết quả khi chạy chương trình
Có thể thay đổi key và plaintext trong code và chạy lại chương trình

Phần giải thích kết quả nằm bên trong báo cáo

```
Bit khác nhau: 35
Tỷ lệ: 54.6875 %
```