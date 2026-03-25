from .node import Node

class Queue:
    def __init__(self) -> None:
        """Creates a queue"""
        self._front: Node | None = None #make the front and back
        self._back: Node | None = None
    def enqueue(self, entry) -> None:
        """Adds the value to the queue"""
        newNode = Node(entry) #make the new node
        if self._front == None:
            #is the front is empty then we must set the fron
            # to be equal to the newNode, as well as the back,
            # as it occupies both spaces
            self._front = newNode
            self._back = newNode
            return None
        else:
            #set the back to point to newNode
            self._back._next = newNode
            #replace the back with new node, so now the previous
            # back points to the new back
            self._back = newNode
    def dequeue(self):
        """Removes the top value from the queue"""
        #is the front empty?
        if self._front is None:
            #we can't dequeue nothing
            raise RuntimeError("Can't dequeue an empty queue")
        #set the removed eetry
        removedEntry = self._front._entry
        #is this the last node?
        if self._front._next != None:
            #if not, remove the _front by
            # setting the _front to _front._next
            # python garbage collecting deletes _front
            self._front = self._front._next
        return removedEntry
    def peek_front(self):
        """Returns the entry of the value at the front"""
        if self._front != None:
            #if the _front is not empty
            return self._front._entry
        raise RuntimeError("Nothing at front")
    def is_empty(self) -> bool:
        """Returns boolean if the queue is empty"""
        return True if self._front == None else False
