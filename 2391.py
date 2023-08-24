class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        units = 0
        totaltravel = 0
        paper = 0
        waste = 0
        metal = 0
        for i in range(len(garbage)):
            if i > 0:
                totaltravel += travel[i-1]
            units += len(garbage[i])
            if 'P' in garbage[i]:
                paper = totaltravel
            if 'G' in garbage[i]:
                waste = totaltravel
            if 'M' in garbage[i]:
                metal = totaltravel

        return units + paper + waste + metal
