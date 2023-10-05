class MyCircularDeque {
    deque<int> circular;
    int capacity;

public:
    MyCircularDeque(int k)
    : circular(),
      capacity(k)
    { }

    bool insertFront(int value)
    {
        if (isFull())
            return false;

        circular.push_front(value);
        return true;
    }

    bool insertLast(int value)
    {
        if (isFull())
            return false;

        circular.push_back(value);
        return true;
    }

    bool deleteFront()
    {
        if (isEmpty())
            return false;
        circular.pop_front();
        return true;
    }

    bool deleteLast()
    {
        if (isEmpty())
            return false;
        circular.pop_back();
        return true;
    }

    int getFront() const
    {
        return isEmpty() ? -1 : circular.front();
    }

    int getRear() const
    {
        return isEmpty() ? -1 : circular.back();
    }

    bool isEmpty() const
    {
        return circular.empty();
    }

    bool isFull() const
    {
        return circular.size() == capacity;
    }
};
