package v1

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type MyNode struct {
	Node *ListNode
	Next *MyNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	var reverseA *MyNode
	var reverseB *MyNode
	nodeA := headA
	nodeB := headB
	for nodeA != nil || nodeB != nil {
		if nodeA != nil {
			reverseA = &MyNode{
				Node: nodeA,
				Next: reverseA,
			}

			nodeA = nodeA.Next
		}
		if nodeB != nil {
			reverseB = &MyNode{
				Node: nodeB,
				Next: reverseB,
			}

			nodeB = nodeB.Next
		}
	}

	var sameUntil *ListNode
	for reverseA != nil && reverseB != nil {
		if reverseA.Node != reverseB.Node {
			return sameUntil
		}
		sameUntil = reverseA.Node

		reverseA = reverseA.Next
		reverseB = reverseB.Next
	}
	return sameUntil
}

// Runtime: 59 ms, faster than 21.46% of Go online submissions for Intersection of Two Linked Lists.
// Memory Usage: 7.8 MB, less than 21.80% of Go online submissions for Intersection of Two Linked Lists.
