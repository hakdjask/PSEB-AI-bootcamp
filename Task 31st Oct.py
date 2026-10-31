class person: 
    def __init__(self):
        
        self.person_name = input("Enter your name: ")
        self.person_age = int(input("Enter your age: "))
         
    def greet(self):
        print(f"Hello, my name is {self.person_name} and I am {self.person_age} years old.")
    
h = person()
h.greet()