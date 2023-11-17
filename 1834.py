class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        incoming = []
        for i, ( start, duration ) in enumerate(tasks):
            heappush(incoming, ( start, duration, i ))

        timestamp = 0
        waiting   = []
        done      = 0
        while done < len(tasks):
            # CPU was idle, pick next job
            if not waiting:
                start, duration, i = heappop(incoming)
                timestamp = max(timestamp, start) # skip forward
                heappush(waiting, ( duration, i ))

            # jobs becoming available
            while incoming and incoming[0][0] <= timestamp:
                start, duration, i = heappop(incoming)
                heappush(waiting, ( duration, i ))

            # process job
            duration, i = heappop(waiting)
            timestamp  += duration
            done       += 1
            yield i
