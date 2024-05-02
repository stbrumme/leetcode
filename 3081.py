class Solution:
    def minimizeStringValue(self, s: str) -> str:
        result = ""

        abc = "abcdefghijklmnopqrstuvwxyz"

        # count all characters, create a min-heap
        have = [ ( s.count(a), a ) for a in abc ]
        heapify(have)

        # replace questions marks by least frequent characters
        need = s.count("?")
        replace = { a: 0 for a in abc }
        for _ in range(need):
            low, c = have[0]
            heapreplace(have, ( low + 1, c ))
            replace[c] += 1

        # actually replace question marks
        use = "a"
        for c in s:
            if c == "?":
                while replace[use] == 0:
                    use = chr(ord(use) + 1) # next letter
                result += use
                replace[use] -= 1
            else:
                result += c

        return result
