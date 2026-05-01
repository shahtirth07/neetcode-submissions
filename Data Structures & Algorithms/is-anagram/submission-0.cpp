class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> freq1;
        for (char c : s) {
            freq1[c]++;
        }
        for (char d : t) {
            if (freq1.find(d) == freq1.end()) {
                return false;
            }
            freq1[d]--;

            if (freq1[d] < 0) {
                return false;
            }
        }

        return true;
    }
};
