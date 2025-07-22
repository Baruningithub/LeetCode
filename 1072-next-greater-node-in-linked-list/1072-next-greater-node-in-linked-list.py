class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        result = [0] * len(values)
        stack = []  # will store indices
        
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                idx = stack.pop()
                result[idx] = val
            stack.append(i)
        
        return result
