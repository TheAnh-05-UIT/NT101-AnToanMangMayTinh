// Task 2.4: Mã hóa và giải mã Playfair Cipher
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string key, text;
char matrix5[5][5];

// Hàm tạo ma trận 5x5 từ khóa
void generateMatrix(string key)
{
    bool used[26] = {false};
    // Loại bỏ khoảng trắng và chuyển thành chữ hoa
    key.erase(remove_if(key.begin(), key.end(), ::isspace), key.end());
    transform(key.begin(), key.end(), key.begin(), ::toupper);
    // Điền ký tự vào ma trận
    int row = 0, col = 0;
    for (char c : key)
    {
        // Thay thế 'J' bằng 'I'
        if (c == 'J')
            c = 'I';
        // Nếu ký tự chưa được sử dụng, thêm vào ma trận
        if (!used[c - 'A'])
        {
            matrix5[row][col] = c;
            used[c - 'A'] = true;
            col++;
            if (col == 5)
            {
                col = 0;
                row++;
            }
        }
    }
    // Điền các ký tự còn lại trong bảng chữ cái vào ma trận
    for (char c = 'A'; c <= 'Z'; c++)
    {
        if (c == 'J')
            continue;

        if (!used[c - 'A'])
        {
            matrix5[row][col] = c;
            used[c - 'A'] = true;
            col++;

            if (col == 5)
            {
                col = 0;
                row++;
            }
        }
    }
}

// Hàm in ma trận 5x5
void printMatrix()
{
    cout << "\nPlayfair Matrix:\n";
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
            cout << matrix5[i][j] << " ";
        cout << endl;
    }
}

// Hàm tìm vị trí của ký tự trong ma trận
pair<int, int> findPosition(char c)
{
    if (c == 'J')
        c = 'I';

    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            if (matrix5[i][j] == c)
                return {i, j};

    return {-1, -1};
}

// Hàm chuẩn hóa văn bản đầu vào
string prepareText(string text)
{
    string result = "";
    // Loại bỏ khoảng trắng và chuyển thành chữ hoa
    text.erase(remove_if(text.begin(), text.end(), ::isspace), text.end());
    transform(text.begin(), text.end(), text.begin(), ::toupper);
    // Thêm 'X' giữa các ký tự trùng nhau và cuối văn bản nếu độ dài lẻ
    for (int i = 0; i < text.length(); i++)
    {
        result += text[i];

        if (i + 1 < text.length() && text[i] == text[i + 1])
            result += 'X';
    }

    if (result.length() % 2 != 0)
        result += 'X';

    return result;
}

// Hàm mã hóa văn bản
string encrypt(string text)
{
    string cipher = "";

    for (int i = 0; i < text.length(); i += 2)
    {
        char a = text[i];
        char b = text[i + 1];

        auto p1 = findPosition(a);
        auto p2 = findPosition(b);

        int r1 = p1.first, c1 = p1.second;
        int r2 = p2.first, c2 = p2.second;

        if (r1 == r2)
        {
            cipher += matrix5[r1][(c1 + 1) % 5];
            cipher += matrix5[r2][(c2 + 1) % 5];
        }
        else if (c1 == c2)
        {
            cipher += matrix5[(r1 + 1) % 5][c1];
            cipher += matrix5[(r2 + 1) % 5][c2];
        }
        else
        {
            cipher += matrix5[r1][c2];
            cipher += matrix5[r2][c1];
        }
    }

    return cipher;
}

// Hàm giải mã văn bản
string decrypt(string text)
{
    string plain = "";

    for (int i = 0; i < text.length(); i += 2)
    {
        char a = text[i];
        char b = text[i + 1];

        auto p1 = findPosition(a);
        auto p2 = findPosition(b);

        int r1 = p1.first, c1 = p1.second;
        int r2 = p2.first, c2 = p2.second;

        if (r1 == r2)
        {
            plain += matrix5[r1][(c1 + 4) % 5];
            plain += matrix5[r2][(c2 + 4) % 5];
        }
        else if (c1 == c2)
        {
            plain += matrix5[(r1 + 4) % 5][c1];
            plain += matrix5[(r2 + 4) % 5][c2];
        }
        else
        {
            plain += matrix5[r1][c2];
            plain += matrix5[r2][c1];
        }
    }

    return plain;
}

// Main function
int main()
{
    int choice;

    cout << "1. Encrypt\n";
    cout << "2. Decrypt\n";
    cout << "Choose: ";
    cin >> choice;

    cin.ignore();

    cout << "Enter key: ";
    getline(cin, key);

    generateMatrix(key);
    printMatrix();

    cout << "Enter text: ";
    getline(cin, text);

    if (choice == 1)
    {
        string prepared = prepareText(text);
        cout << "Prepared text: " << prepared << endl;
        cout << "Ciphertext: " << encrypt(prepared) << endl;
    }
    else
    {
        transform(text.begin(), text.end(), text.begin(), ::toupper);
        cout << "Plaintext: " << decrypt(text) << endl;
    }

    return 0;
}