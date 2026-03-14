// Task 2.5: Cài đặt chương trình mã hóa và giải mã Vigenère cipher
#include <iostream>
#include <algorithm>
using namespace std;

// Hàm chuẩn hóa văn bản
string prepareText(string text)
{
    string result = "";
    // Loại bỏ khoảng trắng và chuyển thành chữ hoa
    for (char c : text)
    {
        if (isalpha(c))
            result += toupper(c);
    }
    return result;
}

// Hàm tạo key cùng độ dài với plaintext
string generateKey(string text, string key)
{
    // Chuyển key thành chữ hoa
    transform(key.begin(), key.end(), key.begin(), ::toupper);
    // Sinh key lặp lại cho bằng độ dài văn bản
    string newKey = "";
    int keyIndex = 0;
    // Chỉ giữ lại chữ cái trong key
    for (int i = 0; i < text.length(); i++)
    {
        newKey += key[keyIndex];
        keyIndex++;
        // Nếu key đã hết, quay lại từ đầu
        if (keyIndex == key.length())
            keyIndex = 0;
    }
    return newKey;
}

// Hàm mã hóa
string encrypt(string text, string key)
{

    string cipher = "";

    for (int i = 0; i < text.length(); i++)
    {
        // đưa về chỉ số nằm trong bản chữ cái (0-25)
        int p = text[i] - 'A';
        int k = key[i] - 'A';
        // Áp dụng công thức: (P + K) mod 26 sau đó chuyển về ký tự
        char c = (p + k) % 26 + 'A';
        // Thêm ký tự mã hóa vào kết quả
        cipher += c;
    }

    return cipher;
}

// Hàm giải mã
string decrypt(string cipher, string key)
{

    string plain = "";

    for (int i = 0; i < cipher.length(); i++)
    {
        // đưa về chỉ số nằm trong bản chữ cái (0-25)
        int c = cipher[i] - 'A';
        int k = key[i] - 'A';
        // Áp dụng công thức: (C - K + 26) mod 26 sau đó chuyển về ký tự
        char p = (c - k + 26) % 26 + 'A';
        // Thêm ký tự giải mã vào kết quả
        plain += p;
    }
    return plain;
}

// Main
int main()
{

    int choice;
    string text, key;

    cout << "1. Encrypt\n";
    cout << "2. Decrypt\n";
    cout << "Choose: ";
    cin >> choice;
    cin.ignore();

    cout << "Enter key: ";
    getline(cin, key);

    cout << "Enter text: ";
    getline(cin, text);
    // Chuẩn hóa văn bản
    text = prepareText(text);
    // Tạo key lặp lại cho bằng độ dài văn bản
    string newKey = generateKey(text, key);

    cout << "Prepared text: " << text << endl;
    cout << "Generated key: " << newKey << endl;
    // Thực hiện mã hóa hoặc giải mã dựa trên lựa chọn
    if (choice == 1)
    {
        cout << "Ciphertext: " << encrypt(text, newKey) << endl;
    }
    else
    {
        cout << "Plaintext: " << decrypt(text, newKey) << endl;
    }

    return 0;
}