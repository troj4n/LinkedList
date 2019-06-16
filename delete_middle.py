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
def find_middle(l):
    slow_ptr=l.head
    fast_ptr=l.head
    if l.head is not None:
        while fast_ptr is not None and fast_ptr.next is not None :
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        return slow_ptr.data
    return None

def deletemiddle(l,mid):
    if l.head is None:
        return
    tmp=l.head
    while tmp.next.data!=mid:
        tmp=tmp.next
    ne=tmp.next.next
    tmp.next=None
    tmp.next=ne
    #tmp.next = tmp.next.next
    #tmp.next = None


l=LinkedList()
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.printlist()
m=find_middle(l)
deletemiddle(l,m)
l.printlist()