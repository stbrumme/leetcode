class Solution:
    def longestValidParentheses_old(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        offset = 100000
        depth = offset # avoid negative depths
        nesting = []
        for c in s:
            if c == "(":
                depth += 1
                nesting.append(depth)
            else:
                nesting.append(depth)
                if depth > 0: # negative always invalid
                    depth -= 1

        first = {}
        last  = {}
        for n in range(size):
            current = nesting[n]
            if current == 0:
                continue
            if s[n] == "(" and current not in first:
                first[current] = n

            if s[n] == ")":
                last[current] = n

        best = 0
        for i in first:
            if i in last:
                left  = first[i]
                right = last[i]
                distance = right - left + 1
                if distance > 1 and best < distance:
                    ok = True
                    for x in range(left, right):
                        if nesting[x] < nesting[left]:
                            ok = False
                            break

                    if ok:
                        best = distance

        return best

    def longestValidParentheses(self, s: str) -> int:
        size = len(s)

        brackets = []
        for c in s:
            brackets.append(c)

        again = True
        iterations = 0
        while again:
            again = False

            iterations += 1

            i = 0
            while i < size:
                if i+1 < size and brackets[i] == "(" and brackets[i+1] == ")":
                    brackets[i] = 2
                    del brackets[i+1]
                    size -= 1
                    again = True
                elif i+1 < size and type(brackets[i]) == int and type(brackets[i+1]) == int:
                    brackets[i] += brackets[i+1]
                    del brackets[i+1]
                    size -= 1
                    again = True
                elif i+2 < size and brackets[i] == "(" and type(brackets[i+1]) == int and brackets[i+2] == ")":
                    brackets[i] = brackets[i+1] + 2
                    del brackets[i+2] # delete order is important !
                    del brackets[i+1]
                    size -= 2
                    again = True

                i += 1

        best = 0
        for b in brackets:
            if type(b) == int:
                best = max(best, b)

        return best
