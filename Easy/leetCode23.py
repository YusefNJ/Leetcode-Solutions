# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while (len(lists) > 1):
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList

        return lists[0]
    
    def mergeLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #implement later
        fake = ListNode()
        pointer = fake

        while list1 and list2:
            if(list1.val < list2.val):
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        
        return fake.next