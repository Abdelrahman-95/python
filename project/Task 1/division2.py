def division2():  
    Number_1 = int(input("Enter Number One: ").strip())
    Number_2 = int(input("Enter Number Two: ").strip())
    Number_3 = []
    Number_4 = []
    for Number in range(1,101):
        if Number % Number_1 == 0:
            Number_3.append(Number)
        if Number % Number_2 == 0:
            Number_4.append(Number)
    print(Number_3)
    print(Number_4)


division2()