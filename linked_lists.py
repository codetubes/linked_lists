class Person():
    nextPerson = None #Person ()
    name = None #string
    seatNumber = None #string

    def __init__(self, name, seatNumber):
        self.name = name
        self.seatNumber = seatNumber

class LinkedList:
    head = None #Person()
    
    '''Add new person at the end of the list '''
    def append(self, person):
        if self.head == None:
            self.head = person
            return 

        currentPerson = self.head
     
        while currentPerson.nextPerson != None:
            currentPerson = currentPerson.nextPerson
        
        currentPerson.nextPerson = person
    
    '''Add Person at the begining of the list '''
    def prepend(self, person):
        if self.head == None:
            self.head = person
            return
        newHead = person
        newHead.nextPerson = head
        self.head = newHead
    
    '''Delete Person by name '''
    def deletePerson(self, name):
        if self.head == None:return

        if self.head.name == name:
            self.head = head.nextPerson
            return 

        current = self.head
        while current.nextPerson:
            if current.nextPerson.name == name:
                current.nextPerson = current.nextPerson.nextPerson
                return

            current = current.nextPerson

    '''Find person by name '''
    def findPerson(self,name):
        if self.head == None:return 

        if self.head.name == name:
            return self.head
        
        currentPerson = self.head
        while currentPerson.nextPerson:
            if currentPerson.nextPerson.name == name:
                return currentPerson.nextPerson
            
            currentPerson = currentPerson.nextPerson

    def printList(self):
        if self.head == None:print("List is empty")

        currentPerson = self.head
        print(currentPerson.name, currentPerson.seatNumber)
        while currentPerson.nextPerson:
            print(currentPerson.nextPerson.name,currentPerson.nextPerson.seatNumber)
            currentPerson = currentPerson.nextPerson
            

myList = LinkedList()
myList.append(Person(name="John", seatNumber=2))
myList.append(Person(name="Julie", seatNumber=4))
myList.append(Person(name="Andrew", seatNumber=5))
myList.append(Person(name="Samuel", seatNumber=11))

#print(myList.head.nextPerson.nextPerson.nextPerson.name, myList.head.nextPerson.nextPerson.nextPerson.seatNumber)
#print(myList.findPerson("Andrew").seatNumber)
myList.printList()
myList.deletePerson("Andrew")
print("==================")
myList.printList()
#myList.deletePerson("Andrew")




