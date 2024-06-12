from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.step = 1
        self.last = n
        self.cv   = Condition()

    # all four functions are extremely similar

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.step <= self.last:
                if self.step % 3 == 0 and self.step % 5 != 0:
                    printFizz()
                    self.step += 1
                    self.cv.notifyAll()
                else:
                    self.cv.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.step <= self.last:
                if self.step % 5 == 0 and self.step % 3 != 0:
                    printBuzz()
                    self.step += 1
                    self.cv.notifyAll()
                else:
                    self.cv.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.step <= self.last:
                if self.step % 15 == 0:
                    printFizzBuzz()
                    self.step += 1
                    self.cv.notifyAll()
                else:
                    self.cv.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            while self.step <= self.last:
                if self.step % 3 != 0 and self.step % 5 != 0:
                    printNumber(self.step)
                    self.step += 1
                    self.cv.notifyAll()
                else:
                    self.cv.wait()
