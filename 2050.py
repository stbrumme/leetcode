class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        pre  = defaultdict(set)
        post = defaultdict(set)
        for prev, next in relations:
            pre [next].add(prev) # prerequisites
            post[prev].add(next) # follow-up courses

        last  = 0 # when last course finishes
        start = { i : 0 for i in range(1, n + 1) }           # start of each course
        todo  = [ i for i in range(1, n + 1) if not pre[i] ] # all courses without prerequisites
        while todo:
            current = todo.pop()
            finish  = start[current] + time[current - 1]
            last    = max(last, finish)

            for next in post[current]:
                # adjust start of follow-up courses
                start[next] = max(start[next], finish)
                pre  [next].discard(current)
                if not pre[next]: # all prerequisites fulfilled
                    todo.append(next)

        return last
