class Foo {
        volatile int state;
public:
    Foo() {
        state = 1;
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();

        state++;
    }

    void second(function<void()> printSecond) {
        while (state != 2);

        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();

        state++;
    }

    void third(function<void()> printThird) {
        while (state != 3);

        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};

