
class Employees_List():
    def Employees_Details(self):
        self.Employees={
        "Gaciuki":{
            "RegNo":"KWS0043",
            "Location":"Nakuru",
            "Age":32,
            "Tel":"0678986",
            "Email":"gaciuki@gmail",
            "Degree":"Hospitality",
            "Postal":78
            },
        "Irene": {
            "RegNo": "KWS0293",
            "Location": "Kisumu",
            "Age": 28,
            "Tel": "0678643",
            "Email": "irene@gmail",
            "Degree":"Hospitality",
            "Postal_Code": 66200,
            "Points":64
            },
            "Day": {
                "RegNo": "KWS0093",
                "Location": "Nairobi",
                "Age": 48,
                "Tel": "074983274",
                "Email": "day@gmail",
                "Degree": "Tousism Management",
                "Postal_Code":324500,
                "Points":43
            },
            "Belta": {
                "RegNo": "KWS0113",
                "Location": "Nairobi",
                "Age": 24,
                "Tel": "07490323274",
                "Email": "belta@gmail",
                "Degree": "Culinary Arts",
                "Postal_Code": 32456,
                "Points":24
            },

            "Wambui": {
                "RegNo": "KWS0994",
                "Location": "Nanyuki",
                "Age": 34,
                "Tel": "060323274",
                "Email": "wambui@gmail",
                "Degree": "Aeronautical Eng",
                "Postal_Code": 3200,
                "Points":94
            },

        }
    def Senior_Employees(self):
        print("....SENIOR EMPLOYEES....")
        for employee in self.Employees:
            Points=self.Employees[employee]["Points"]
            if Points<50:
                continue
            print(f"{employee}---{Points}")

    def Junior_Employees(self):
        print("....JUNIUOR EMPLOYEES....")
        for employee in self.Employees:
            Points=self.Employees[employee]["Points"]
            if Points>=50:
                continue
            print(f"{employee}---{Points}")

E1=Employees_List()
E1.Employees_Details()
E1.Senior_Employees()
E1.Junior_Employees()