class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.minstack and self.minstack[-1] == v:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        

'''
normal stack 
push pop top but cant get the minimum 

stack but only push if the element is the minimum 
to get min we just get from stack 

pushing to stacks
    push to normal stack 
    if ele is smaller than minstack[-1] push to minstack

poping from stacks 
    pop from normal stack 
    if its the same as minstack[-1] pop from that too



'''
