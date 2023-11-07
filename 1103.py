class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # brute force
        result = [ 0 ] * num_people
        step   = 0
        while candies > 0:
            pos   = step % num_people
            step += 1
            give  = min(step, candies)
            result[pos] += give
            candies     -= give

        return result
