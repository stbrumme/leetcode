class Solution:
    def rand10(self):
        sum = 0
        for i in range(10):
            sum += rand7() - 1

        return 1 + sum % 10
