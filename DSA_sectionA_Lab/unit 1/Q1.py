class StackADT:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item) # O(1)
        
    def pop(self):
        if self.is_empty():
            return "Underflow Error: Stack is empty"
        return self.stack.pop() # O(1)
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1] # O(1)
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)


my_stack = StackADT()
text = "CSE 101"
for char in text:
    my_stack.push(char)

reversed_text = ""
while not my_stack.is_empty():
    reversed_text += my_stack.pop()

print(f"Original: {text} | Reversed using Stack: {reversed_text}")