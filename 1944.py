class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # put a super-large person on the left-most place
        heights.insert(0, +inf)
        taller  = [ 0 ]

        size    = len(heights)
        visible = [ 0 ] * size

        for i in range(1, size): # skip the super-large one
            current = heights[i]
            while heights[taller[-1]] <= current:
                # we are bigger than someone one the left
                gnome = taller.pop()
                # so they can see us
                visible[gnome] += 1

            # a taller person to be added ...
            visible[taller[-1]] += 1
            # ... the current person is taller than their left neightbors
            taller.append(i)

        return visible[1:] # except that super-tall guy
