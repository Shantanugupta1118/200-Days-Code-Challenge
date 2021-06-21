# Github: Shantanugupta1118
# DAY 41 of DAY 100

class Node:
    def __init__(self, data=0) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push_node(self, val: int) ->Node:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def disp(self) -> None:
        if self.head is None:
            return None
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def remove_duplicacy(self):
        if self.head is None:
            return None
        curr = self.head
        while curr:
            prev, curr = curr, curr.next
            if curr is not None and prev.data == curr.data:
                prev.next = curr.next
                curr = prev
            

ll = LinkedList()
arr = [1,1,2,3,5,5,6,9,10,11,11,11,11,11,11,12,15,20,21,21,21]
for i in arr:
    ll.push_node(i)
ll.disp()
ll.remove_duplicacy()
ll.disp()