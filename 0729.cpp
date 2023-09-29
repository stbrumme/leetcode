class MyCalendar {
    map<double, int> events;
    const int START = 0;
    const int END   = 1;

public:
    bool book(int start, int end)
    {
        double end2 = end - 0.1;
        auto s = events.lower_bound(start);
        auto e = events.lower_bound(end);

        // start at same time
        if (s != events.end() && s->first == start)
            return false;
        // started earlier but not finished
        if (s != events.begin() && prev(s)->second == START)
            return false;
        // something inbetween
        if (s != e)
            return false;

        events[start] = START;
        events[end2]  = END;
        return true;
    }
};
