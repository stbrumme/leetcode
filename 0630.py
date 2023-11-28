class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by lastday
        ordered = [ ( lastday, duration ) for duration, lastday in courses ]
        ordered.sort()

        # remove impossible courses
        while ordered and ordered[0][0] < ordered[0][1]:
            ordered.pop(0)

        # attended courses
        taken = [] # max-heap

        now = 0
        for lastday, duration in ordered:
            # try attending the course
            heappush(taken, -duration)
            now += duration
            while taken and now > lastday:
                # remove longest courses (can be the current course !)
                longest = -heappop(taken) # max-heap
                now    -= longest

        return len(taken)
