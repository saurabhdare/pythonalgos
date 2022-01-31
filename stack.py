''' define the stack class '''

class Stack(object):

    def __init__(self):
        # this is a list
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value:
            return value
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return "Stack is empty"

    def __repr__(self):
        return '{}'.format(self.items)

if __name__=='__main__':
    stack = Stack()

    print("Is the stack empty?", stack.isEmpty())
    print("Adding 0 to 10 in the stack...")

    # add value into stack
    for i in range(10):
        stack.push(i)

    print("Stack size: ", stack.size())
    print("Stack peek: ", stack.peek())
    print("Pop....", stack.pop())
    print("Stack peek: ", stack.peek())
    print("Is the stack empty? ", stack.isEmpty())

    # print it as a list
    print(stack)
