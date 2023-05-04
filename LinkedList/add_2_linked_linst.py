class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        temp = l1
        carry = 0
        t1 = l1
        t2 = l2
        while t1 and t2:
            t1 = t1.next
            t2 = t2.next
        if t2:
            temp = l2
            l1, l2 = l2, l1
        pre = l1
        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            if (first + second + carry) > 9:
                l1.val = first + second + carry - 10
                carry = 1
            else:
                l1.val = first + second + carry
                carry = 0
            pre = l1
            l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            pre.next = ListNode(1)
        return temp
