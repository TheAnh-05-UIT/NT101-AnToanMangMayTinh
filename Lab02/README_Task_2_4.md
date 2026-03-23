# Task 2.5 – Phân tích sự lan truyền lỗi trong các chế độ mã hóa AES

## Giới thiệu

Chương trình này thực hiện mô phỏng việc **lỗi bit trên kênh truyền** ảnh hưởng như thế nào đến quá trình giải mã của thuật toán AES-128. Bằng cách làm hỏng (đảo bit) 1 bit duy nhất trong bản mã (Ciphertext), chúng ta sẽ quan sát số lượng khối (blocks) dữ liệu bị lỗi sau khi giải mã ở các chế độ: **ECB, CBC, CFB, và OFB**.

---

## Nguyên lý lan truyền lỗi (Error Propagation)

Trong mật mã học, mỗi chế độ vận hành khối có cách liên kết các khối dữ liệu khác nhau, dẫn đến khả năng chịu lỗi khác nhau:

- **ECB (Electronic Codebook)**: Các khối độc lập, lỗi ở khối nào chỉ ảnh hưởng đến khối đó.
- **CBC (Cipher Block Chaining)**: Lỗi ở một khối bản mã sẽ làm hỏng hoàn toàn khối hiện tại và thay đổi 1 bit tương ứng ở khối kế tiếp sau khi giải mã.
- **CFB (Cipher Feedback)**: Lỗi ở bản mã làm hỏng khối hiện tại và ảnh hưởng đến các khối tiếp theo cho đến khi lỗi được đẩy ra khỏi thanh ghi dịch.
- **OFB (Output Feedback)**: Luồng khóa được tạo độc lập với bản mã, do đó lỗi 1 bit ở bản mã chỉ ảnh hưởng đúng 1 bit tại vị trí đó ở bản rõ.

---

## Chức năng của chương trình

Chương trình thực hiện quy trình thử nghiệm tự động cho từng chế độ:

1. **Khởi tạo dữ liệu**: Tạo một chuỗi dữ liệu lớn (1000 byte) và thực hiện **Padding** để đảm bảo kích thước phù hợp với block size của AES (16 byte).
2. **Mã hóa**: Sử dụng khóa ngẫu nhiên và vector khởi tạo (IV) ngẫu nhiên để mã hóa dữ liệu.
3. **Gây lỗi (Bit Flipping)**: Đảo ngược 1 bit tại vị trí byte thứ 26 trong bản mã.
4. **Giải mã**: Giải mã bản mã đã bị lỗi bằng cùng một khóa và IV.
5. **Thống kê**: Đếm số lượng khối (16-byte blocks) bị sai khác so với bản rõ ban đầu.

---

## Cấu trúc chương trình

### Các hàm hỗ trợ:
- `flip_bit(data, byte_index, bit_index)`: Sử dụng toán tử `XOR` để đảo ngược giá trị của một bit cụ thể trong mảng byte.
- `count_corrupted_blocks(p1, p2)`: Chia dữ liệu thành từng cụm 16 byte và so sánh để đếm số khối không giống nhau.

### Hàm chính `test_mode(mode)`:
- Thực hiện đầy đủ chu kỳ mã hóa -> gây lỗi -> giải mã -> báo cáo cho từng chế độ được truyền vào.

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
python Task2_4.py
```

## Kết quả khi chạy chương trình

Phần giải thích kết quả nằm bên trong báo cáo

```
Mode: ECB
Số block bị lỗi: 1

Mode: CBC
Số block bị lỗi: 2

Mode: CFB
Số block bị lỗi: 2

Mode: OFB
Số block bị lỗi: 1
```