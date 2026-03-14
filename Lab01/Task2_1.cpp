/*Task 2.1: Cài đặt chương trình mã hóa và giải mã Caesar cipher, đồng thời thực hiện tấn công brute-force để tìm khóa.*/
#include <iostream>
#include <string>
using namespace std;

// Hàm mã hóa văn bản sử dụng Caesar cipher
string encrypt(string text, int key)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        char c = text[i];
        if (isupper(c))
            result += char((c - 'A' + key) % 26 + 'A');
        else if (islower(c))
            result += char((c - 'a' + key) % 26 + 'a');
        else
            result += c;
    }
    return result;
}

// Hàm giải mã văn bản sử dụng Caesar cipher
string decrypt(string text, int key)
{
    return encrypt(text, 26 - key);
}

// Hàm thực hiện tấn công brute-force trên cipher
void bruteForce(string cipher)
{
    cout << "\nAll possible decryptions:\n";
    for (int key = 0; key < 26; key++)
    {
        cout << "Key " << key << ":\n";
        cout << decrypt(cipher, key) << endl
             << endl;
    }
}

// Hàm main
int main()
{
    int choice, key;
    string text;
    do
    {
        cout << "\n===== CAESAR CIPHER PROGRAM =====\n";
        cout << "1. Encrypt\n";
        cout << "2. Decrypt\n";
        cout << "3. Brute-force attack\n";
        cout << "0. Exit\n";
        cout << "Choose an option: ";
        cin >> choice;
        cin.ignore();
        switch (choice)
        {
        case 1:
            cout << "Enter plaintext: ";
            getline(cin, text);
            cout << "Enter key (0-25): ";
            cin >> key;
            cout << "Ciphertext: " << encrypt(text, key) << endl;
            break;
        case 2:
            cout << "Enter ciphertext: ";
            getline(cin, text);
            cout << "Enter key (0-25): ";
            cin >> key;
            cout << "Plaintext: " << decrypt(text, key) << endl;
            break;
        case 3:
            cout << "Enter ciphertext: ";
            getline(cin, text);
            bruteForce(text);
            break;
        }
    } while (choice != 0);
    return 0;
}