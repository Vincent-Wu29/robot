#include<iostream>
using namespace std;

int main(){
    int num1, num2;
    char oper;

    cout << "数字1：";
    cin >> num1;
    cout << "数字2：";
    cin >> num2;
    cout << "运算符(+、-、*、/)：";
    cin >> oper;

    switch (oper){
        case '+':
            cout << num1 + num2 << endl;
            break;
        case '-':
            cout << num1 - num2 << endl;
            break;
        case '*':
            cout << num1 * num2 << endl;
            break;
        case '/':
            if (num2 == 0){
                cout << "除数不能为0" << endl;
                break;
            }
            cout << num1 / num2 << endl;
            break;
    }
}