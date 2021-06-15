


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = new_node

	def disp(self):
		if self.head is None:
			print("Empty Nodes")
		curr = self.head
		while curr:
			print(curr.data, end = ' ')
			curr = curr.next
		print()

	def swaps(self):
		if self.head is None:
			print("None")
		curr = self.head
		while curr:
			i = 0
			while i<=1:
				prev = curr
				curr = curr.next
				i += 1
			print("1", curr.data, prev.data)
			curr = prev
			print("2",curr.data, prev.data)
			prev = curr
			curr = curr.next
			print(curr.data)


ll = LinkedList()
arr = [1, 2, 3, 4]
for i in arr:
	ll.push(i)

ll.disp()
ll.swaps()
ll.disp()