class Solution:
    def validStrings(self, n: int) -> List[str]:
        # use ints instead of string because it's a bit faster
        todo = deque([ 1, 0 ])
        stop = 1 << (n - 1) # enough bits

        while True:
            if todo[0] >= stop:
                break

            # append 0 and/or 1
            t = todo.popleft()
            if t & 1:
                todo.append(t * 2)
            todo.append(t * 2 + 1)

        # convert to string, strip "0b" and prepend zero
        for t in todo:
            yield bin(t)[2 :].zfill(n)
