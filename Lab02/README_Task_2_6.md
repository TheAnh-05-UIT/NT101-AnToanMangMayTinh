# Task 2.6 - Mersenne Prime - Số nguyên tố lớn

## Giới thiệu

Chương trình này triển khai các thuật toán số học nền tảng, đóng vai trò là "xương sống" cho các hệ thống mật mã bất đối xứng như RSA và Diffie-Hellman. Chương trình tập trung vào việc xử lý số nguyên lớn, kiểm tra tính nguyên tố xác suất và các phép toán modulo hiệu quả cao.

---

## Nguyên lý các thuật toán

### 1. Kiểm tra số nguyên tố Miller-Rabin
Thay vì chia thử (Trial Division) tốn thời gian, Miller-Rabin sử dụng tính chất của số nguyên tố trong lý thuyết số để xác định một số là "số nguyên tố có khả năng" (probably prime).
- **Độ phức tạp**: $O(k \log^3 n)$.
- **Độ tin cậy**: Với $k$ vòng thử, xác suất một hợp số vượt qua bài kiểm tra là ít hơn $(1/4)^k$.

### 2. Lũy thừa Modulo (Modular Exponentiation)
Tính $a^x \pmod p$ bằng thuật toán **Square-and-Multiply**. Thuật toán này giúp tính toán các số mũ khổng lồ mà không cần tính ra giá trị thực của $a^x$ (vốn có thể lên đến hàng triệu chữ số), giúp tránh tràn bộ nhớ và tăng tốc độ xử lý.

### 3. Thuật toán Euclid (Greatest Common Divisor)
Tìm ước chung lớn nhất (GCD) của hai số. Trong mật mã học, GCD được dùng để kiểm tra tính nguyên tố cùng nhau ($\text{gcd}(a, b) = 1$), điều kiện cần thiết để tìm nghịch đảo modulo.

---

## Chức năng của chương trình

Chương trình cung cấp một bộ công cụ số học bao gồm:

1. **Sinh số nguyên tố ngẫu nhiên**
   - Hỗ trợ các độ dài bit phổ biến: 8-bit, 16-bit, và 64-bit (số nguyên lớn).
2. **Tìm số nguyên tố lớn**
   - Tìm 10 số nguyên tố nằm ngay dưới số Mersenne thứ 10 ($2^{89} - 1$).
3. **Kiểm tra số nguyên tố thủ công**
   - Giao diện nhập liệu để kiểm tra một số bất kỳ từ người dùng.
4. **Tính toán GCD và Modulo nhanh**
   - Thực hiện các phép tính cơ bản với hiệu suất tối ưu.

---

## Cấu trúc mã nguồn

### Hàm `miller_rabin(n, k=5)`
- Thực hiện kiểm tra tính nguyên tố dựa trên phân tích $n-1 = 2^s \cdot d$.

### Hàm `generate_prime(bits)`
- Sử dụng hàm `getrandbits` để tạo số ngẫu nhiên, sau đó dùng bitwise để đảm bảo số đó là số lẻ và có độ dài bit chính xác trước khi đưa vào kiểm tra Miller-Rabin.

### Hàm `mod_exp(a, x, p)`
- Triển khai vòng lặp tối ưu để tính lũy thừa theo cơ số 2 của số mũ $x$.

---

## Cách chạy chương trình

### Yêu cầu
- Máy tính đã cài đặt **Python 3.x**.

### Thực thi
Mở terminal tại thư mục chứa file và chạy:

```bash
python Task2_6.py
```

## Kết quả chạy chương trình 

Phần giải thích kết quả có bên tỏng báo cáo

```
1. Sinh số nguyên tố
Prime 8-bit : 151
Prime 16-bit: 34183
Prime 64-bit: 11425338897908186219

2. 10 số nguyên tố < 2^89 - 1
1: 618970019642690137449562091
2: 618970019642690137449562081
3: 618970019642690137449562063
4: 618970019642690137449562043
5: 618970019642690137449562013
6: 618970019642690137449562009
7: 618970019642690137449561847
8: 618970019642690137449561791
9: 618970019642690137449561671
10: 618970019642690137449561509

3. Kiểm tra số nguyên tố
Nhập số cần kiểm tra: 97
=> Là số nguyên tố

4. GCD
Nhập a: 14
Nhập b: 28
GCD = 14

5. Lũy thừa modulo
Nhập a: 7
Nhập x: 40
Nhập p: 19
7^40 mod 19 = 7
```