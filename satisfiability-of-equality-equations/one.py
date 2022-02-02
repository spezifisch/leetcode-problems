class Group:
    def __init__(self, _id: int, eq_elem: int):
        self.id = _id
        self.equal = set(eq_elem)
        self.unequal = set()

class Solution:
    def getGroup(self, op: str):
        for g in self.groups:
            if op in g.equal:
                return g
            
        return None
    
    def equationsPossible(self, equations: List[str]) -> bool:
        self.next_gid = 0
        self.groups = []
        
        for eq in equations:
            lop = eq[0]
            rop = eq[3]
            equals = eq[1] == "="
            
            if lop == rop:
                if not equals:
                    return False                
                continue
            
            g_lop = self.getGroup(lop)
            g_rop = self.getGroup(rop)
            
            if g_lop is None:
                g_lop = Group(self.next_gid, lop)
                self.groups.append(g_lop)
                self.next_gid += 1
                
                if g_rop is not None:
                    # make sure the newly created group is g_rop
                    g_lop, g_rop = g_rop, g_lop
                
            if g_rop is None:
                g_rop = Group(self.next_gid, rop)
                self.groups.append(g_rop)
                self.next_gid += 1
            
            if equals:
                if g_lop == g_rop:
                    pass
                elif g_lop.id in g_rop.unequal or g_rop.id in g_lop.unequal:
                    return False
                else:
                    # merge
                    g_lop.equal |= g_rop.equal
                    g_lop.unequal |= g_rop.unequal
                    g_rop.equal = None
                    g_rop.unequal = None
                    self.groups.remove(g_rop)

                    for g in self.groups:
                        if g.id == g_lop.id or g.id == g_rop.id:
                            continue

                        if g_rop.id in g.equal:
                            g.equal.add(g_rop.id)
                        if g_rop.id in g.unequal:
                            g.unequal.add(g_rop.id)
            else:
                # unequal
                if g_lop == g_rop:
                    return False
                elif g_lop.id in g_rop.equal or g_rop.id in g_lop.equal:
                    return False
                else:
                    g_lop.unequal.add(g_rop.id)
                    g_rop.unequal.add(g_lop.id)
                    
        return True
    
# Runtime: 68 ms, faster than 6.68% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Satisfiability of Equality Equations.

