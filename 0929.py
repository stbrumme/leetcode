class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def filter(mail):
            # regex could be used, too

            # dots
            pos = mail.find(".")
            while pos < mail.find("@"):
                mail = mail[:pos] + mail[pos+1:]
                pos = mail.find(".")

            # plus
            pos = mail.find("+")
            at  = mail.find("@")
            if pos != -1 and pos < at:
                mail = mail[:pos] + mail[at:]

            return mail

        return len(set(filter(m) for m in emails))
