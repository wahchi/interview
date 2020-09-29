# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        if head.next is None:
            return head
        
        # seperate 
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        
        return self.mergeTwoList(self.sortList(head), self.sortList(fast))

    def mergeTwoList(self, first: ListNode, second: ListNode) -> ListNode:
        # merge two list node
        if first and second:
            if first.val > second.val:
                second.next = self.mergeTwoList(first, second.next)
                return second
            else:
                first.next = self.mergeTwoList(first.next, second)
                return first
        else:
            if first is None:
                return second
            else:
                return first
