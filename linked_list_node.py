# This shows the logic of how items in a list are linked
# Next step would be building a two way linked list - has a next AND previous node
# Then building a binary linked list, where one node has two next_nodes
class Node():
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def add(self, node):
		self.next_node = node


def create_and_link(num_of_nodes):
	first_node = Node(0)
	last_node = first_node

	for i in range(1, num_of_nodes):
		temp = Node(i)
		last_node.add(temp)
		last_node = temp

		# return first_node

	node = first_node

	while node:
		print (node.data)
		node = node.next_node

create_and_link(5)		



