class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = { w : i for i, w in enumerate(list1) }
        both  = sorted([ (i + dict1[w], w) for i, w in enumerate(list2) if w in dict1 ])
        return [ w for i, w in both if i == both[0][0] ]
