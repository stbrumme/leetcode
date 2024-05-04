class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        result = ""

        # step 1: find longest common subsequence
        # step 2: greedily output each string until hitting a character from step 1

        size1 = len(str1)
        size2 = len(str2)

        # find shortest length using a space-optimized LCS approach
        previous = [ "" ] * (size2 + 1)
        for i in range(1, size1 + 1):
            current  = [ "" ] * (size2 + 1)
            for j in range(1, size2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    current[j] = previous[j - 1] + str1[i - 1] # or str2[j - 1]
                else:
                    if len(current[j - 1]) >= len(previous[j]):
                        current[j] = current[j - 1]
                    else:
                        current[j] = previous[j]
            previous = current
        common = current[-1]

        # step 2
        for c in common:
            one = str1.find(c)
            result += str1[: one]
            str1    = str1[one + 1 :]

            two = str2.find(c)
            result += str2[: two]
            str2    = str2[two + 1 :]

            result += c

        return result + str1 + str2
