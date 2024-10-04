# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        l3_pointer = None
        l3_divisor = 0

        while True:
            l1_value = 0
            l2_value = 0

            if l1 is not None:
                l1_value = l1.val
                l1 = l1.next
            if l2 is not None:
                l2_value = l2.val
                l2 = l2.next
            
            sum_val = l1_value + l2_value + l3_divisor
            l3_value = sum_val % 10
            l3_divisor = sum_val // 10

            if l3 is None:
                l3 = ListNode(l3_value)
                l3_pointer = l3
            else:
                l3_pointer.next = ListNode(l3_value)
                l3_pointer = l3_pointer.next
            
            if l1 is None and l2 is None:
                if l3_divisor != 0:
                    l3_pointer.next = ListNode(l3_divisor)
                
                break


        return l3