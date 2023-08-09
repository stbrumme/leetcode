class FreqStack {
    unordered_map<int, int> freq;
    map<int, unordered_set<int>> inverse;
    list<int> stack;

public:
    void push(int val) {
        int before = freq[val];
        if (before > 0)
        {
            inverse[before].erase(val);
            if (inverse[before].empty())
                inverse.erase(before);
        }

        int now = before + 1;
        freq[val] = now;
        inverse[now].insert(val);
        stack.push_back(val);
    }

    int pop() {
        auto& most = inverse.rbegin()->second;

        for (auto i = prev(stack.end()); ; i--)
        {
            int top = *i;
            if (most.count(top) == 0)
                continue;

            int before = freq[top];
            int now = before - 1;

            freq[top] = now;
            inverse[before].erase(top);
            if (inverse[before].empty())
                inverse.erase(before);

            if (now > 0)
                inverse[now].insert(top);

            stack.erase(i);

            return top;
        }

        return -1;
    }
};
