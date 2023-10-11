class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) <= 1:
            return False

        one = two = "?"
        for a, b in zip(s, goal):
            if a != b:
                if one == "?": # first mismatch
                    one = a
                    two = b
                else:
                    # second (or third) mismatch
                    if one != b or two != a:
                        return False
                    one = two = "!" # invalid characters so that third mismatch fails

        if one == "!":
            return True
        if one != "?":
            return False # one mismatch without a second mismatch

        # if no mismatch, then swap two identical characters
        return len(set(s)) < len(s)
