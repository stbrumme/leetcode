class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # brute forcing the first few grids gave the sequence 0,12,60,168,360,660,...
        # which is https://oeis.org/A300758
        # the formula is a(n) = 2n*(n+1)*(2n+1)
        # where the perimeter is 8*n

        # that's not a lot of programming, therefore I want to make it run a bit faster
        # "step" tries to make big steps and then refines
        step = 100
        n = 0
        while True:
            apples = 2 * n * (n + 1) * (2 * n + 1)
            if apples >= neededApples:
                if step == 1:
                    return 8 * n

                n -= step # go back and take smaller steps
                step //= 10

            n += step
