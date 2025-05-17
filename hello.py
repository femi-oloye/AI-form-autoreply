class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
		
node1 = Node(8)
node2 = Node (9)
node3  = Node (2)

node1.next = node2
node2.next = node3

def traverse(head):
	current = head
	while current is not None:
		print (current.data)
		current = current.next

traverse(node1)



		

		
