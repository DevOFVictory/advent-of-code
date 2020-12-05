file=open("input.txt" , "r")

values = []

for i in file:
    values.append(int(i))

for x in values:
    for y in values:
        for z in values:
            if x+y+z==2020:
                print(x,y,z,x*y*z)
                exit(0)
