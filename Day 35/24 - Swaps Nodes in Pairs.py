


class Node:
	def __init__(self, data=0):
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
		tail = prev = Node()
		tail.next = self.head
		while tail.next and tail.next.next:
			first = tail.next
			second = tail.next.next
			third = tail.next.next.next
			tail.next = second
			tail.next.next = first
			tail.next.next.next = third
			tail = first
		
		return prev.next


ll = LinkedList()
arr = [1, 2, 3, 4]
for i in arr:
	ll.push(i)
# new_val = LinkedList()
ll.disp()


new_val = ll.swaps()
while new_val:
	print(new_val.data, end=' ')
	new_val = new_val.next