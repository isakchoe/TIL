

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n_list = []

        while head != None:
            n_list.append(head.val)
            head = head.next

        n = len(n_list)
        k = k % n

        temp = n_list[-k:]
        result = temp + n_list[:-k]

        head = self.make_node(result)
        return head


    def make_node(self, arr):
        head = ListNode(arr[0])
        temp = head

        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return head

