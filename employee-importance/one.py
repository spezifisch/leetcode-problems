"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        importance = None
        for e in employees:
            if e.id == id:
                importance = e.importance
                importance += sum(
                    [self.getImportance(employees, sub_id) for sub_id in e.subordinates]
                )
                break

        return importance


# Runtime: 236 ms, faster than 28.87% of Python3 online submissions for Employee Importance.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Employee Importance.
