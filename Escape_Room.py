from time import sleep

#Room class
class Room:
    #constructor - name, exits, exitLocations, items, itemDescriptions, grabbables
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    
    #getters
    #name getter
    @property
    def name(self):
        return self._name
    
    #exits getter
    @property
    def exits(self):
        return self._exits
    
    #exitLocations getter
    @property
    def exitLocations(self):
        return self._exitLocations
    
    #items getter
    @property
    def items(self):
        return self._items
    
    #itemDescriptions getter
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    
    #grabbables getter
    @property
    def grabbables(self):
        return self._grabbables
    
    
    #setters
    #name setter
    @name.setter
    def name(self, new):
        self._name = new
        
    
    #exits setter
    @exits.setter
    def exits(self, new):
        self._exits = new
    
    #exitLocations setter
    @exitLocations.setter
    def exitLocations(self, new):
        self._exitLocations = new
    
    #items setter
    @items.setter
    def items(self, new):
        self._items = new
    
    #itemDescriptions setter
    @itemDescriptions.setter
    def itemDescriptions(self, new):
        self._itemDescriptions = new
    
    #grabbables setter
    @grabbables.setter
    def grabbables(self, new):
        self._grabbables = new
    
    
    #method to add exit to a room
    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)
    
    #method to add item to a room
    def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)
        
    #method to remove item from a room and change it to something else
    def replaceItem(self, oldItem, newItem, desc):
        for i in range(len(self.items)):
            if(self.items[i] == oldItem):
                self._itemDescriptions[i] = desc
                self.items[i] = newItem
                break
    
    #method to add grabbable to a room
    def addGrabbable(self, item):
        self._grabbables.append(item)
    
    #method to remove grabbable from a room
    def delGrabbable(self, item):
        self._grabbables.remove(item)
    #custom string output
    def __str__(self):
        #room name
        s = "You are in {}.\n".format(self.name)
        
        #items in room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        
        #exits from room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        
        #return full string
        return s
    
#method to create the rooms
def createRooms():
    global currentRoom
    
    #create rooms within room class
    global r1, r2, r3, r4, r5
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    
    #Room 1
    #add exits
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    #add grabbables
    r1.addGrabbable("key")
    #add items
    r1.addItem("chair", "This is indeed a chair.")
    r1.addItem("table", "Why is a raven like a writing desk? Also, there's a key on the table...")
    
    #Room 2
    #add exits
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    #add items
    r2.addItem("rug", "Is that the pattern or is that a stain?")
    r2.addItem("fireplace", "Who brought the marshmallows?")
    
    #Room 3
    #add exits
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    #add grabbables
    r3.addGrabbable("book")
    #add items
    r3.addItem("bookshelves", "So much knowledge, so little time...or maybe you're just easily distracted.")
    r3.addItem("statue", "Wow, it's (insert your favorite character here)!!")
    r3.addItem("desk", "Why is a raven like a writing table? also, there's a book on the desk...")
    
    #Room 4
    #add exits
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)
    #add grabbables
    r4.addGrabbable("6-pack")
    #add items
    r4.addItem("brewrig", "Not to be confused with a blue pig.")
    r4.addItem("kennel", "The pupper inside looks happy to see you, and sad when you walk away. Poor doggo.")
    
    #Room 5/Secret Room
    r5 = Room("the Secret Room")
    #add exits
    r5.addExit("west", r2)
    #add items
    r5.addItem("cat", "A cat sits in the center of the room, licking its paw...\nwhy do I hear boss music?")
    
    currentRoom = r1

#checks that the player has the key in their inventory
def hasKey():
    for item in inventory:
        if item == "key":
            return True
    return False
    
#checks that the player has the dog in their inventory
def hasDog():
    for item in inventory:
        if item == "doggo":
            return True
    return False
#Main
#Start the game
inventory = []
createRooms()

#Initiates final boss fight if player has read book to open room
def bossFight():
    if(hasDog()):
        print("The cat stands, giving you a mischievous look.")
        sleep(2)
        print("Arching its back, it takes its final form of Cat-thulu!")
        sleep(2)
        print("The doggo growls, also transforming into its final form: Dogzilla!")
        sleep(2)
        action = input("What do you do? (run/fight) ")
        if(action.lower() == "run"):
            #escape
            print("You run to safety in another room.")
            sleep(2)
            print("Not needing to worry about you, Dogzilla easily defeats Cat-thulu, clearing the way to the exit.")
            sleep(2)
            print("\n\nYOU WIN!\nYou and doggo walk into the sunset and live happily ever after.\n(Ending 4/4)")
            alive = False
            return
            
        elif(action.lower() == "fight"):
            print("You try to help Dogzilla defeat Cat-thulu.")
            sleep(2)
            print("Dogzilla tries to protect you, but you are both defeated!")
            sleep(1)
            print("\n\nGAME OVER\nYou died.\n(Ending 3/4)")
            alive = False
            return
        else:
            print("Dogzilla tries to protect you, but you are both defeated!")
            sleep(1)
            print("\n\nGAME OVER\nYou died.\n(Ending 3/4)")
            alive = False
            return
    else:
        print("The cat stands, giving you a mischievous look.")
        sleep(2)
        print("Arching its back, it takes its final form of Cat-thulu!")
        sleep(1)
        print("Almost before you can register what has happened, Cat-thulu has swiped its mighty paws and defeated you.")
        sleep(1)
        print("\n\nGAME OVER\nYou died.\n(Ending 2/4)")
        alive = False
        return

#Frees the dog if player has the key
def freeDog():
    response = input("unlock kennel with key? (y/n)? ")
    if(response.lower() == "y" or response.lower() == "yes"):
        inventory.remove("key")
        #add the dog in all rooms, as if it follows you around
        r4.replaceItem("kennel", "doggo", "wouf wouf") #Room 4

        r5.addItem("doggo", "Wouf wouf!")                #Room 5
        
        r3.addItem("doggo", "Wouf wouf!")               #Room 3

        r2.addItem("doggo", "Wouf wouf!")               #Room 2

        r1.addItem("doggo", "Wouf wouf!")               #Room 1
        
        inventory.append("doggo")                      #Inventory
        
        return "You free the doggo! He is so happy and follows you around.\n"
    else:
        return "The pupper looks devestated."

#Read book
def readBook():
    response = input("Read the book (y/n)? ")
    if(response == "y" or response == "Y" or response == "yes" or response == "Yes"):
        print("The book tells you about a secret passage accessed through the east wall of Room 2.")
        r2.addExit("east", r5)

#play until death or quit
global alive
alive = True
while (alive):
    #fall into the void (death)
    if (currentRoom == None):
        print("You open the door to reveal an infinite void.")
        sleep(1)
        print("Unable to resist its pull, you enter, falling out of the world.")
        sleep(1)
        print("\n\nGAME OVER\nYou died.\n(Ending 1/4)")
        alive = False
        break
    
    #set status
    status = "{}\nYou have: {}\n".format(currentRoom, inventory)
    print("-------------------------------------------------------------------------")
    print(status)
    
    #take user input
    action = input("What to do? ")
    action = action.lower()
    if(action == "quit" or action == "exit" or action == "leave" or action == "bye"):
        break
    
    #parse user input
    #default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."
    words = action.split()
    verb = ""
    noun = ""
    
    if(len(words) == 2):
        verb = words[0]
        noun = words[1]
    
    #verb "go" implementation
    if(verb == "go"):
        response = "Invalid exit."
        for i in range(len(currentRoom.exits)):
            if(noun == currentRoom.exits[i]):
                currentRoom = currentRoom.exitLocations[i]
                #print(currentRoom)
                response = "Room changed."
                break
    
    #verb "look" implementation
    elif(verb == "look"):
        response = "I don't see that item."
        for i in range(len(currentRoom.items)):
            if(noun == currentRoom.items[i]):
                response = currentRoom.itemDescriptions[i]
                seenItem = currentRoom.items[i]
                #Unlock kennel with key
                if(seenItem == "kennel" and hasKey()):
                    response = freeDog()
                    break
                #Dog defeats final boss cat
                if(seenItem == "cat"):
                    bossFight()
                    alive = False
                    break
            
    #verb "take" implementation
    elif(verb == "take"):
        response = "I don't see that item."
        for grabbable in currentRoom.grabbables:
            if(noun == grabbable):
                takenItem = grabbable
                inventory.append(grabbable)
                currentRoom.delGrabbable(grabbable)
                response = "Item grabbed."
            #Reading the book for access to a hidden room
            if(takenItem == "book"):
                readBook()
                break
    
    #display final response
    if(alive):
        print("\n{}".format(response))