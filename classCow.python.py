class Animal(object):
    def __init__(self,Nickname,Breed,Suspecies):
        self.Nickname=Nickname
        self.Breed=Breed
        self.Suspecies=Suspecies

    def Details(self):
        print(f"My name is {self.Nickname}.My breed is {self.Breed} and {self.Suspecies} is my suspecies .")


class Cow(Animal):
    def __init__(self,Nickname,Breed,Suspecies):
        super().__init__(Nickname,Breed,Suspecies)

    def HornStatus(self,Horn):
        print(f"{self.Suspecies} is naturally {Horn}.")

    def Stayability(self,Stayability):
        print(f"{Stayability} years old {self.Suspecies} are productive.")

    def RegionOfOrigin(self,Origin):
        print(f"{self.Breed} originates from {Origin}.")

    def Coat(self,Coat):
        print(f"{self.Breed} can either be {Coat}.")

    def Weight(self,Weight):
        print(f"Female {self.Suspecies} has {Weight} kgs while Male {self.Suspecies} has {Weight}kgs.")

    def Height(self,Height):
        print(f"Female {self.Suspecies} has a height of {Height} cm while Male {self.Suspecies} has a height of {Height} cm.")

    def GestationPeriod(self,Gestation):
        print(f"{self.Suspecies} average gestation period is {Gestation} days. ")

A1=Cow("Doddies","Aberdeen Angus","Angus")
A1.Details()
A1.HornStatus("Polled horn")
A1.Stayability("12 and 13")
A1.RegionOfOrigin("Scotland")
A1.Coat("Black or Red")
A1.Weight("1000 ,650")
A1.Height("145,135")
A1.GestationPeriod(283)
