class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if(l1 is None or l2 is None):
            return l1 or l2
        sorted = ListNode(0)
        dummy = sorted
        while(l1 is not None and l2 is not None):
            if(l1.val <  l2.val):
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if(l1 is None):
            dummy.next = l2
        elif(l2 is None):
            dummy.next = l1
        
        return sorted.next
