class Node:
    def __init__(self,data = None , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node

    def printt(self):
        if self.head is None:
            print("Linked List Is Empty")

        ele = self.head

        while ele:
            print(ele.data,"---->",end=" ")
            ele = ele.next
        print()

    def insert_at_end(self,data):
        npode = Node(data,None)
        if self.head == None:
            self.head = npode
            return
        ele = self.head

        while ele.next:

            ele = ele.next
        
        ele.next = npode

    def insert_values(self,data_list):
        if not data_list :
            print("Data List Is Empty")
            return
        for element in data_list:
            self.insert_at_begin(element)

    def get_length(self):
        if self.head == None :
            print('List is Empty')

        ele = self.head
        count = 0 
        while ele:
            count+=1
            ele = ele.next
        print(f'Count is : {count}')
        return count
        

    def value_at_middle(self,data,index):
        if self.head is None and index > 0 :
            print("List in Empty")
            self.insert_at_begin(data)
            return
        ele = self.head
        count = 0 
        while ele:
            
            if count == index-1:
                # print('dsfsdf')
                node = Node(data,ele.next)
                ele.next = node
                return
            ele = ele.next
            count+=1
            
    def at_remove(self,index):
        if self.head == None or index < 0 or index > self.get_length():
            raise Exception("Empty")
        ele = self.head
        count = 0
        while ele:
            if count == index-1 :
                ele.next = ele.next.next
                return

            ele = ele.next
            count += 1 
    def insert_after_value(self,data_after,data_to_insert ):
        if self.head == None :
            raise Exception("Empty")

        ele = self.head

        while ele:
            if data_after == ele.data:
                node = Node(data_to_insert,ele.next)
                ele.next = node
                return

            ele = ele.next

    def remove_by_value(self,data):
        if self.head == None :
            raise Exception("Empty")

        ele = self.head

        while ele:
            if data == ele.next.data:
                ele.next = ele.next.next
                return

            ele = ele.next
if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_begin(6)
    obj.insert_at_begin(8)
    obj.insert_at_end(5)
    obj.insert_values(['jaggi','shah'])
    obj.get_length()
    obj.value_at_middle(3,2)
    obj.insert_after_value('jaggi','chal_paya')
    obj.remove_by_value(8)
    # obj.at_remove(2)
    obj.printt()