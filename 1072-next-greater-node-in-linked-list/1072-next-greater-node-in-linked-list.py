class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []

        current = head
        while current:
            next_node = current.next
            found = 0
            
            while next_node:
                if next_node.val > current.val:
                    found = next_node.val
                    break
                next_node = next_node.next

            ans.append(found)
            current = current.next

        return ans
