class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        round = 0
        answer = head
        while True:
            val1 = l1.val
            val2 = l2.val

            temp = val1 + val2 + round

            if temp >= 10:
                temp -= 10
                round = 1
            else:
                round = 0

            # answer setting
            answer.val = temp

            # next step
            if l1.next == None and l2.next == None and round == 0:
                break

            answer.next = ListNode()

            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = 0

            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0
            answer = answer.next
        return head