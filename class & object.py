class rs:
    def fun(self,a,b):
        self.a=a
        self.b=b
        print("This is Class & Object:");
        
    def fun1(self):
        c=self.a+self.b;
        print(c);

obj=rs();
obj.fun(1000,2000);
obj.fun1();
