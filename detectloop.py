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
#hare and tortoise algorithm (Floyd's cycl detection algorithm)
def detect_loop(l):
    hare=l.head
    turtle=l.head
    while turtle and hare and hare.next:
        turtle=turtle.next
        hare=hare.next.next
        if turtle == hare:
            return True
        
    return False
    
        
l=LinkedList()
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.head.next.next.next.next.next.next=l.head.next.next
if detect_loop(l):
    print "There is a loop"
else:
    print "No Loop"
