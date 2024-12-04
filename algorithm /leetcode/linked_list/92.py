

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        answer = []

        while head is not None:
            answer.append(head.val)
            head = head.next

        temp = answer[left-1: right]
        temp.reverse() # reverse, sort(reverse = True) 전혀 다름..  역순 vs 내림차순 정렬임...

        result = answer[:left-1] + temp + answer[right:]

        return self.make_node(result)

    def make_node(self, node_list):

        head = ListNode(node_list[0])
        temp = head

        for i in range(1, len(node_list)):
            temp.next = ListNode(node_list[i])
            temp = temp.next

        return head

a = Solution()
head = [1, 2, 3, 4, 5]
left = 2
right = 4
print(a.reverseBetween(head, left, right))