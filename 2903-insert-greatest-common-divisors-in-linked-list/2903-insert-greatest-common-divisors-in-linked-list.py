# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None : return head

        dummy = head
        while head.next != None:
            curr = head

            gcd = ListNode()
            gcd.val = math.gcd(curr.val, curr.next.val)

            gcd.next = curr.next
            curr.next = gcd

            head = head.next.next
        
        return dummy
        