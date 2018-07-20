class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def reverse(self):

        prev=None
        count=0
        temp=self.head
        while temp is not None:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
            count+=1
        self.head=prev
        print( count)

    def pprint(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
li=linkedlist()
li.add(20)
li.add(4)
li.add(15)
li.add(85)
li.add(528)
li.add(90)

li.pprint()
li.reverse()
li.pprint()
        
