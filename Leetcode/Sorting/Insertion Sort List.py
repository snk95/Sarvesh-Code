# https://leetcode.com/problems/insertion-sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

	def insertionSortList(self, head: ListNode) -> ListNode:

		dummy = ListNode(float('-inf'))
		nxt = head
		while nxt:
			node, nxt = nxt, nxt.next # get the node to insert, and update nxt
			node.next = None # cut the link between node and nxt
			# insert node
			cur = dummy
			while cur:
				if cur.next and cur.next.val <= node.val: # pass
					cur = cur.next
					continue
				else:
					node.next = cur.next
					cur.next = node
					break
		return dummy.next