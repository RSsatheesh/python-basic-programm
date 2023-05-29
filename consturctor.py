class rs:
    def __init__(self,name,age):
        self.rsname=name
        self.rsage=age
    def displayAge(self):
        print("age:",self.rsage);

obj=rs("satheesh",20)
print("name:",obj.rsname);
obj.displayAge()
