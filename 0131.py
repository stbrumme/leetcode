class Solution:
    @cache
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        halfsize = len(s) // 2
        return s[0:halfsize] == s[-halfsize:][::-1]

    @cache
    def deeper(self, s):
        size = len(s)
        if size == 0:
            return None
        if size == 1:
            return [ [ s ] ]

        result = []
        for i in range(1, size+1):
            current = s[:i]
            other   = s[i:]

            if not self.isPalindrome(current):
                continue

            next = self.deeper(other)
            if not next:
                result.append([ current ])
                continue
            for x in next:
                result.append([ current ] + x)

        return result

    def partition(self, s: str) -> List[List[str]]:
        return self.deeper(s)
