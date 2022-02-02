from math import ceil
from itertools import count


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        self.weights = weights
        self.D = D

        if D == 0:
            return 0

        min_capacity = ceil(sum(weights) / D)
        max_weight = max(weights)
        if max_weight == 0:
            return 0

        if min_capacity < max_weight:
            min_capacity = max_weight

        for capacity in count(min_capacity):
            if self.is_shippable(capacity):
                return capacity

        return -1

    def is_shippable(self, capacity: int) -> bool:
        ship_weight = 0
        days = 1

        for weight in self.weights:
            ship_weight += weight
            if ship_weight > capacity:
                days += 1
                ship_weight = weight

            if days > self.D:
                return False

        return True
