# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        dummyA = headA
        dummyB = headB
        while dummyA != dummyB:
            dummyA = headB if dummyA == None else dummyA.next
            dummyB = headA if dummyB == None else dummyB.next
        return dummyA
    # Treats None as a node, pointers can be None and meet at None on the second 
    # iteration if they are not found to intersect
