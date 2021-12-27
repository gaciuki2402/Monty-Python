class Animal(object):
    def __int__(self,Nickname,Breed):
        self.Nickname=Nickname
        self.Breed=Breed

    def Details(self):
        print(f"My name is {self.Nickname} and my breed is {self.Breed}.")

    def Suspecies(self,Suspecies):
        print(f"{self.Nickname} is of {Suspecies} suspecies.")

class Cow(Animal):
    def __init__(self,Nickname,Breed):
        super().__init__(Nickname,Breed)

    def HornStatus(self,Horn):
        print(f"{Suspecies} is naturally {Horn}.")

    def Stayability(self,Stayability):
        print(f"{Stayability} years old {Suspecies} are productive.")

    def RegionOfOrigin(self,Origin):
        print(f"{self.Breed} originates from {Origin}.")

    def Coat(self,Coat):
        print(f"{self.Breed} can either be {Coat}.")

    def Weight(self,Weight):
        print(f"Female {Suspecies} has {Weight} kgs while Male {Suspecies} has {Weight}kgs.")

    def Height(self,Height):
        print(f"Female {Suspecies} has a height of {Height} cm while Male {Suspecies} has a height of {Height} cm.")

    def GestationPeriod(self,Gestation):
        print(f"{Suspecies} average gestation period is {Gestation} days. ")

A1=Cow("Doddies","Aberdeen Angus")
A1.Details()
A1.Suspecies("Angus")
A1.HornStatus("Polled horn")
A1.Stayability("12 and 13")
A1.RegionOfOrigin("Scotland")
A1.Coat("Black or Red")
A1.Weight("1000 ,650")
A1.Height("145,135")
A1.GestationPeriod(283)
