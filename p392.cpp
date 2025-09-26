#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
private:

public:
    bool isSubsequence(string s, string t) {
        int s_z = s.size(), t_z = t.size();
        int j = 0;
        for(int i = 0; i<t_z;i++){
            if(j >= s_z)
                return true;
            if(t[i] == s[j])
                j++;
        }
        return j>= s_z;
    }
};
