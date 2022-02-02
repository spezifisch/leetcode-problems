class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list(set(list1) & set(list2))

        places1 = {place: idx for idx, place in enumerate(list1)}
        places2 = {place: idx for idx, place in enumerate(list2)}

        min_index_sum = None
        min_places = []

        for place in common:
            index_sum = places1[place] + places2[place]
            if min_index_sum is None or index_sum < min_index_sum:
                min_places = [place]
                min_index_sum = index_sum
            elif index_sum == min_index_sum:
                min_places.append(place)

        return min_places


# Runtime: 68 ms, faster than 81.97% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 13.5 MB, less than 6.35% of Python3 online submissions for Minimum Index Sum of Two Lists.
