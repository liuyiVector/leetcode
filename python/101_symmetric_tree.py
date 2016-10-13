#! /usr/bin/python
# coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def equal(self, nodeA, nodeB):
        if (nodeA == None and nodeB != None) or (nodeA != None and nodeB == None):
            return False
        if (nodeA != None and nodeB != None) and (nodeA.val != nodeB.val):
            return False
        return True

    def symmetricArr(self, arrs):
        if arrs == None:
            return True
        size = len(arrs)
        for i in range(0,size):
            if not self.equal(arrs[i], arrs[size - 1 - i]):
                return False
        return True

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        nodes = []
        nodes.append(root)

        while len(nodes) > 0:
            size = len(nodes)
            tmp = nodes[0:size]
            if not self.symmetricArr(tmp):
                return False
            nodes = []
            for item in tmp:
                if item == None:
                    continue
                nodes.append(item.left)
                nodes.append(item.right)
        return True
        
    # TODO add recursive method
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
