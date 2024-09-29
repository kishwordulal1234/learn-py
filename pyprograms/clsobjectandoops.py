class employe:
    def putdata(self):
        self.name = input("inter your name ")
        self.id = int(input("inter your id "))
        self.salary = float(input("inter the salary "))
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
    
var = employe()
var.putdata()
var.display()

