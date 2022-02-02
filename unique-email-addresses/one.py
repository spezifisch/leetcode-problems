class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addrs = set()

        for mail in emails:
            user, domain = mail.split("@", 1)
            if "+" in user:
                user, _ = user.split("+", 1)

            user = user.replace(".", "")
            addr = user + "@" + domain
            addrs.add(addr)

        return len(addrs)


# Runtime: 52 ms, faster than 58.43% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.2 MB, less than 5.79% of Python3 online submissions for Unique Email Addresses.
