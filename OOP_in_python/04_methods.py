class Student:
    college = "IOE"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

    @classmethod
    def show_college(cls):
        print(cls.college)

    @staticmethod
    def greet():
        print("Welcome")

s1 = Student("Ram")

s1.display()
Student.show_college()
Student.greet()