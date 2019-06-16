#This code has memory leak issues. Beacuse nodes are not deleted
#If anyone can fix this. please do
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
    temp=l.head
    nxt=l.head
    traverse=l.head
    while traverse is not None:
        if temp.data is nxt.data:
            while nxt.data is temp.data:
                nxt=nxt.next
            temp.next=nxt
        else:
            temp=temp.next
            nxt=nxt.next
        traverse=traverse.next

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