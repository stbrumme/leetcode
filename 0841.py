class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        size = len(rooms)
        closed = set(range(size))
        keys   = [ 0 ]

        while keys:
            next = []
            for open in keys:
                if open in closed:
                    keys += rooms[open]
                    closed.discard(open)
            keys = next

        return not closed
