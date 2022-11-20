class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce(self):
        print(f"Hi I'm {self.firstName} {self.lastName}, they call me a Person")

personOne = Person("Clarence", "Castro")
personOne.introduce()

#inherit attributes of Person and add new attribute
class Student(Person):
    def __init__(self, firstName, lastName, course):
        super().__init__(firstName, lastName)
        self.course = course

#Overwrite method introduce
    def introduce(self):
        print(f"Hi I am {self.firstName} {self.lastName}, I took the course {self.course} and they call me a Student.")

studentOne = Student("Teng","Castro","BSIT")
studentOne.introduce()
