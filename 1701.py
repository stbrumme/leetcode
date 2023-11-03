class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        done = 0
        wait = 0
        for arrive, duration in customers:
            done  = max(done, arrive) + duration
            wait += done - arrive

        return wait / len(customers)
