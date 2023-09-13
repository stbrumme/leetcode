class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        need = tickets[k]
        for i in range(len(tickets)):
            buy = min(tickets[i], need)
            if i > k: # one less if behind in queue
                buy = min(tickets[i], need - 1)
            total += buy

        return total
