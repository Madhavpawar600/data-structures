class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=None

    def atfront(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def atend(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node

        else:
            temp=self.head

            while temp.next:
                temp=temp.next
            temp.next=new_node

    def atpos(self,data,num):
        new_node=node(data)

        if num==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        l=0
        while temp:
            if l<num:
                prev=temp
                temp=temp.next
                l+=1
            else:
                break
        prev.next=new_node
        new_node.next=temp

    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=' ')
            temp=temp.next

    def search(self,ele):
        temp=self.head
        count=0
        while temp:
            if ele == temp.data:
                print('found at position',count)
                
                break
            else:
                pass
            count+=1
            temp=temp.next

            

c1=linkedlist()
c1.atfront(4)
c1.atfront(3)
c1.atfront(2)
c1.atend(7)
c1.atend(8)
c1.display()
c1.atpos(5,3)
c1.atpos(6,4)
c1.display()
c1.search(7)
