class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        result = +inf

        size = len(tasks)
        all  = (1 << size) - 1 # bitmask of all tasks

        @cache
        def deeper(have, today, days): # bitmask of finished jobs, hours left today
            nonlocal result
            if days >= result:
                return

            if have == all:
                result = days
                return

            best = size
            for i in range(1, size):
                mask = 1 << i
                if not (have & mask):
                    if today >= tasks[i]:
                        # job can be finished today
                        deeper(have | mask, today       - tasks[i], days)
                    else:
                        # finish tomorrow
                        deeper(have | mask, sessionTime - tasks[i], days + 1)

        # always do longest job on the first day
        tasks.sort(reverse = True)

        deeper(1, sessionTime - tasks[0], 1)
        return result
