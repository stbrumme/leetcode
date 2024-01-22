class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        result = +inf

        jobs.sort(reverse = True) # not needed, but allows for early exit
        total = [ 0 ] * k         # total time of each worker

        def deeper(i): # assign i-th job to each worker and find best combination
            nonlocal result
            longest = max(total)  # worker with highest load
            if longest >= result: # we already had better assignments
                return

            # all jobs assigned
            if i == len(jobs):
                result = longest
                return

            # optimization: try to assign to workers with low load first
            todo = sorted(range(k), key = lambda x : total[x]) # worker IDs, sorted by their load

            # assign current job to each worker and start recursion
            previous = -1 # workload of last worker
            for t in todo:
                # optimization: current worker has same workload as previous,
                #               no need assigning same job to both
                if previous == total[t]:
                    continue
                previous = total[t]

                # assign job
                total[t] += jobs[i]
                # next job
                deeper(i + 1)
                # un-assign
                total[t] -= jobs[i]

        # let's go !
        deeper(0)
        return result
