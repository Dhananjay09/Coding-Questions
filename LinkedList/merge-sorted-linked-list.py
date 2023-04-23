class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            self.merge(list2, list1)
            return list2
        self.merge(list1, list2)
        return list1

    def merge(self, first, second):
        while first and second:
            if first.next:
                if first.next.val > second.val:
                    temp = first.next
                    first.next = second
                    second = second.next
                    first = first.next
                    first.next = temp
                else:
                    first = first.next
            else:
                first.next = second
                break
