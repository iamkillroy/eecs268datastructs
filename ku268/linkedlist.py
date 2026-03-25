from .node import Node
class LinkedList:
    def __init__(self) -> None:
        """Creates a Linked List that can be inserted and traversed"""
        self.head = None
        self.length = 0

    def insert(self, index: int, entry) -> None:
        """Inserts the index at either 0 (front) or length inclusively"""
        if self.head == None:
            self.head = Node(entry)
            self.length += 1
            return None
        currentNode = self.head
        j = 0
        while (
            j != index and currentNode._next is not None
        ):  # if we're not at the index or we're at the end of the list
            currentNode = (
                currentNode._next
            )  # recursively go through each element A -> B -> C
            j += 1
        # REALLY IMPORTANT
        # to keep the list "linked" i'm going to get the next._next value
        # but if this is none, we gotta just add it on
        try:
            insertLocationNextNode = currentNode._next._next
        except AttributeError:
            insertLocationNextNode = None
        currentNode._next = Node(
            entry, next=insertLocationNextNode
        )  # se the next entry to the next Node
        self.linkedListLength += 1

    def length(self) -> int:
        """Fuction that recursively goes through every single element, but also doesn't
        necessarily need to go through every value because we're just counting and is an overengineered
        solution because I don't trust the methods and I'd rather be dead certain of the length"""
        if self.head == None:
            return 0  # quick zero node check
        currentNode = self.head  # set the current entry to the head
        lengthCounter = 1
        while currentNode._next != None:  # while the entry is not none
            lengthCounter += 1  # increment by 1
            currentNode = (
                currentNode._next
            )  # set the current entry to the the next entry
        return lengthCounter  # return the length

    def add(self, entry, front: bool = False) -> None:
        """Adds a linked list's element to the top (like a stack) or bottom (like a queue)"""
        if front:  # if we wanna add to the front
            previousNode = self.head
            self.head = Node(entry, previousNode)
        else:  # get the length, insert there
            self.insert(
                self.length(), entry
            )  # no offset needed on the length, it's the last nth indexable + 1 so next

    def __iter__(self):
        returnList: list = []
        currentNode: Node = self.head
        while hasattr(currentNode, "next"):
            returnList.append(currentNode._entry)
            currentNode = currentNode._next
        return iter(returnList)

    def display(self, debugInput=False, displayOutput=True) -> tuple[str, str]:
        """Displays the entire node in a human readable output way"""
        # converting from writing rust all break kinda made me like type
        # declarations that are explicit like this. it might be just a phase mom :(
        if self.head == None:
            raise RuntimeError("No Nodes in this list")
        nodeElementString: str = "START | "
        nodeValueString: str = "VALUE | "
        currentNode: Node = self.head  # start
        charDisplayList: tuple = (
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "Y",
            "X",
            "Z",
        )
        charDisplayPoint: int = 0
        while hasattr(currentNode, "next"):
            # first let's see if the entry can actually be displayed
            # for real for real by python's inbuilt str()
            try:
                valueOfNodeEntry = str(currentNode._entry)
            except TypeError:
                # that's okay let's just say the type as a string
                valueOfNodeEntry = str(type(currentNode._entry))
            nodeValueString = (
                nodeValueString + valueOfNodeEntry + " "
            )  # set value and offset
            distanceBetweenValue = (
                " " + (len(valueOfNodeEntry) - 3) * "-" + "> "
            )  # evil little offset
            nodeElementString = (
                nodeElementString
                + charDisplayList[charDisplayPoint % 25]
                + distanceBetweenValue
            )  # to display A B etc
            currentNode = currentNode._next
            charDisplayPoint += 1
        if displayOutput:
            print("LinkedList Display: ")
            print(nodeElementString)
            print(nodeValueString)
        if debugInput:
            input("OK > ")
        return nodeElementString, nodeValueString

    def get_entry(self, index: int) -> Node:
        """Gets entry with negative indexing"""
        if self.head == None:
            raise IndexError("List is empty")  # quick zero node check
        currentNode: Node = self.head
        j: int = 0
        # two modes, negative and positive addressing
        # postive addressing here
        if index >= 0:
            finalValue: int = index
        else:  # negative addressing
            finalValue: int = (
                self.length() - 2 #negative 2 is just an offset for -1 and then zero to get the right value
            ) - index  # -1 is for the list len versus index offset
        try:
            while j != abs(finalValue):  # while we're not there
                currentNode = currentNode._next  # increment
                j += 1
            return currentNode._entry  # return entry
        except TypeError:
            raise IndexError("The index can't be found in the list")

    def clear(self) -> None:
        """Clears the list"""
        self.head = None  # just clear it, thanks garbage collection in python!!!
        return None

    def pop(self) -> Node:
        "Removes the top element"
        return self.remove(self.length() - 1)  # nth element offset

    def remove(self, index) -> Node:
        """Removes element from given index and links all Nodes back together"""
        if self.head == None:
            raise IndexError(f"Can't delete from non-existant index {index}")
        try:
            j = 0
            currentNode: Node = self.head  # the current Node
            previousNode: Node = None  # the next Node
            while j != index:
                previousNode = currentNode
                currentNode = currentNode._next
                j += 1
            # okay now that we've found it, we need to set the previous node's value to the currentNode._next
            try:
                previousNode._next = currentNode._next
            except AttributeError:
                pass  # just means that the previous Node isn't actually real
                # like there's just no node that exist because it's like the 0th index
            self.linkedListLength -= 1
            return currentNode
        except:
            raise IndexError(f"Can't delete from non-existant index {index}")
