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
