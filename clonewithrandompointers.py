# coding: utf-8
# Your code here!
class Node: 
    '''Structure of linked list node'''
  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.random = None
  
def clone(original_root): 
    curr = original_root 
    while curr != None: 
        new = Node(curr.data) 
        new.next = curr.next
        curr.next = new 
        curr = curr.next.next
    curr = original_root 
    while curr != None: 
        curr.next.random = curr.random.next
        curr = curr.next.next
    curr = original_root 
    dup_root = original_root.next
    while curr.next != None: 
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp 
    return dup_root 
  
def print_dlist(root): 
    '''Function to print the doubly linked list'''
  
    curr = root 
    while curr != None: 
        print('Data =', curr.data, ', Random =', curr.random.data) 
        curr = curr.next

original_list = Node(1) 
original_list.next = Node(2) 
original_list.next.next = Node(3) 
original_list.next.next.next = Node(4) 
original_list.next.next.next.next = Node(5) 
  

original_list.random = original_list.next.next

original_list.next.random = original_list 

original_list.next.next.random = original_list.next.next.next.next

original_list.next.next.next.random = original_list.next.next.next.next

original_list.next.next.next.next.random = original_list.next
  

print('Original list:') 
print_dlist(original_list) 
  

cloned_list = clone(original_list) 
  

print('\nCloned list:') 
print_dlist(cloned_list) 
  
