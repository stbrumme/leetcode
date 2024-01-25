class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # min-heap ( weight, index )
        available = [ ( s, i ) for i, s in enumerate(servers) ]
        heapify(available)
        # min-heap ( end-of-work-timestamp, weight, index )
        working = []
        # min-heap ( start-of-job, duration )
        jobs = [ ( i, t ) for i, t in enumerate(tasks) ]

        second = 0
        while jobs:
            # some servers may have finished their tasks
            while working and working[0][0] <= second:
                when, weight, who = heappop(working)
                heappush(available, ( weight, who ))

            # start tasks
            while available and jobs[0][0] <= second:
                queued, duration = heappop(jobs)
                weight, who      = heappop(available)
                heappush(working, ( second + duration, weight, who ))
                yield who

                # all tasks done
                if not jobs:
                    return

            second += 1
            # skip second where nothing starts or ends
            if not available:
                second = max(second, working[0][0])
