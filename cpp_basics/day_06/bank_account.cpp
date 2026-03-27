#include<iostream>
#include<string>
using namespace std;

class Account{
    private: 
        string account_id = "";
        string name;
        float money;

    public:
        void add_money(float cash){
            money += cash;
        }

        void sub_money(float cash){
            money -= cash;
        }

        float get_money(){
            return money;
        }

        Account(string name){
            this->name = name;
            this->money = 0;
        }
};

int main(){
    Account lisi("李四");
    lisi.add_money(5000);
    lisi.sub_money(500);
    cout << "李四账户余额：" << lisi.get_money() << endl;
    return 0;
}