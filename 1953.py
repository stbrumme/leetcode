class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # the project with the most milestones is the critical path:
        # 1) try to always work on that project
        # 2) to avoid violating the second rule, work every second on the project with the second-most milestones

        total = sum(milestones)
        most  = max(milestones)
        other = total - most
        if most > other:
            return 2 * other + 1 # can't finish the longest project:
                                 # start with it, work on other projects every second week
                                 # and work on it once again before rule 2 kicks in
        else:
            return total         # it's possible to finish everything
