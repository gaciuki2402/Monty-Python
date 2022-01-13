mountains={
    "Mount Everest":8848,
    "Mount Manaslu":8163,
    "Mount Trivor":7577,
    "Mount Noshaq":7492,
    "Mount Ultar":7388,
    "Mount Diran":7266,
    "Mount Malangutti Sar":7207
}
print(mountains)
print("-"*45)
class Basic_Salary():
    def Personal_Details(self):
        self.Employees={
            "Fortune":{
                "salary":900345},
            "Ernest":{
                "salary":674000},
            "Makandi":{
                "salary":5667000},
            "Peter":{
                "salary":2987056},
            "Njau":{
                "salary":987743},
            "Mwirigi":{
                "salary":67892303
            },

        }
    def Commision(self):
        print("...BIG SALARIED EMPLOYEES...")
        for employee in self.Employees:
            salary=self.Employees[employee]["salary"]
            commision = salary * 0.05
            if salary>=1000000:
                commision = salary * 0.05
                total_salary=commision+salary
                print(f"{employee} --> {salary} --- {commision} = {total_salary}")


    def commision(self):
        print("...LOW SALARIED EMPLOYEES...")
        for employee in self.Employees:
            salary=self.Employees[employee]["salary"]
            if salary<1000000:
                commission=salary*0.01
                total_salary=commission+salary
                print(f"{employee}-->{salary}---{commission} = {total_salary}")

E1=Basic_Salary()
E1.Personal_Details()
E1.Commision()
E1.commision()





