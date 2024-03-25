class Solution:
    def magicalString(self, n: int) -> int:
        # understanding the problem: 30 minutes
        # writing the code:           5 minutes
        # that's ridiculous ...

        # by the way:
        # https://en.wikipedia.org/wiki/Kolakoski_sequence
        # https://oeis.org/A156077 and https://oeis.org/A000002

        sequence = [ 1, 2, 2 ]
        pos = 2
        while len(sequence) < n:
            last   = sequence[-1]
            length = sequence[pos]
            pos   += 1

            sequence += [ last ^ 3 ] * length # same as 3 - last, but looks nicer to me :-)

        # maybe we need to strip trailing elements
        while len(sequence) > n:
            sequence.pop()

        return sequence.count(1)
