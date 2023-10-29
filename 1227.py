class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # this is a weird problem:
        # writing a simulation was fun but figuring out
        # that the math behind it leads to a one-liner makes me feel bad

        if n < 10:
            # simulation
            last = n - 1 # zero-based
            correct = 0
            for first in range(n):
                occupied = [ False ] * n
                occupied[first] = True
                for i in range(1, last): # all except the first and last
                    if occupied[i]:
                        # pick randomly an available seat
                        available = n - i
                        pick = randint(1, available)
                        for j in range(n):
                            if not occupied[j]:
                                pick -= 1
                                if pick == 0:
                                    occupied[j] = True
                                    break

                        # last passenger's seat taken
                        if occupied[last]:
                            break
                    else:
                        # pre-assigned seat
                        occupied[i] = True

                if not occupied[last]:
                    correct += 1

            #print(correct / n)

        # yes, that's all there is ...
        return 1 if n == 1 else 0.5
