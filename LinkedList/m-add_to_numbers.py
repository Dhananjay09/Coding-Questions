class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        temp = l1
        carry = 0
        while l1 and l2:
            if (l1.val+l2.val+carry) > 9:
                l1.val = l1.val+l2.val+carry - 10
                carry = 1
            else:
                l1.val = l1.val+l2.val+carry
                carry = 0
            l1 = l1.next
            l2 = l2.next
        return temp


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

Solution().addTwoNumbers(l1, l2)
