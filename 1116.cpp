class ZeroEvenOdd {
private:
    atomic<int> limit, current;
    atomic<int> state;

public:
    ZeroEvenOdd(int n) {
        limit   = n;
        current = 0;
        state   = 0;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        while (current < limit)
            if (state % 2 == 0)
            {
                printNumber(0);
                state++;
            }
    }

    void even(function<void(int)> printNumber) {
        while (current < limit)
            if (state == 3)
            {
                printNumber(++current);
                state = 0;
            }
    }

    void odd(function<void(int)> printNumber) {
        while (current < limit)
            if (state == 1)
            {
                printNumber(++current);
                state = 2;
            }
    }
};
