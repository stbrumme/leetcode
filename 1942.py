class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        size = len(times)
        # all chairs are initially empty, a sorted list is a min-heap as well
        available = list(range(size))
        occupied  = [ False ] * size

        # when does he arrive
        target = times[targetFriend][0]

        leave = [] # min-heap
        for arrive, depart in sorted(times): # in order of arrival
            # process all "leave" events
            while leave and leave[0][0] <= arrive:
                when, where = heappop(leave)
                occupied[where] = False # "available"" have contain stale data now
                heappush(available, where)

            # clean up garbage (stale entries on top of the heap)
            while occupied[available[0]]:
                heappop(available)
            # finally found a free seat ...
            where = heappop(available)
            # it's our friend
            if arrive == target:
                return where
            # take seat (again, "available" may have stale entries)
            occupied[where] = True

            # add current person's "leave" event
            heappush(leave, ( depart, where ))
