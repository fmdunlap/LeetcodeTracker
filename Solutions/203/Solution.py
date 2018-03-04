class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        newHead = head
        while newHead is not None and newHead.val is val:
            newHead = newHead.next
        
        if newHead is not None:
            prev = newHead
            curr = newHead.next

            while curr is not None:
                if curr.val is val:
                    prev.next = curr.next
                    curr = prev.next
                else:
                    prev = curr
                    curr = curr.next
        
        return newHead