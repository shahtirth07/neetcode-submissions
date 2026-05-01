class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        bitset<32> bits = n;
        string str = bits.to_string();
        reverse(str.begin(), str.end());
        uint32_t res = stoul(str, nullptr, 2);
        return res;
    }
};
