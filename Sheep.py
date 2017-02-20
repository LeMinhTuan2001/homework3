ships_sizes = [5, 9, 40, 60, 100, 120, 211, 98]
times = int(input("do this for ? months"))
print("Hello, i'm the owner and these are my ship sizes")
print(ships_sizes)
for i in range (1,times+1):
    print("MONTH ", i)
    print("One month has passed, now here is my flock")
    print(ships_sizes)
    sizes_max = ships_sizes[0]
    position = 0
    for i in range (len(ships_sizes)):
        if(ships_sizes[i] > sizes_max):
            sizes_max = ships_sizes[i]
            position = i
    print("Now my biggest sheep has size ", sizes_max, "let's shear it")
    ships_sizes[position] = 8
    print("After shearing, here is m flock")
    print(ships_sizes)
    if(i>1):
        for j in range (len(ships_sizes)):
            ships_sizes[j] += 50
    print()
sum = 0
for i in range(len(ships_sizes)):
    sum += ships_sizes[i]
print("My flock has size in total: ", sum)
print("I would get", sum, "* 2$ =", sum * 2,end='')
print("$")
