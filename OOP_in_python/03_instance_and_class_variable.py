class Student:
    college = "IOE"

    def __init__(self, name):
        self.name = name

s1 = Student("Ram")
s2 = Student("Hari")

print(s1.college)
print(s2.college)