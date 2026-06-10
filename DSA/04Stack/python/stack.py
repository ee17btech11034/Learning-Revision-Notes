class stack:
    def __init__(self):
        self.st = []
    
    def length(self):
        return len(self.st)
    
    def insert(self, value):
        # we can use append but then last element will be the top 
        self.st.insert(0, value) # first element is the top
    
    def pop(self):
        if (self.length):
            self.st.pop(0)
        else:
            raise Exception("Stack underflow -> No element to pop")
    
    def peek(self):
        if (self.length):
            return self.st[0]
        else:
            raise Exception("No element in stack")
        
st_obj = stack()
