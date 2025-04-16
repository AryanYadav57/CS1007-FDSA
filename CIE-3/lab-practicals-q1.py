class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None  


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node  

    def pop(self):
        if self.empty():
            return None
        popped_node = self.top  
        self.top = self.top.next  
        return popped_node.data  

    def peek(self):
        if self.empty():  
            return None
        return self.top.data  

    def empty(self):
        return self.top is None  

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top of the stack:", stack.peek()) 
    print("Pop from stack:", stack.pop())  
    print("Top of the stack after pop:", stack.peek())  
    print("Is stack empty?", stack.empty())  
    print("Pop all items:")
    print(stack.pop())  
    print(stack.pop()) 
    print("Is stack empty now?", stack.empty()) 
