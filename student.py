class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def st_info(self):
        print(self.name, 'is', self.age, 'years old')
student1 = student('emmanuel', 19)
student1.st_info()
