from threading import Semaphore, Lock

class H2O:
    # oxygen will be blocked until two hydrogen arrived, which in turn unblock hydrogen
    # 0. initially oxygen is blocked
    # 1. when the first  hydrogen arrives, an "H" will be sent
    # 2. when the second hydrogen arrives, an "H" will be sent and oxygen unblocked
    # 3. oxygen then sends "O" and unblocks 2 hydrogens for further use

    def __init__(self):
        self.hydro = Semaphore(2) # signal when acquired twice
        self.oxy   = Lock()       # signal when acquired once, initially signalled
        self.oxy.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydro.acquire()

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

        if self.hydro._value == 0:
            self.oxy.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxy.acquire()

        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()

        self.hydro.release(2)
