class Person():
    nextPerson = None #Person()
    name = None #string
    seatNumber = None #int

    def __init__(self,name, seatNumber):
        self.name = name
        self.seatNumber = seatNumber

class LinkedList:
    head = None # Person()

    ''' Add new person at the end of the list '''
    def append(self, person):
        if self.head == None:
            self.head = person
            return 
        
        currentPerson = self.head
        while currentPerson.nextPerson != None:
            currentPerson = currentPerson.nextPerson
        
        currentPerson.nextPerson = person
    ''' Add new person at the beginning of the list '''
    def prepend(self,person):
        if self.head == None:
            self.head = person
            return
        
        newHead = person
        newHead.nextPerson = self.head
        self.head = newHead
    
    '''Delete Person by Name'''
    def deletePerson(self,name):
        if self.head == None: return

        if self.head.name == name:
            self.head = self.head.nextPerson
            return
        
        currentPerson = self.head
        while currentPerson.nextPerson != None:
            if currentPerson.nextPerson.name == name:
                currentPerson.nextPerson = currentPerson.nextPerson.nextPerson
                return
            currentPerson = currentPerson.nextPerson

    ''' Find person by name '''
    def findPerson(self,name):
        if self.head == None: return

        if self.head.name == name:
            return self.head

        currentPerson = self.head
        while currentPerson.nextPerson != None:
            if currentPerson.nextPerson.name == name:
                return currentPerson.nextPerson
            
            currentPerson = currentPerson.nextPerson
    
    ''' Print all elements in the list '''
    def printList(self):
        if self.head == None: print("The list is empty")

        currentPerson = self.head
        print(currentPerson.name, currentPerson.seatNumber)

        while currentPerson.nextPerson != None:
            print(currentPerson.nextPerson.name, currentPerson.nextPerson.seatNumber)
            currentPerson = currentPerson.nextPerson




myList = LinkedList()
myList.append(Person(name="Julie", seatNumber=3))
myList.append(Person(name="Simon", seatNumber=13))
myList.append(Person(name="John", seatNumber=16))
myList.append(Person(name="Smith", seatNumber=20))

#myList.printList()
#print("=== Find Person ===")
#print(myList.findPerson(name="John").seatNumber, myList.findPerson(name="John").name)

myList.prepend(Person(name="Andrew", seatNumber=2))
myList.printList()

print("==============")
myList.deletePerson(name="Simon")
myList.printList()
