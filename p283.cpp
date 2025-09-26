#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
private:
    void swap(int &a, int &b){
        int temp = a;
        a = b;
        b = temp;
    }

public:
    void moveZeroes(vector<int>& nums) {
        vector<int>::iterator it = nums.begin();
        cout<<*it<<endl;
        for(auto it2 = nums.begin()+1; it2 != nums.end(); it2++){
            if(*it == 0 && *it2 != 0){
                swap(*it, *it2);
                it++;
            }
            if(*it != 0){
                it++;
            }
        }
        for(auto n : nums){
            cout<<n<<" ";
        }
    }
};
