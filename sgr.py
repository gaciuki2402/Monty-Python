class SGR_Bookings():
    def Passengers_Details(self):
        self.Passengers={
            "Passenger1":{
                "Username":"Grace",
                "IdNo":36378989,
                "Contact":"07838345",
                "CoachNo":67,
                "SeatNo":96,
                "Destination":"Emali",
                "Amount":700
                },
            "Passenger2":{
                "Username": "Juma",
                "IdNo": 3618199,
                "Contact":"06767282",
                "CoachNo": 67,
                "SeatNo":23,
                "Destination": "Nairobi",
                "Amount": 700,
                },
            "Passenger4": {
                "Username": "Karen",
                "IdNo": 2618199,
                "Contact": "067443328",
                "CoachNo": 53,
                "SeatNo": 33,
                "Destination": "Athi River",
                "Amount": 1500
                },
            "Passenger5": {
                "Username": "Njoki",
                "IdNo": 45463782,
                "Contact": "07454542",
                "CoachNo": 20,
                "SeatNo": 14,
                "Destination": "Voi",
                "Amount": 200
                },
            "Passenger6": {
                "Username": "Fiona",
                "IdNo": 4324199,
                "Contact": "06231315",
                "CoachNo": 113,
                "SeatNo": 89,
                "Destination": "Mombasa",
                "Amount": 2000
                },

        }
    def first_class(self):
        print("...FIRST CLASS...")
        for passenger in self.Passengers:
            Amount=self.Passengers[passenger]["Amount"]
            Username=self.Passengers[passenger]["Username"]
            Destination=self.Passengers[passenger]["Destination"]
            CoachNo=self.Passengers[passenger]["CoachNo"]
            SeatNo=self.Passengers[passenger]["SeatNo"]
            if Amount<1000:
                continue
            print(f"{passenger}-->USERNAME:{Username}\n\tAMOUNT:{Amount}\n\tDESTINATION:{Destination}\n\tCOACH:{CoachNo}\n\tSEATNO:{SeatNo}")
    def economy_class(self):
        print("...ECONOMY CLASS...")
        for passenger in self.Passengers:
            Amount=self.Passengers[passenger]["Amount"]
            Username=self.Passengers[passenger]["Username"]
            Destination=self.Passengers[passenger]["Destination"]
            CoachNo=self.Passengers[passenger]["CoachNo"]
            SeatNo=self.Passengers[passenger]["SeatNo"]
            if Amount>1000:
                continue
            print(f"{passenger}-->USERNAME:{Username}\n\tAMOUNT:{Amount}\n\tDESTINATION:{Destination}\n\tCOACH:{CoachNo}\n\tSEATNO:{SeatNo}")

S1=SGR_Bookings()
S1.Passengers_Details()
S1.first_class()
S1.economy_class()
