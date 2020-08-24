# Understand
# Given two linked list represent two numbers
# where each node contains a single digit
# in reverse order
# add the two numbers and return the result as a linked list

# Plan

# create two arrays to hold the digits in the linked list
# traverse the linked lists appending each digit into the respective array
# reverse the list and join the number
# cast the strings to ints and add them together
# cast the result as a string
# split the string
# reverse the list
# create a new linked list
# add the elements from the list ot the linked list
# return the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def add_two_number(l1: ListNode, l2: ListNode) -> ListNode:
#     # create two arrays to hold the digits in the linked list
#     l1digits = []
#     l2digits = []
#     # traverse the linked lists appending each digit into the respective array
#     current = l1
#     while current is not None:
#         l1digits.append(current.val)
#         current = current.next
#     current = l2
#     while current is not None:
#         l2digits.append(current.val)
#         current = current.next
#     # reverse the lists 
#     l2digits = l2digits[::-1]
#     l1digits = l1digits[::-1]
#     # Join the numbers and cast it as an int
#     l1num = int("".join(l1digits))
#     l2num = int("".join(l2digits))

#     #get the sum and convert it to a string
#     total = str(l1num + l2num)

#     # split the string
#     totalarr = total.split()
#     # reverse the list
#     totalarr = totalarr[::-1]
#     # create a new linked list with the elements in the list
#     # we need the first node to be named so we can return it when we finish
#     l3 = ListNode(val=totalarr[0], next=totalarr[1])
#     #loop through the list
#     for i in range(len(totalarr)- 1):
#         if i == 0:
#             continue
#         if i == len(totalarr) - 1:
#             newNode = ListNode(totalarr[i], None)
#         newNode = ListNode(totalarr[i], totalarr[i + 1])
#     # return the head of the new linked list
#     return l3

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1digits = []
        l2digits = []
        # traverse the linked lists appending each digit into the respective array
        current = l1
        while current is not None:
            l1digits.append(str(current.val))
            current = current.next
        current = l2
        while current is not None:
            l2digits.append(str(current.val))
            current = current.next
        # reverse the lists 
        l2digits = l2digits[::-1]
        l1digits = l1digits[::-1]
        # Join the numbers and cast it as an int
        l1num = int("".join(l1digits))
        l2num = int("".join(l2digits))

        #get the sum and convert it to a string
        total = str(l1num + l2num)

        # split the string
        totalarr = list(total)
        # reverse the list
        totalarr = totalarr[::-1]
        # create a new linked list with the elements in the list
        # we need the first node to be named so we can return it when we finish
        # l3 = ListNode(int(totalarr[0]), None)
        l3 = None
        #loop through the list
        # for i in range(len(totalarr)- 1):
        #     if i == 0:
        #         continue
        #     elif i == len(totalarr) - 1:
        #         newNode = ListNode(int(totalarr[i]), None)
        #     else:
        #         newNode = ListNode(int(totalarr[i]), int(totalarr[i + 1]))
        for i in reversed(range(len(totalarr))):
            Node = ListNode(int(totalarr[i]))
            if l3 is None:
                l3 = Node
            else:
                prev_head = l3
                l3 = Node
                l3.next = prev_head
        # return the head of the new linked list
        return l3





