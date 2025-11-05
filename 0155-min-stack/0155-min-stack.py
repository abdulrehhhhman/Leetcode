class MinStack(object):

    def __init__(self):
        self.stk=[]
        self.min_stk=[]
       
        

    def push(self, val):
        self.stk.append(val)
        if not self.min_stk or val<= self.min_stk[-1]:
            self.min_stk.append(val)

       
        

    def pop(self):
        if self.stk:
            if self.stk[-1]==self.min_stk[-1]:
                self.min_stk.pop()
            self.stk.pop()    
    def top(self):
        return self.stk[-1] if self.stk else None

    def getMin(self):
        return self.min_stk[-1] if self.min_stk else None            

                

    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()