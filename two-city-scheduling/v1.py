class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: -abs(c[1] - c[0]))
        total_cost = 0
        count_a = 0
        count_b = 0
        limit = len(costs) // 2

        for c in costs:
            if count_a >= limit:
                count_b += 1
                total_cost += c[1]
            elif count_b >= limit:
                count_a += 1
                total_cost += c[0]
            elif c[0] < c[1]:
                count_a += 1
                total_cost += c[0]
            else:
                count_b += 1
                total_cost += c[1]

        assert count_a == count_b
        assert count_a == limit
        return total_cost


# Runtime: 57 ms, faster than 54.44% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.9 MB, less than 82.59% of Python3 online submissions for Two City Scheduling.
