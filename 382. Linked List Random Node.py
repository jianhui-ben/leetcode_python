# 382. Linked List Random Node
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
#
# Implement the Solution class:
#
# Solution(ListNode head) Initializes the object with the integer array nums.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur, i, out = self.head, 0, None
        while cur:
            i += 1
            if int(i * random()) == 0:
                out = cur.val
            cur = cur.next
        return out

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()