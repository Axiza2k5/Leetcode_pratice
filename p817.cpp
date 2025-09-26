#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>


using namespace std;


class Solution {
private:

public:
    int numComponents(ListNode* head, vector<int>& nums) {
        int count = 0;
        std::unordered_map<int, bool> map;
        for(auto it : nums)
        {
            map[it] = 1;
        }

        while(head != nullptr)
        {
            if(map.find(head->val) != map.end())
            {
                count++;
                while((head != nullptr) && (map.find(head->val) != map.end()))
                {
                    head = head->next;
                }
            }
            if (head != nullptr)
                head = head->next;

        }
        return count;
    }
};
