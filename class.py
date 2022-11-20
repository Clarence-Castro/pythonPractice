class socMed():
    def __init__(self, firstName, lastName, likes, friends):
        self.firstName = firstName
        self.lastName = lastName
        self.likes = likes
        self.friends = friends

    def introduce(self):
        print(f"Hi I am {self.firstName} {self.lastName}")

    def fullProfile(self):
        print(f"Full Name\t: {self.firstName} {self.lastName} \nLikes\t: {str(self.likes)}")
        print("Friends\t:")
        for x in self.friends:
            print(x)


friendsList = ("Carlos Perez" , "Marielle Reyes", "Kenneth Navarro")
soc = socMed("Clarence","Castro", 10, friendsList)
soc.introduce()
soc.fullProfile()