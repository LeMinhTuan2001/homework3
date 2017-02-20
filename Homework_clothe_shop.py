clothe = ["T-Shirt", "Jacket","Bra","Jeans"]
while True:
    a = input("Welcome. What do you want(C,R,U,D)").lower()
    if (a=="c"):
        clothe.append(input("New item?"))
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[(len(clothe))-1])


        
    elif (a=="r"):
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])


        
    elif (a=="d"):
        item = int(input("Delete item? "))
        clothe.pop(item)
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])

        
    elif (a=="u"):
        item = int(input("Update item "))
        new_clothe = input("New item? ")
        clothe[item] = new_clothe
        print("Our items:", end=' ')
        for i in range(len(clothe)-1):
            print(clothe[i], end=', ')
        print(clothe[len(clothe)-1])
    print()
