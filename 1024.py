class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        impossible = 9999

        clips.sort()

        @cache
        def deeper(pos):
            if pos >= time:     # done
                return 0

            best = impossible
            for start, end in clips:
                if start > pos: # gap
                    break

                if end   > pos: # stitch
                    best = min(best, 1 + deeper(end))

            return best

        return -1 if deeper(0) == impossible else deeper(0)
