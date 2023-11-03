class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # if two ants meet then basically nothing changes:
        # ant A and B change direction but A moves the same path that B would move
        # if there were no A
        # more or less A becomes B and B becomes A
        # so the total duration of ant X on the plank is its distance to the end
        # of the direction it's walking
        l = max(left)      if left  else 0
        r = n - min(right) if right else 0
        return max(l, r)
