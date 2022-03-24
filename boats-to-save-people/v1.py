class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        a = 0
        b = len(people) - 1
        while a < b:
            if people[a] + people[b] > limit:
                b -= 1
            else:
                b -= 1
                a += 1

            boats += 1

        if a == b:
            boats += 1

        return boats


# Runtime: 687 ms, faster than 33.46% of Python3 online submissions for Boats to Save People.
# Memory Usage: 20.9 MB, less than 34.38% of Python3 online submissions for Boats to Save People.
