/*Task 2.6: Cài đặt chương trình phân tích tần suất và tấn công giải mã Vigenere cipher.*/
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cctype>
#include <cmath>

using namespace std;

// Tần suất chữ cái tiếng Anh
map<char, double> ENGLISH_FREQ = {
    {'A', 0.0817}, {'B', 0.0150}, {'C', 0.0278}, {'D', 0.0425}, {'E', 0.1270}, {'F', 0.0223}, {'G', 0.0202}, {'H', 0.0609}, {'I', 0.0697}, {'J', 0.0015}, {'K', 0.0077}, {'L', 0.0403}, {'M', 0.0241}, {'N', 0.0675}, {'O', 0.0751}, {'P', 0.0193}, {'Q', 0.0010}, {'R', 0.0599}, {'S', 0.0633}, {'T', 0.0906}, {'U', 0.0276}, {'V', 0.0098}, {'W', 0.0236}, {'X', 0.0015}, {'Y', 0.0197}, {'Z', 0.0007}};

string clean_text(string text)
{
    string result = "";

    for (char c : text)
    {
        if (isalpha(c))
            result += toupper(c);
    }

    return result;
}

double get_index_of_coincidence(string text)
{
    int n = text.length();

    if (n <= 1)
        return 0;

    map<char, int> counts;

    for (char c : text)
        counts[c]++;

    double ic = 0;

    for (auto &p : counts)
    {
        ic += p.second * (p.second - 1);
    }

    ic /= (double)(n * (n - 1));

    return ic;
}

int find_key_length(string ciphertext, int max_len = 20)
{
    int best_len = 1;
    double closest_ic = 0;

    for (int length = 1; length <= max_len; length++)
    {
        vector<double> ics;

        for (int i = 0; i < length; i++)
        {
            string subsequence = "";

            for (int j = i; j < ciphertext.length(); j += length)
                subsequence += ciphertext[j];

            ics.push_back(get_index_of_coincidence(subsequence));
        }

        double avg_ic = 0;

        for (double x : ics)
            avg_ic += x;

        avg_ic /= ics.size();

        if (abs(avg_ic - 0.067) < abs(closest_ic - 0.067))
        {
            closest_ic = avg_ic;
            best_len = length;
        }
    }

    return best_len;
}

double chi_squared_score(string text)
{
    int n = text.length();
    map<char, int> counts;

    for (char c : text)
        counts[c]++;

    double score = 0;

    for (auto &p : ENGLISH_FREQ)
    {
        char c = p.first;
        double freq = p.second;

        int observed = counts[c];
        double expected = freq * n;

        score += pow(observed - expected, 2) / expected;
    }

    return score;
}

string decrypt_caesar(string text, int shift)
{
    string result = "";

    for (char c : text)
        result += char((c - 'A' - shift + 26) % 26 + 'A');

    return result;
}

void crack_vigenere(string ciphertext)
{
    string clean_ct = clean_text(ciphertext);

    int key_len = find_key_length(clean_ct);

    string key = "";

    for (int i = 0; i < key_len; i++)
    {
        string subsequence = "";

        for (int j = i; j < clean_ct.length(); j += key_len)
            subsequence += clean_ct[j];

        int best_shift = 0;
        double min_chi = 1e18;

        for (int shift = 0; shift < 26; shift++)
        {
            string decrypted = decrypt_caesar(subsequence, shift);

            double score = chi_squared_score(decrypted);

            if (score < min_chi)
            {
                min_chi = score;
                best_shift = shift;
            }
        }

        key += char(best_shift + 'A');
    }

    string plaintext = "";
    int key_index = 0;

    for (char c : ciphertext)
    {
        if (isalpha(c))
        {
            int shift = key[key_index % key_len] - 'A';

            char base = isupper(c) ? 'A' : 'a';

            plaintext += char((c - base - shift + 26) % 26 + base);

            key_index++;
        }
        else
            plaintext += c;
    }

    cout << "\n------------------------------\n";
    cout << "PHAN TICH HOAN TAT\n";
    cout << "Do dai khoa du doan: " << key_len << endl;
    cout << "Khoa tim duoc: " << key << endl;
    cout << "------------------------------\n";
    cout << "Ban ro du doan:\n";

    if (plaintext.length() > 500)
        cout << plaintext.substr(0, 500) << "...\n";
    else
        cout << plaintext << endl;
}

int main()
{
    cout << "=== Vigenere Cipher Breaker ===\n";

    string choice;
    cout << "Ban muon nhap tu (1) Ban phim hay (2) File? ";
    cin >> choice;
    cin.ignore();

    string cipher_input;

    if (choice == "2")
    {
        string filename;
        cout << "Nhap ten file (VD: data.txt): ";
        getline(cin, filename);

        ifstream file(filename);

        if (!file)
        {
            cout << "Khong tim thay file!\n";
            return 0;
        }

        string line;
        while (getline(file, line))
            cipher_input += line + "\n";

        file.close();
    }
    else
    {
        cout << "Nhap ciphertext: ";
        getline(cin, cipher_input);
    }

    crack_vigenere(cipher_input);

    return 0;
}