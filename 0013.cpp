class Solution {
public:
    int romanToInt(string s) {
        char prev = 0;
        int result = 0;
        for (auto c : s)
        {
            switch (c)
            {
                case 'I': result++; break;
                case 'V': if (prev == 'I') result += 5-2*1; else result += 5; break;
                case 'X': if (prev == 'I') result += 10-2*1; else result += 10; break;
                case 'L': if (prev == 'X') result += 50-2*10; else result += 50; break;
                case 'C': if (prev == 'X') result += 100-2*10; else result += 100; break;
                case 'D': if (prev == 'C') result += 500-2*100; else result += 500; break;
                case 'M': if (prev == 'C') result += 1000-2*100; else result += 1000; break;
            }

            prev = c;
        }
        return result;
    }
};
