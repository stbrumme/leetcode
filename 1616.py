class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        size = len(a)

        def deeper(x, y):
            for left in range(size):
                right = size - left - 1
                if left >= right:
                    return True

                # mismatch, split here
                if x[left] != y[right]:
                    # at least one inner section must be a palindrome
                    inner = x[left : right + 1]
                    if inner == inner[::-1]:
                        return True
                    inner = y[left : right + 1]
                    if inner == inner[::-1]:
                        return True

                    # nope
                    return False

        return deeper(a, b) or deeper(b, a)
