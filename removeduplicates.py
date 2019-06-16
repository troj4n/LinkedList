class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def push(self,newnode):
        newNode=Node(newnode)
        newNode.next=self.head
        self.head=newNode
    def printlist(self):
        temp=self.head
        while temp:
            print temp.data,"->",
            temp=temp.next
        print "Null"

def removeDuplicates(l):
    temp = l.head
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next

l=LinkedList()
l.push(64)
l.push(4)
l.push(4)
l.push(3)
l.push(3)
l.push(1)
l.push(1)
l.printlist()

removeDuplicates(l)
l.printlist()