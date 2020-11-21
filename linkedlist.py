class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0

    def push(self, val):
        """
        inserts the node after the current one!
        if current node not exist, creates the head!
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.length += 1
            return
        else:
            head = self.head 
            tail = head
            while(tail.next is not None):
                tail = tail.next
            tail.next = newNode
        self.length += 1 
    
    def display_list(self):
        """
        prints the list!
        """
        start = self.head
        tail = start
        try:
            while(tail.next is not None):
                print(tail.val)
                tail = tail.next
        except expression as identifier:
            print(e)
                
            

    def unshift(self, val):
        """
        pushes the new node at the begining of the list!
        """
        newNode = Node(val)
        if(self.head is None):
            self.head = newNode
            return 
        else:
            newNode.next = self.head 
            self.head = newNode
        self.length += 1

    def countNodes(self):
        """
        returns the no. of nodes!
        """
        print(self.length)

     
            

ll = LinkedList()
ll.push("I ")
ll.push("am ")
ll.push("the Best! ")
ll.unshift("who is the Best? ")
ll.display_list()
ll.countNodes()