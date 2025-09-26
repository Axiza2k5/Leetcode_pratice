#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int width = 0;
        int maxx = -1;
        
        while(left < right)
        {
            width = right-left;
            maxx = std::max(std::min(height[left], height[right])*(right-left), maxx);

            if (height[left] < height[right])
                left++;
            else right--;
        }
        return maxx;
    }

    // 58/65
    // int maxArea(vector<int>& height) {
    //     int sz = height.size();
    //     long long maxx = -1;
    //     for(int i = 0; i < sz-1;i++)
    //     {
    //         for(int j = sz;j >i;j--)
    //         {
    //             long long minHeight = height[i] > height[j] ? height[j] : height[i];
    //             long long val = minHeight * (j-i);
    //             maxx = val > maxx ? val : maxx;
    //         }
    //     }
    //     return maxx;
    // }
};