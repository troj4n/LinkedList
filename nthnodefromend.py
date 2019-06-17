# coding: utf-8
# Your code here!
#nth node from the end of linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        newNode=Node(new_data)
        newNode.next=self.head
        self.head=newNode
            
    def printList(self):
        temp=self.head
        while temp:
            print temp.data,"->",
            temp=temp.next
        print "Null"

def findnfromend(l,n):
    res=n
    if l.head is None:
        return
    temp=l.head
    nptr=l.head
    while n-1:
        if nptr is None:
            print "{} is greater than no og nodes in the list".format(res)
            return
        nptr=nptr.next
        n-=1
    while nptr.next:
        nptr=nptr.next
        temp=temp.next
    print temp.data
    #print nptr.data
l=LinkedList()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.push(4)
l.push(32)
l.push(76)
l.push(345)
l.printList()
n=12
findnfromend(l,n)
