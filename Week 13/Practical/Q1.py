# Implementation of the Stack ADT using a Python list.
class Stack:
    # Creates an empty stack.
    def __init__( self ):
        self._theItems = list()

    #Returns True if the stack is empty or False
    # otherwise.
    def isEmpty( self ):
        return len(self._theItems) < 1
        # if len(self._theItems) == 0:
        #     return True
        # else:
        #     return False

    # Returns the number of items in the stack.
    def __len__ ( self ):
        return len(self._theItems)
    # Returns the top item on the stack without
    # removing it.

    def peek( self ):
        assert not self.isEmpty(), \
        "Cannot peek at an empty stack"
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), \
        "Cannot pop from an empty stack"
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    def push( self, item ):
        self._theItems.append(item)

    # Returns the str value of stack
    def __str__(self):
        return str(self._theItems)

#Test Codes

if __name__ == '__main__':

    PROMPT = "Enter a number (ctrl-D to end): "
    myStack = Stack()

    value = int(input(PROMPT))
    while True:
        try:
            myStack.push(value)
            value = int(input(PROMPT))

        except EOFError:
            break

    print("\nThe contents of the stack: ")
    while not myStack.isEmpty():
        value = myStack.pop()
        print(value)
