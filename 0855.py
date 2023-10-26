class ExamRoom:
    def __init__(self, n: int):
        self.last  = n - 1 # right-most seat
        self.used  = 0
        self.seats = [ ]

    def seat(self) -> int:
        # empty room / first student
        if self.used == 0:
            self.used  = 1
            self.seats = [ 0 ]
            return 0

        # consider sitting at the left end
        distance = self.seats[0]
        result   = 0
        # loop through all occupied seats and check their distance
        for i in range(1, len(self.seats)):
            left  = self.seats[i - 1]
            right = self.seats[i]
            if left + 1 == right:
                continue # no free seat inbetween

            current = (right - left) // 2
            if distance < current:
                distance = current
                result  = (right + left) // 2 # round down ("seat with the lowest number")

        # consider sitting at the right end
        current = self.last - self.seats[-1]
        if distance < current:
            result = self.last

        self.used += 1
        insort(self.seats, result) # add to sorted list
        return result

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        self.used -= 1
