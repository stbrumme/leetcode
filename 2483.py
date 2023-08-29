class Solution:
    def bestClosingTime(self, customers: str) -> int:
        people = customers.count("Y")
        customers += "N"

        noone   = 0
        missed  = people
        penalty = missed + noone
        result  = 0

        for i in range(len(customers)):
            if penalty > missed + noone:
                penalty = missed + noone
                result = i

            if customers[i] == "Y":
                missed -= 1
            else:
                noone  += 1

        return result
