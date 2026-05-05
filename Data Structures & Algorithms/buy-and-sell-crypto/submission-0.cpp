class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0, r = 1;
        int maxprice = 0;
        while(r <prices.size()) {
            if(prices[i]<prices[r]) {
                int profit = prices[r] - prices[i];
                maxprice = max(profit, maxprice);
            } else{
                i=r;
            }

            r++;
        }
        return maxprice;
    }
};
