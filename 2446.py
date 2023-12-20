class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # start/end
        s1, e1 = event1
        s2, e2 = event2

        if s1 < s2:
            return e1 >= s2
        else:
            return e2 >= s1
