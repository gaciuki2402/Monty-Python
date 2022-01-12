

i=3#start
while i<12: #end value =9
    print(i)
    if i==7:
        print('breaking from loop')
        break
    i+=2#increment



i=1
while i<10:
    print(i)
    if i==10:
        print('breaking from loop')
        break
    i+=0.25


i=100
while i<500:
    print(i)
    if i == 500:
        print('breaking the loop')
        break
    i+=50

i=95.38
while i<99.38:
    print(i)
    if i==100:
        print('breaking the loop')
        break
    i+=0.38

for i in(0,1,2,3,4):
    print(i)
    if i==2:
        break
#continue statement
for i in(0,1,2,3,4,5):
    if i==1 or i==3 or i==5:
        continue
    print(i)

#for loops
def break_loop():
    for i in range(1,5):
        if i==3:
            return i
        print(i)
    return i
print(break_loop())


def break_loop():
    for i in range(13,27):
        if i==15:
            return i
        print(i)
print(break_loop())

def break_loop():
    for i in range(45,60):
        if i==60:
            return i
        print(i)
print(break_loop())


def break_loop():
    for i in range(17,58):
        if i==23:
            return i
        print(i)

print(break_loop())

for i in range(5):
    print(i)

#iterating
for x in ["mango","apple","banana","cherry"]:
    print(x)

for m in range(1,6):
    print(m)

for index, item in enumerate(["mango","apple","banana","cherry"]):
    print(index,"::",item)


for t in ["kenya","uganda","tanzania","mozabique","china"]:
        print(t)
for index,item in enumerate(["kenya","uganda","tanzania","mozabique","china"]):
    print(index,"::",item)
  










