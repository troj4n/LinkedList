# coding: utf-8
# Your code here!
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 


# Constructor to initialize the node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	def deleteList(self): 
		
		# initialize the current node 
		current = self.head 
		while current: 
			prev = current.next # move next node 
			
			# delete the current node 
			del current.data 
			
			# set current equals prev node 
			current = prev 

	# push function to add node in front of llist 
	def push(self, new_data): 

		# Allocate the Node & 
		# Put in the data 
		new_node = Node(new_data) 
		
		# Make next of new Node as head 
		new_node.next = self.head 
		
		# Move the head to point to new Node 
		self.head = new_node 
	def printll(self):
		curr=self.head
		while curr:
			print (curr.data),
			curr=curr.next
		print ("Null")
# Use push() to construct below 
# list 1-> 12-> 1-> 4-> 1 
if __name__ == '__main__': 

	llist = LinkedList() 
	llist.push(1) 
	llist.push(4) 
	llist.push(1) 
	llist.push(12) 
	llist.push(1) 

	llist.printll()
	print("Deleting linked list") 
	llist.deleteList() 
	
	print("Linked list deleted") 
