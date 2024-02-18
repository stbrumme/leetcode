class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        result = 0

        heapify(players)
        heapify(trainers)

        while players and trainers:
            if players[0] <= trainers[0]:
                heappop(players)
                result += 1

            heappop(trainers)

        return result
