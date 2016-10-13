#! /usr/bin/python
# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 每次fast的指针走两步，如果有循环fast指针肯定先在环里，当slow进入环后，可以看成fast在追赶slow，肯定会追上的
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head
        while True:
            slow = slow.next
            if slow == None:
                return False
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next

            if fast == None:
                return False

            if slow == fast:
                return True
        return False
