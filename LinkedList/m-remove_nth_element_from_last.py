class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        if n == 1 and not head.next:
            return None
        while fast and n > 0:
            fast = fast.next
            n -= 1
        pre = None
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        if not slow:
            return None
        if not slow.next:
            pre.next = None
        if pre:
            pre.next = slow.next
            return head
        else:
            return head.next
