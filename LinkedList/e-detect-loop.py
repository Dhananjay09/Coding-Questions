class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head
        while slow and fast and slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
