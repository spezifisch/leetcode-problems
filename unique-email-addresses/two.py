class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addrs = dict()
        
        for mail in emails:
            user, domain = mail.split('@', 1)
            if '+' in user:
                user, _ = user.split('+', 1)
            
            user = user.replace('.', '')
            addr = user + '@' + domain
            addrs[addr] = True
            
        return len(addrs)
    
# Runtime: 48 ms, faster than 80.57% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.3 MB, less than 5.79% of Python3 online submissions for Unique Email Addresses.

