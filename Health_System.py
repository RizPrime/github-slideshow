def getdate():
    import datetime
    return datetime.datetime.now()

client = {1:'Harry', 2:'Rohan', 3:'Hammad'}
d = str(getdate())

print("Enter the client key:", end=" ")
c = int(input())
clt = client[c]
print("Client name is ", clt)

if c == 1:
    print("Press 1 to enter log; Press 2 to read data.:", end=" ")
    inp1 = int(input())
    if inp1 ==1:
        print("Press 1 to enter diet log; Press 2 to enter workout log.:", end=" ")
        inp2 = int(input())
        if inp2 == 1:
            f = open("HarryDP.txt", "a")
            print("Enter meal taken:", end=" ")
            meal = input()
            f.write(d)
            f.write("\t")
            f.write(meal)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
        if inp2 == 2:
            f = open("HarryWork.txt", "a")
            print("Enter workout performed:", end=" ")
            wkot = input()
            f.write(d)
            f.write("\t")
            f.write(wkot)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
    else:
        print("Enter 1 for Diet log; Enter 2 for Workout log.:", end=" ")
        rd = int(input())
        if rd == 1:
            k = open("HarryDP.txt")
            a = k.read()
            print(a)
            k.close()
        if rd == 2:
            k = open("HarryWork.txt")
            a = k.read()
            print(a)
            k.close()

elif c == 2:
    print("Press 1 to enter log; Press 2 to read data.:", end=" ")
    inp1 = int(input())
    if inp1 == 1:
        print("Press 1 to enter diet log; Press 2 to enter workout log.:", end=" ")
        inp2 = int(input())
        if inp2 == 1:
            f = open("RohanDP.txt", "a")
            print("Enter meal taken:", end=" ")
            meal = input()
            f.write(d)
            f.write("\t")
            f.write(meal)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
        if inp2 == 2:
            f = open("RohanWork.txt", "a")
            print("Enter workout performed:", end=" ")
            wkot = input()
            f.write(d)
            f.write("\t")
            f.write(wkot)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
    else:
        print("Enter 1 for Diet log; Enter 2 for Workout log.:", end=" ")
        rd = int(input())
        if rd == 1:
            k = open("RohanDP.txt")
            a = k.read()
            print(a)
            k.close()
        if rd == 2:
            k = open("RohanWork.txt")
            a = k.read()
            print(a)
            k.close()

elif c == 3:
    print("Press 1 to enter log; Press 2 to read data.:", end=" ")
    inp1 = int(input())
    if inp1 == 1:
        print("Press 1 to enter diet log; Press 2 to enter workout log.:", end=" ")
        inp2 = int(input())
        if inp2 == 1:
            f = open("HammadDP.txt", "a")
            print("Enter meal taken:", end=" ")
            meal = input()
            f.write(d)
            f.write("\t")
            f.write(meal)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
        if inp2 == 2:
            f = open("HammadWork.txt", "a")
            print("Enter workout performed:", end=" ")
            wkot = input()
            f.write(d)
            f.write("\t")
            f.write(wkot)
            f.write("\n")
            print("Data Entered successfully!")
            f.close()
    else:
        print("Enter 1 for Diet log; Enter 2 for Workout log.:", end=" ")
        rd = int(input())
        if rd == 1:
            k = open("HammadDP.txt")
            a = k.read()
            print(a)
            k.close()
        if rd == 2:
            k = open("HammadWork.txt")
            a = k.read()
            print(a)
            k.close()

else:
     print("Client does not exist.")