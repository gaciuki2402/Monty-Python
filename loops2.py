i=10
while i<100:
    print(i)
    if i==70:
        print("Break the Loop")
        break
    i+=10
i=1
while i<10:
    print(i)
    if i==6:
        print("Break Loop")
        break
    i+=1

t=2
while t<=14:
    print(t)
    if t==14:
        print("Break loop")
        break
    t+=3

m=0
while m<=15:
    print(m)
    if m==9:
        print("Break Loop")
        #break
    m+=3
i=100
while i<220:
    print(i)
    if i==160:
        print("Breaking From The Loop")
        break
    i+=20

w=25.56
while w<=55.56:
    print(w)
    if w==45.56:
        print("Break Loop")
        break
    w+=10
print("x"*50)
for i in (0,1,2,3,4,5,6,7,8,9,10):
    if i==1 or i==2 or i==4 or i==6 or i==8:
        continue
    print(i)
print("x"*56)
for t in (10,20,30,40,50,60,70,80,90,100):
    if t==10 or t==30 or t==50 or t==70 or t==90:
        continue
    print(t)
print("="*56)

def break_the_loop():
    for i in range(100,500):
        if i==450:
            return f"i is equal to {i}"
        print (i)
print(break_the_loop())

def loop():
    for i in range(1,10):
        if i==8:
            return i
        print(i)
print(loop())
print("z"*56)

def break_from_loop():
    for t in range(10,20):
        if t==15:
            return f"t is equal to {t}"
        print(t)
print(break_from_loop())
def continue_looping():
    for i in range(10,20):
        if i==12:
            # print(f"{i} is present" )
            continue
        print(i)
    return "status OK"

print(continue_looping())


def class_names():
    students=["Grace","Gacioki","John","Doe","Irene","Day"]
    for student in students:
        if student=="John":
            continue
        print(student)
    return "---finished--"
print(class_names())

fruits= ["Mango","Paw Paw","Pineapple","Apple","Orange","Cherry"]
for fruit in fruits:
    print(i)

myList=["Grace","Irene","day"] #List/array
mytuple=("Grace","Irene","Day") #tuple--> values cant change/ immutable(127.0.0.1:8000,127.0.0.1:3000)
mySet={"Grace","Irene","Day","Grace"} #set
print(mySet)
#pass List
def studentPassList():
    students={
        "Grace":90,
        "Irene":90,
        "John":23,
        "Doe":40,
        "Jane":37
    }
    print("TTU PASS LIST")
    for student in students:
        marks=students[student]
        if marks<40:
            continue
        print(f"{student}- {students[student]}")

studentPassList()


class PerformanceList:
    def studentDetails(self):
        self.students={
            "Grace":{
                "Adm No":"Tu01",
                "Age":20,
                "Course":"MCS",
                "Marks":90
            },
            "Irene": {
                "Adm No": "Tu02",
                "Age": 21,
                "Course": "MCS",
                "Marks": 90
            },
            "John": {
                "Adm No": "Tu03",
                "Age": 22,
                "Course": "BBIt",
                "Marks": 38
            },
            "Doe": {
                "Adm No": "Tu03",
                "Age": 22,
                "Course": "BBIt",
                "Marks": 35
            },
        }
    def StudentPassList(self):
        print("-----Pass List-----")
        for student in self.students:
            marks=self.students[student]["Marks"]
            if marks<40:
                continue
            print(f"{student}--{marks}")

    def Supplimentary(self):
        print("-----Supplimentary-----")
        for student in self.students:
            marks=self.students[student]["Marks"]
            if marks>=40:
                continue
            print(f"{student}--{marks}")

c1=PerformanceList()
c1.studentDetails()
c1.StudentPassList()
c1.Supplimentary()