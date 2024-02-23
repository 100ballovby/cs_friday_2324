#include <iostream>
#include <string>
using namespace std;

int length(string s) {
    int count = 0;
    for (char _ : s) {
        count += 1;
    }
    return count;
}

string both_ends(string str) {
    string res;
    if (str.size() < 2) {
        return "";
    }
    res = str.substr(0, 2) + str.substr(str.size() - 2, 2);
    return res;
}

string change_char(string str) {
    char first_char = str[0];
    for (int i = 1; i < str.size(); i++) {
        if (str[i] == first_char) {
            str[i] = '$';
        }
    }
    return str;
}

string char_mix_up(string a, string b) {
    string new_a = b.substr(0,1) + a.substr(1);
    string new_b = a.substr(0,1) + b.substr(1);
    string res = new_a + " " + new_b;
    return res;
}




int main() {
    // Write C++ code here
    string s = "Hello, world!";
    for (int i = 0; i < length(s); i++) {
        cout << s[i] << endl;
    }
    cout << both_ends("hello") << endl;
    cout << both_ends("h") << endl;
    cout << both_ends("w3school") << endl;

    cout << change_char("abracadabra") << endl;

    cout << char_mix_up("abc", "xyz") << endl;
    return 0;
}