def schools():
    schools=["Masinde","Kibwezi","Taita","Voi","Imara Daima","Mutoro","Prestige"]
    for school in schools:
        if school=="Taita":
            continue
        print(school)
    return "OK"
print(schools())

def fruits():
    fruits=["apple","mango","orange","banana","lemon","berry","guava"]
    for fruit in fruits:
        if fruit=="orange":
            continue
        print(fruit)
    return "....finished...."
print(fruits())

def Cities():
    Cities=["Nairobi","Mombasa","Nakuru","Kisumu","Dar El Salam","Arusha","Warsaw"]
    for city in Cities:
        if city=="Nakuru":
            continue
        print(city)
    return "Ok"
print(Cities())
print("z"*57)

def Hospitals():
    Hospitals=["Kenyatta National Hospital","Meru Level Five Hospital","Aga Khan Hospital","Getrudes Hospital"]
    for hospital in Hospitals:
        if hospital=="Aga Khan Hospital":
            continue
        print(hospital)
    return"...COMPLETE..."
print(Hospitals())
angles={
    "acute angle":180,
    "right angle":90,
    "obtuse angle":270,
    "reflex anlge":360
}
print(angles)
print("x"*67)
def Interview_List():
    interviewees={
        #"interviewee":points,
        "Grace":23,
        "Irene":65,
        "Belta":78,
        "Day":45,
        "Peni":80,
        "Wambui":47,
        "Gaciuki":94
    }
    print("KWS NEW EMPLOYEES LIST")
    for interviewee in interviewees:
        Points=interviewees[interviewee]
        if Points<50:
            continue
        print(f"{interviewee}-{interviewees[interviewee]}")
Interview_List()
print("-"*78)


