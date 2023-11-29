class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def deeper(left, right):
            # basic cases
            if left > right:
                return 0
            if s[left : right + 1] == "()":
                return 1

            open  = 0
            close = 0
            for i in range(left, right + 1):
                if s[i] == "(":
                    open  += 1
                else:
                    close += 1

                # pair of brackets found
                if open == close and i < right:
                    # case "AB"
                    return deeper(left, i) + deeper(i + 1, right)

            # case "(A)"
            return 2 * deeper(left + 1, right - 1)

        return deeper(0, len(s) - 1)
