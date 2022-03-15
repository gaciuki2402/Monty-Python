def Candidates():
    Students=["Grace","Peni","Belta","Elegae","Mike","Salma"]
    for student in Students:
        if student=="Elegae":
            continue
        print(student)
    return "......."

Candidates()
print("*"*67)

class Categories_of_Animals():
    def Animals(self):
        self.animals={
            1:{
                "Name":"Zebra",
                "Area":"National Park"
            },
            2:{
                "Name": "Lion",
                "Area": "National Park"
            },
            3:{
                "Name": "Goat",
                "Area": "Home"
            },
            4:{
                "Name": "Rhino",
                "Area": "National Park"
            },
            5:{
                "Name": "Pig",
                "Area":"Home"
            },
            6:{
                "Name": "Cow",
                "Area": "Home"
            }
        }
    def Wild_Animals(self):
        print("The Following Are Wild Animals.")
        for animal in self.animals:
            Area=self.animals[animal]["Area"]
            Name=self.animals[animal]["Name"]
            if Area=="Home":
                continue
            print(f"{Name}")
    def Domestic_Animals(self):
        print("The Following Are Domestic Animals.")
        for animal in self.animals:
            Area=self.animals[animal]["Area"]
            Name=self.animals[animal]["Name"]
            if Area=="National Park":
                continue
            print(f"{Name}")
a1=Categories_of_Animals()
a1.Animals()
a1.Wild_Animals()
a1.Domestic_Animals()

