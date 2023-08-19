class Solution:
    @cache
    def dot(self, text, pattern):
        if not pattern:
            return len(text) == 1
        if pattern[0] == "*":
            for i in range(len(text), -1, -1): # longest first
                if self.match(text[i:], pattern[1:]):
                    return True
            return False

        if not text:
            return False

        return self.match(text[1:], pattern)

    @cache
    def star(self, text, pattern, letter):
        same = 0
        while same < len(text) and text[same] == letter:
            same += 1

        # longest first to reduce recursion
        while same >= 0:
            if self.match(text[same:], pattern):
                return True
            same -= 1
        return False

    @cache
    def match(self, text, pattern):
        if not pattern:
            return not text

        if pattern[0] == ".":
            return self.dot(text, pattern[1:])

        if len(pattern) >= 2 and pattern[1] == "*":
            return self.star(text, pattern[2:], pattern[0])

        if not text:
            return False

        i = 0
        while i < len(pattern) and i < len(text) and pattern[i] == text[i]:
            i += 1

        if i > 0 and i < len(pattern) and pattern[i] == "*":
            i -= 1

        if i == 0:
            return False
        return self.match(text[i:], pattern[i:])


    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s, p)
