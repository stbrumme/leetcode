class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # (1) It has at least 8 characters.
        if len(password) < 8:
            return False

        rule2 = False # (2) It contains at least one lowercase letter.
        rule3 = False # (3) It contains at least one uppercase letter.
        rule4 = False # (4) It contains at least one digit.
        rule5 = False # (5) It contains at least one special character.
                      #     The special characters are the characters in the following string:
                      #     "!@#$%^&*()-+"
                      # (6) It does not contain 2 of the same character in adjacent positions
                      #     (i.e., "aab" violates this condition, but "aba" does not).
        last  = ""
        for c in password:
            if   "a" <= c <= "z":
                rule2 = True
            elif "A" <= c <= "Z":
                rule3 = True
            elif "0" <= c <= "9":
                rule4 = True
            elif c in "!@#$%^&*()-+":
                rule5 = True

            if c == last:
                return False
            last = c

        return rule2 and rule3 and rule4 and rule5
