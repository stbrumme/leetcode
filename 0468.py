import socket
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # use built-in IP parser
        try:
            # IPv4
            socket.inet_pton(socket.AF_INET, queryIP)
            return "IPv4"
        except socket.error:
            pass

        try:
            # IPv6
            socket.inet_pton(socket.AF_INET6, queryIP)
            if queryIP.count("::") == 0: # weird extra-condition of this problem
                return "IPv6"
        except socket.error:
            pass

        return "Neither"
