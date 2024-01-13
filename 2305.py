class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        have = [ 0 ] * k # cookies per kid

        # worst unfairness: give all cookies to one kid
        best = sum(cookies)

        # assign largest bag to first kid
        cookies.sort()
        have[0] = cookies.pop()

        # iterate through all assignments of a bag
        def deeper(bag):
            nonlocal have, best

            # abort if high unfairness
            unfairness = max(have)
            if unfairness >= best:
                return

            # all cookies distributed
            if bag == len(cookies):
                # must be a new minimum
                best = unfairness
                return

            result = +inf
            # try to give each bag to each kid (and start recursion with next bag)
            for i in range(k):
                have[i] += cookies[bag]
                deeper(bag + 1)
                have[i] -= cookies[bag]

        deeper(0)
        return best
