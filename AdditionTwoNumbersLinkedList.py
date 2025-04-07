class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total //10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  

solution=Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = solution.addTwoNumbers(l1, l2)

while result:
    print(result.val, "\n")
    result = result.next