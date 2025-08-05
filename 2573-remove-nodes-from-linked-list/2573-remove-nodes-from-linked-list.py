# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        # Add node to stack (not values)
        while head:
            stack.append(head)
            head = head.next

        curr = stack.pop()
        maximum = curr.val
        ans = ListNode(maximum)

        while stack:
            curr = stack.pop()

            if curr.val < maximum:
                continue

            else:
                new_node = ListNode(curr.val)
                new_node.next = ans
                ans = new_node
                maximum = curr.val

        return ans