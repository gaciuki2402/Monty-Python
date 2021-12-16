for number in range(3):
    print('attempt', number + 1, (number + 1) * ".")

for number in range(4):
    print("grace", number)


def break_loop2():
    for j in range(1, 5):
        for i in range(1, 4):
            if i * j == 4:
                return (i)
            print(i * j)


def break_loop():
    for i in range(5.0,10.0):
        if i==9.8:
            return i
        print(i)

print(break_loop2())
print("==="*30)
name="Grace Gaciuki"
print(name)
for letter in name:
    print(letter)
l=[1,2,7,8,9,10]
print(l)
for num in l:
    print(num)

for i in range(10):
    print(i)

for i in range(100):
    print(i)
for k in range(50,70):
    print(k)

for l in range(0,100,5):
    print(l)

#range(start,stop,step)
for m in range(100,0,-1):
    print(m)
for n in range(100,0,-5):
    print(n)
n=["john","doe","jane","grace","python","irene","james"]
print(n)
for name in n:
    if name=="python":
        continue
    print(name)
#1. john
#2. doe
#create a loop
print(len(n))
#for index in range(len(n)):
 #   print(,n[index])