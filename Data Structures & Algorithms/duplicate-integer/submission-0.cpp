using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> num;
        for (int i: nums) {
            if(find(num.begin(), num.end(), i) != num.end()) {
                return true;
            }
            else {
                num.push_back(i);
            }
        }
        return false;
    }
};
