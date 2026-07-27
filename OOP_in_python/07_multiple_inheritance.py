class Father:
    def father(self):
        print("Father")

class Mother:
    def mother(self):
        print("Mother")

class Child(Father, Mother):
    pass

c = Child()

c.father()
c.mother()