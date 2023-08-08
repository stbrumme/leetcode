class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (auto c : s)
            switch (c)
            {
                case '(':
                case '{':
                case '[':
                    stack.push_back(c);
                    break;

                case ']':
                    if (stack.empty()) return false;
                    if (stack.back() != '[') return false;
                    stack.pop_back();
                    break;
                case '}':
                    if (stack.empty()) return false;
                    if (stack.back() != '{') return false;
                    stack.pop_back();
                    break;
                case ')':
                    if (stack.empty()) return false;
                    if (stack.back() != '(') return false;
                    stack.pop_back();
                    break;
            }

        return stack.empty();
    }
};

