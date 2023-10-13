class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def deeper(a, b, have):
            current = "".join([ str(h) for h in have ])
            if len(current) >  len(num):
                return []
            if len(current) == len(num):
                return have if current == num else []

            c = a + b
            if c >= 2**31:
                return [] # too big

            # we could abort early if c mismatches but len(num) is quite small
            return deeper(b, c, have + [ c ])

        for i in range(1, len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                a = int(num[:i])
                b = int(num[i:j])

                sequence = deeper(a, b, [ a, b ])
                if len(sequence) >= 3: # empty if failed
                    return sequence

                # no leading zero
                if num[0] == "0" or num[i] == "0":
                    break

        return []
