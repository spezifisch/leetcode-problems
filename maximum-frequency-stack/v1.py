from sortedcontainers import SortedDict, SortedList
from dataclasses import dataclass


@dataclass
class FreqItem:
    count: int
    val: int
    push_sequence: list[int]


class FreqStack:
    def __init__(self):
        self.seq = 0
        self.items: dict[int, FreqItem] = {}
        self.counts = SortedDict()

    def _add_counts_item(self, item: FreqItem) -> None:
        count_items = self.counts.get(item.count)
        if count_items is not None:
            count_items.add(item)
        else:
            self.counts[item.count] = SortedList(
                [item], key=lambda x: x.push_sequence[-1]
            )

    def push(self, val: int) -> None:
        item = self.items.get(val)
        if not item:
            # create item
            item = FreqItem(count=1, val=val, push_sequence=[self.seq])
            self.items[val] = item
        else:
            if item.count != 0:
                # remove from old count list
                self.counts[item.count].remove(item)

            item.count += 1
            item.push_sequence.append(self.seq)

        self._add_counts_item(item)
        self.seq += 1

    def pop(self) -> int:
        most_counts = self.counts.values()[-1]
        latest_item = most_counts.pop()
        if not most_counts:
            del self.counts[latest_item.count]

        latest_item.count -= 1
        latest_item.push_sequence.pop()
        val = latest_item.val

        if latest_item.count > 0:
            self._add_counts_item(latest_item)

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Runtime: 1050 ms, faster than 5.04% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 26.4 MB, less than 6.49% of Python3 online submissions for Maximum Frequency Stack.
