# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 9 of DAY 100
# LeetCode - 02 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        curr = self.head
        if curr == None:
            print("None")
        else:
            while curr:
                print(curr.data, end = ' -> ')
                curr = curr.next
            print("NULL", end='\n')

    def solve(self, l1, l2):
        curr1 = l1.head
        curr2 = l2.head
        carry = 0
        while curr1 is not None:
            s = str(curr1.data + curr2.data)
            temp = '0'
            if len(s) == 2:
                temp = s[0]
                s = s.replace(s[0], '')
                print(temp, s)
            self.add(int(s)+int(carry))
            carry = int(temp)
            curr1 = curr1.next
            curr2 = curr2.next


arr1 = [2,4,3]
arr2 = [5,6,4]

l1 = LL()           #LinkedList 1
for i in arr1:
    l1.add(i)

l2 = LL()           #LinkedList 2
for i in arr2:
    l2.add(i)
l3 = LL()
l3.solve(l1, l2)
l3.display()






'''
# ________________________________________________________
# LeetCode solution style:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
'''