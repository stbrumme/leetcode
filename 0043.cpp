class Solution {
public:
    void addReversed(string& result, string& num2)
    {
        while (result.size() < num2.size() && num2.back() == '0')
            num2.pop_back();
        while (result.size() < num2.size())
            result += '0';
        while (result.size() > num2.size())
            num2 += '0';

        int carry = 0;
        for (int i = 0; i < result.size(); i++)
        {
            auto sum = carry + (result[i] - '0') + (num2[i] - '0');
            result[i] = (sum % 10) + '0';
            carry = sum / 10;
        }
        if (carry > 0)
            result += '1';
    }

    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0")
            return "0";

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());

        // premultiplied
        string two[10];
        string singleSum = num2;
        for (int i = 1; i <= 9; i++)
        {
            two[i] = singleSum;
            addReversed(singleSum, num2);
        }

        string result;
        for (auto one : num1)
        {
            int factor = one - '0';
            addReversed(result, two[factor]);

            for (auto& t : two)
                t.insert(t.begin(), '0');
        }

        reverse(result.begin(), result.end());
        return result;
    }
};

