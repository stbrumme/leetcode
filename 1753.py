class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        result = 0

        state = [ a, b, c ]
        state.sort()
        while True:
            # pick a stone from the smallest and the largest pile
            state[0]  -= 1
            state[-1] -= 1

            result += 1

            # simpler/faster than state.sort()
            if state[-1] < state[-2]:
                state[-1], state[-2] = state[-2], state[-1]

            # remove empty piles
            while state[0] == 0:
                del state[0]
                if len(state) < 2:
                    return result
