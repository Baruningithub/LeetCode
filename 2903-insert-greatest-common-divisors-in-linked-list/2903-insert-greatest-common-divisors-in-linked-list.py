# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None : return head

        curr = head
        while curr and curr.next:
            gcd = ListNode()
            gcd.val = math.gcd(curr.val, curr.next.val)

            gcd.next = curr.next
            curr.next = gcd

            curr = gcd.next
        
        return head
        