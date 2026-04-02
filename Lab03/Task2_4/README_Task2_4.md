# Task 2.4: Xác minh thủ công X.509 Certificate

## Mục tiêu
Thực hiện quy trình xác minh chứng chỉ số X.509 một cách thủ công. Quy trình này bao gồm:
- Trích xuất khóa công khai (Modulus `n` và Exponent `e`) từ chứng chỉ của nhà phát hành (CA Certificate).
- Trích xuất chữ ký số (Signature) và phần thân chứng chỉ (TBS Certificate) từ chứng chỉ của máy chủ (Server Certificate).
- Sử dụng ngôn ngữ lập trình Python để giải mã chữ ký bằng công thức RSA (`EM' = S^e mod n`) và đối chiếu với giá trị băm SHA-256 tự tính toán từ phần thân chứng chỉ.

## Danh sách tập tin
- `c0.pem`: Chứng chỉ của máy chủ (Server Certificate) tải về thông qua OpenSSL.
- `c1.pem`: Chứng chỉ của nhà phát hành (CA Certificate / Intermediate CA).
- `signature.txt`: Khối dữ liệu dạng Hex chứa chữ ký số RSA, được trích xuất từ `c0.pem`.
- `c0_body.bin`: Dữ liệu nhị phân của phần thân chứng chỉ gốc chưa qua mã hóa (To-Be-Signed Certificate), trích xuất từ `c0.pem`.
- `verify_cert.py`: Script Python thực hiện tính toán băm SHA-256, giải mã RSA và so sánh để xác minh tính hợp lệ của chữ ký.

## Hướng dẫn chạy chương trình

**1. Môi trường yêu cầu:**
- Python 3.x
- Không yêu cầu cài đặt thêm thư viện bên ngoài (sử dụng thư viện `hashlib` tích hợp sẵn).

**2. Cách chạy chương trình:**
Mở Terminal/Command Prompt, di chuyển đến thư mục chứa mã nguồn (đảm bảo tất cả các tệp `.pem`, `.txt`, `.bin` đều nằm cùng cấp với file `.py`) và thực thi lệnh sau:

```bash
python verify_cert.py
```