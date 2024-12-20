#Sorting Hat

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

day = int(input("Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n>>>"))  

personality = int(input("When I'm dead, I want people to remenber me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n>>>"))   

instrument = int(input("Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n>>>"))   

#firt question
if day == 1:
    gryffindor += 1
    ravenclaw += 1
elif day == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

#second question
if personality == 1:
    hufflepuff += 2
elif personality == 2:
    slytherin += 2
elif personality == 3:
    ravenclaw += 2
elif personality == 4:
    gryffindor += 2
else:
    print("Wrong input")

#third question
if instrument == 1:
    slytherin += 4
elif instrument == 2:
    hufflepuff += 4
elif instrument == 3:
    ravenclaw += 4
elif instrument == 4:
    gryffindor += 4
else:
    print("Wrong input")

#Result
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("GRYFFINDOR!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("RAVENCLAW!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("HUFFLEPUFF!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("SLYTHERIN!")
else:
    print("Try again.")