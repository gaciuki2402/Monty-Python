class Covid_19_Sampling():
    def Volunteers(self):
        self.Samples={
            1:{
                "Name":"Bessy",
                "Age":21,
                "Blood_Group":"O+",
                "Weight":"231 Pounds",
                "Temperature":36,
                "Blood_Pressure":"156/2",
                "Location":"Nyanza"

            },
            2:{
                "Name": "Gaciuki",
                "Age": 20,
                "Blood_Group": "O-",
                "Weight": "201 Pounds",
                "Temperature": 40,
                "Blood_Pressure": "122/3",
                "Location": "Tigania"

            },
            3:{
                "Name": "David",
                "Age": 31,
                "Blood_Group": "A+",
                "Weight": "190 Pounds",
                "Temperature": 42,
                "Blood_Pressure": "178/2",
                "Location": "Nakuru"

            },
            4:{
                "Name": "Kinaynjui",
                "Age": 11,
                "Blood_Group": "B-",
                "Weight": "94 Pounds",
                "Temperature": 39,
                "Blood_Pressure": "111/2",
                "Location": "Meru"

            },
            5:{
                "Name": "Joyce",
                "Age": 41,
                "Blood_Group": "A+",
                "Weight": "131 Pounds",
                "Temperature": 32,
                "Blood_Pressure": "201/3",
                "Location": "Isiolo"
            }
        }
    def Positive(self):
        print("The Following Have Covid_19 Virus.")
        for sample in self.Samples:
            Temperature=self.Samples[sample]["Temperature"]
            Name=self.Samples[sample]["Name"]
            if Temperature<36:
                continue
            print(f"{Name}...> {Temperature}")
    def Negative(self):
        print("The Following Tested Negative For Covid_19 Virus.")
        for sample in self.Samples:
            Temperature=self.Samples[sample]["Temperature"]
            Name=self.Samples[sample]["Name"]
            if Temperature>=36:
                continue
            print(f"{Name}...>{Temperature} ")
c1=Covid_19_Sampling()
c1.Volunteers()
c1.Positive()
c1.Negative()

