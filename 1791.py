class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # two edges are sufficient
        a, b = edges[0]
        c, d = edges[1]
        # find duplicate
        four = [ a,b,c,d ]
        while four:
            x = four.pop()
            if x in four:
                return x
