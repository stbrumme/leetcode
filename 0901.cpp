class StockSpanner {
    map<int, int, std::greater<int>> last;
    int today;

public:
    StockSpanner()
    : last(),
      today(0)
    {
        last[0] = 9999999;
    }

    int next(int price)
    {
        // std::greater => descending order => newest first
        while (last.begin()->second <= price)
            last.erase(last.begin());

        today++;
        int span = today - last.begin()->first;
        last[today] = price;
        return span;
    }
};
