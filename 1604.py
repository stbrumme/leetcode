class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # one hour alert, measured in minutes
        threshold = 60

        # split into names
        all = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            # convert HH:MM to minutes since midnight
            a, b = t.split(":")
            minutes = int(a) * 60 + int(b)
            all[n].append(minutes)

        # and sort
        for user in sorted(all):
            one = two = -inf
            for three in sorted(all[user]):
                if three - one <= 60:
                    yield user
                    break

                one = two
                two = three
