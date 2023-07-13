class Solution:
    def detectCycle(self, head):
        if not head:
            return
        if not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def remove_cycle(self, head):
        starting_index = self.detectCycle(head)
        if not starting_index:
            return
        starting_index.next = None
        return head

    def maxProduct(self, nums):
        maxi = INT_MIN;
        prod = 1;
