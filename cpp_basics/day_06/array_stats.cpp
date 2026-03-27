#include<iostream>
#include<vector>
using namespace std;

void array_stats(vector<int>);

int main(){
    vector<int> array{4,2,6,2,7,62,5,8,2,5};
    array_stats(array);
}

void array_stats(vector<int> array){
    int max = 0;
    int min = 1000;
    int sum = 0;
    int average;
    for (int i = 0; i < array.size(); i++){
        if (array[i] > max){
            max = array[i];
        }
        if (array[i] < min){
            min = array[i];
        }
        sum += array[i];
    }

    cout << "最大值：" << max << endl;
    cout << "最小值：" << min << endl;
    cout << "平均值：" << float(sum) / array.size() << endl;
}