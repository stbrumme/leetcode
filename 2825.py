class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        pos = 0 # index in str2
        for one in str1:
            have = str2[pos]
            # use identical character
            okay = (have == one)
            # rotate character
            if not okay:
                need = ord(one) - ord("a")  # from ASCII to 0...25
                need = (need + 1) % 26      # rotate
                need = chr(need + ord("a")) # from 0...25 to ASCII
                okay = (have == need)

            # match
            if okay:
                pos += 1
                if pos == len(str2):
                    return True

        return False
