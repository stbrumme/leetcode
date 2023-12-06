class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # one bucket => it must be poisonous, no tests needed
        if buckets == 1:
            return 0

        # a pig can be tested this often (assuming it survives every time)
        maxTests = minutesToTest // minutesToDie
        # if buckets <= maxTests then a single pig is enough:
        # - give it one bucket a time
        # - if the poor pig dies, we know the poisonous bucket
        # - if it survives at the end, the untested bucket is poisonous
        # - therefore we implicitly tested one more
        maxTests += 1
        # assume we have 3 buckets in example 2 (instead of 4), then one pig is sufficient:
        # - feed bucket 1 at minute 0
        # - if pig is dead at minute 15, bucket 1 was poisonous
        # - if not, feed it bucket 2 at minute 15
        # - if pig is dead at minute 30, bucket 2 was poisonous
        # - if not, the untested bucket 3 is poisonous
        # therefore 30 // 15 + 1 = 3 buckets were tested with one pig

        # if there are multiple pigs p, then assign each bucket a number in base p
        # in example 1 there are four buckets 1,2,3,4
        # let's convert it from one-based to zero-based numbering: 0,1,2,3
        # if we have two pigs then these (binary) numbers would be 00, 01, 10, 11
        # the first pig is matched to the first digit, the second to the second digit, and so on
        # in round 0 we feed:
        # - first  pig: bucket 00 and 10 (0 and 2 in decimal => or 1 and 3 in one-based numbering)
        # - second pig: bucket 00 and 01 (0 and 1 in decimal => or 1 and 2 in one-based numbering)
        # - if both dead, then bucket 00 was the cause
        # - if only first  pig dead: bucket 10
        # - if only second pig dead: bucket 01
        # - if both alive, then bucket 11 is bad
        capacity = 1
        pigs     = 0
        while capacity < buckets:
            # add one more pig
            capacity *= maxTests
            pigs     += 1

        return pigs
