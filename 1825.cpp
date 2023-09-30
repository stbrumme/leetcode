class MKAverage {
    deque<int> data;
    map<int, int> freq;
    int size, ignore;

public:
    MKAverage(int m, int k)
    : data(),
      freq(),
      size(m),
      ignore(k)
    { }

    void addElement(int num)
    {
        data.push_back(num);
        freq[num]++;
        if (data.size() > size)
        {
            freq[data.front()]--; // optional: delete this entry if zero
            data.pop_front();
        }
    }

    int calculateMKAverage()
    {
        if (data.size() < size)
            return -1;

        int64_t sum = 0;
        int skip = ignore;
        int have = 0;
        int need = size - 2*ignore;
        for (auto i : freq)
        {
            // ignore this number
            if (i.second <= skip)
            {
                skip -= i.second;
                continue;
            }

            int take = i.second;
            // take only partial (left side)
            if (skip > 0)
            {
                take -= skip;
                skip  = 0;
            }
            // take only partial (right side)
            take = min(take, need - have);

            sum  += take * i.first;
            have += take;
            if (have == need)
                break;
        }

        return sum / need;
    }
};
