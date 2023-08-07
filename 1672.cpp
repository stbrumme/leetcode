class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxcust = 0;
        int maxmoney = 0;
        for (int cust = 0; cust < accounts.size(); cust++)
        {
            int money = 0;
            for (auto m : accounts[cust])
                money += m;
            if (money < maxmoney)
                continue;

            maxmoney = money;
            maxcust = cust;
        }
        return maxmoney;
    }
};
