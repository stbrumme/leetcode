class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        size  = len(customers)
        # satisfied people when the bookstore owner doesn't use his secret
        happy = sum([ (1 - grumpy[i]) * customers[i] for i in range(size) ])

        result = 0
        secret = 0 # formerly unsatisfied people who only like the store because the secret is currently in use
        for i in range(size):
            # sliding window
            secret     += customers[i]   * grumpy[i]
            if i >= minutes:
                old     = i - minutes
                secret -= customers[old] * grumpy[old]

            result = max(result, happy + secret)

        return result
