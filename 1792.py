class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # compute the influence of an extra student
        gain = lambda pas, total: (pas + 1) / (total + 1) - pas / total

        worst  = []
        result = 0
        for pas, total in classes:
            # only consider classes where at least one child fails
            if pas < total:
                # max-heap
                heappush(worst, ( -gain(pas, total), total, pas ))
                result  += pas / total
            else:
                result  += 1

        if not worst:
            return 1 # all classes already passed

        # assign extra students to small classes without perfect score
        for i in range(extraStudents):
            g, total, pas = worst[0]
            result -= pas / total
            pas    += 1
            total  += 1
            result += pas / total
            heappushpop(worst, ( -gain(pas, total), total, pas ))

        return result / len(classes)
