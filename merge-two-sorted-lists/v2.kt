/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    var head: ListNode? = null
    var node: ListNode? = null

    fun setNextNode(next: ListNode?) {
        if (head == null) {
            head = next
        }
        node?.next = next
        node = next
    }

    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var a = list1
        var b = list2

        while (a != null || b != null) {
            if (a != null && b != null) {
                if (a.`val` < b.`val`) {
                    setNextNode(a)
                    a = a.next
                } else {
                    setNextNode(b)
                    b = b.next
                }
            } else if (a != null) {
                setNextNode(a)
                a = a.next
            } else if (b != null) {
                setNextNode(b)
                b = b.next
            }
        }

        node?.next = null
        return head
    }
}

// Runtime: 290 ms, faster than 34.25% of Kotlin online submissions for Merge Two Sorted Lists.
// Memory Usage: 36.2 MB, less than 29.80% of Kotlin online submissions for Merge Two Sorted Lists.
