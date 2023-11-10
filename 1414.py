class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # generate Fibonacci sequence
        fib = [ 1, 1 ]
        while fib[-1] < k:
            fib.append(fib[-2] + fib[-1])

        # subtract largest elements of that sequence
        steps = 0
        while k > 0:
            if fib[-1] <= k:
                k     -= fib[-1]
                steps += 1
            fib.pop()
        return steps
