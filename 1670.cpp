class FrontMiddleBackQueue
{
    // the test cases are fairly small, maybe a simple deque with generic insert/erase would suffice
    // nevertheless, let's write a proper solution
    list<int> data;
    list<int>::iterator middle;

public:
    FrontMiddleBackQueue()
    {
        middle = data.begin(); // == data.end()
    }

    void pushFront(int val)
    {
        data.push_front(val);

        if (data.size() <= 1)
            middle = data.begin();
        else if (data.size() % 2 == 0)
            middle--;
    }

    void pushMiddle(int val)
    {
        if (data.size() <= 1)
        {
            middle = data.insert(data.begin(), val);
        }
        else
        {
            if (data.size() % 2 == 0)
                middle++;
            middle = data.insert(middle, val);
        }
    }

    void pushBack(int val)
    {
        data.push_back(val);

        if (data.size() <= 1)
            middle = data.begin();
        else if (data.size() % 2 == 1)
            middle++;
    }

    int popFront()
    {
        if (data.empty())
            return -1;

        int result = data.front();
        if (data.size() % 2 == 0)
            middle++;
        data.pop_front();

        return result;
    }

    int popMiddle()
    {
        if (data.empty())
            return -1;

        int result = *middle;
        middle = data.erase(middle);
        if (data.size() % 2 == 0 && !data.empty())
            middle--;

        return result;
    }

    int popBack()
    {
        if (data.empty())
            return -1;

        int result = data.back();
        if (data.size() % 2 == 1)
            middle--;
        data.pop_back();

        return result;
    }
};
