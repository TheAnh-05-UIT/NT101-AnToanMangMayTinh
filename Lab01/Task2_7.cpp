// Task 2.7: Cài đặt chương trình mã hóa và giải mã Hill cipher
#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// Tính phép chia lấy dư mod 26
int mod26(int x)
{
    x %= 26;
    if (x <= 0)
        x += 26;
    return x;
}

// Chuẩn hóa dữ liệu đầu vào trước khi mã hóa/giải mã
string normalize(string text)
{
    string result = "";

    for (char c : text)
    {
        if (isalpha(c))
            result += toupper(c);
    }

    return result;
}

// Hàm mã hóa
string encrypt(string text, int key[2][2])
{
    string cipher = "";

    if (text.length() % 2 != 0)
        text += 'X';

    for (int i = 0; i < text.length(); i += 2)
    {
        // Chuyển ký tự thành số (A=1, B=2, ..., Z=26)
        int p1 = text[i] - 'A' + 1;
        int p2 = text[i + 1] - 'A' + 1;
        // Áp dụng ma trận key để mã hóa
        int c1 = mod26(key[0][0] * p1 + key[0][1] * p2);
        int c2 = mod26(key[1][0] * p1 + key[1][1] * p2);
        // Chuyển số thành ký tự
        cipher += char(c1 - 1 + 'A');
        cipher += char(c2 - 1 + 'A');
    }

    return cipher;
}

// Tính nghịch đảo modulo 26
int modInverse(int a)
{
    for (int i = 1; i <= 26; i++)
    {
        // Nếu (a * i) mod 26 == 1 thì i là nghịch đảo của a
        if ((a * i) % 26 == 1)
            return i;
    }
    return -1;
}

// Tính ma trận nghịch đảo của key
void inverseKey(int key[2][2], int inv[2][2])
{
    // Tính định thức của ma trận key
    int det = key[0][0] * key[1][1] - key[0][1] * key[1][0];
    det = mod26(det);
    // Tính nghịch đảo của định thức
    int detInv = modInverse(det);
    // Tính ma trận nghịch đảo
    inv[0][0] = mod26(key[1][1] * detInv);
    inv[0][1] = mod26(-key[0][1] * detInv);
    inv[1][0] = mod26(-key[1][0] * detInv);
    inv[1][1] = mod26(key[0][0] * detInv);
}

//  Hàm giải mã
string decrypt(string cipher, int key[2][2])
{
    int inv[2][2];
    inverseKey(key, inv);

    string plain = "";

    for (int i = 0; i < cipher.length(); i += 2)
    {
        // Chuyển ký tự thành số (A=1, B=2, ..., Z=26)
        int c1 = cipher[i] - 'A' + 1;
        int c2 = cipher[i + 1] - 'A' + 1;
        // Áp dụng ma trận nghịch đảo để giải mã
        int p1 = mod26(inv[0][0] * c1 + inv[0][1] * c2);
        int p2 = mod26(inv[1][0] * c1 + inv[1][1] * c2);
        // Chuyển số thành ký tự
        plain += char(p1 - 1 + 'A');
        plain += char(p2 - 1 + 'A');
    }

    return plain;
}

int main()
{
    // Ma trận khóa 2x2
    int key[2][2];
    // Nhập ma trận khóa từ người dùng
    cout << "Enter key matrix (2x2):\n";
    cin >> key[0][0] >> key[0][1];
    cin >> key[1][0] >> key[1][1];

    cin.ignore();

    string text;
    // Nhập văn bản cần mã hóa
    cout << "Enter plaintext: ";
    getline(cin, text);
    //  Chuẩn hóa văn bản đầu vào
    text = normalize(text);
    //  Lựa chọn mã hóa hoặc giải mã
    int choice;
    cout << "Choose an option:\n1. Encrypt\n2. Decrypt\nEnter your choice: ";
    cin >> choice;

    if (choice == 1)
    {
        // Mã hóa văn bản và hiển thị kết quả
        string cipher = encrypt(text, key);
        cout << "Ciphertext: " << cipher << endl;
    }
    else
    {
        // Giải mã văn bản và hiển thị kết quả
        string plain = decrypt(text, key);
        cout << "Decrypted: " << plain << endl;
    }
    return 0;
}