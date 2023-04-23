class Solution:
    def getIntersectionNode(self, headA, headB):
        flen = 0
        temp = headA
        while temp:
            flen += 1
            temp = temp.next
        slen = 0
        temp = headB
        while temp:
            slen += 1
            temp = temp.next
        if flen > slen:
            ans = flen - slen
            while ans > 0:
                headA = headA.next
                ans -= 1
        else:
            ans = slen - flen
            while ans > 0:
                headB = headB.next
                ans -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return
