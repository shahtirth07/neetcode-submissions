class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> chars;
        int l = 0, res = 0;

        for(int r = 0; r < s.size(); r++) {
            while(chars.find(s[r]) != chars.end()) {
                chars.erase(s[l]);
                l++;
            }
            chars.insert(s[r]);
            res = max(res, r-l+1);
        }
        return res;
    }
};
