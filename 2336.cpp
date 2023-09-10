class SmallestInfiniteSet {
    // let's try a unusual approach ... std::set<int> would be much easier
    bitset<1002> inf;
    int lowpos;
public:
    SmallestInfiniteSet() {
        lowpos = 1;     // one-based
        inf.set();
        inf[0] = false; // stop-marker
    }

    int popSmallest() {
        int result = lowpos;
        inf[lowpos] = false;
        while (!inf[lowpos])
            lowpos++;
        return result;
    }

    void addBack(int num) {
        inf[num] = true;
        if (num < lowpos)
            lowpos = num;
        else
            while (!inf[lowpos])
                lowpos++;
    }
};
