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

def clone(l):
    new_list=LinkedList()
    new_list.head=l.head
    tmp=new_list.head
    curr=l.head
    while curr:
        tmp.next=curr.next
        curr=curr.next
        tmp=tmp.next
    return new_list
l=LinkedList()
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.printlist()
x=clone(l)
x.printlist()

print id(l)
print id(x)
