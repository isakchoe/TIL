
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.dfs(head, 0)

        if length == n:
            head = head.next
            return head

        target_index = length - n -1
        self.dfs_update(head, 0, target_index)
        return head

    def dfs(self, head, depth):
        if head is None:
            return depth
        return self.dfs(head.next, depth+1)

    def dfs_update(self,head, now_index, target_index):
        if now_index == target_index:
            head.next = head.next.next
            return
        self.dfs_update(head.next, now_index+1, target_index)