from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = defaultdict(lambda: 0)
        for line in cpdomains:
            count, domain = line.split(" ")
            count = int(count)
            
            parts = domain.split(".")
            for i in range(len(parts)):
                upper_domain = ".".join(parts[i:])
                visits[upper_domain] += count
            
        ret = []
        for name, visit_count in visits.items():
            ret.append(f"{visit_count} {name}")
        
        return ret
    
# Runtime: 60 ms, faster than 73.77% of Python3 online submissions for Subdomain Visit Count.
# Memory Usage: 13.2 MB, less than 7.07% of Python3 online submissions for Subdomain Visit Count.

