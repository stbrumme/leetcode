class FooBar {
private:
    int n;
    volatile int state; // brute-force it ...

public:
    FooBar(int n) {
        this->n = n;
        state = 0;
    }

    void foo(function<void()> printFoo) {

        for (int i = 0; i < n; i++) {
            while (state != 0);
            state = 0;

            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();

            state = 1;
        }
    }

    void bar(function<void()> printBar) {

        for (int i = 0; i < n; i++) {
            while (state != 1);
            state = 1;

            // printBar() outputs "bar". Do not change or remove this line.
            printBar();

            state = 0;
        }
    }
};
