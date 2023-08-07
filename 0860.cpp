class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // order is important !
        int c[21];
        c[5] = c[10] = c[20] = 0;
        for (auto x : bills)
        {
            c[x]++;
            switch (x)
            {
                case 5: break;
                case 10: if (c[5] == 0) return false; c[5]--; break;
                case 20: if (c[5] == 0) return false;
                         if (c[10] == 0)
                         {
                             if (c[5] < 3)
                                return false;
                             c[5] -= 3;
                         }
                         else
                         {
                             c[5]--;
                             c[10]--;
                         }
                         break;
            }
        }
        return true;
    }
};
