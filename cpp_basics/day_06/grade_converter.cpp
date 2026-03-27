#include<iostream>
using namespace std;

int main(){
    int score;
    cout << "成绩：";
    cin >> score;
    char degree;
    if (score >= 90){
        degree = 'A';
    }else if (score >= 80){
        /* code */
        degree = 'B';
    }else if (score >= 70){
        degree = 'C';
    } else if (score >= 60){
        degree = 'D';
    } else {
        degree = 'F';
    }

    cout << "成绩：" << score << " " << "等级：" << degree << endl;
    
}