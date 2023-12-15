#The Cyclone Rollercoaster #####INCOMPLETO#####

height = int(input('Enter your height: '))
credit = int(input('How many credits do you have: '))
with_taller_person = False #bool(input('With a taller person? (True - False) '))

if credit < 10:
    print("You don't have enough credit to ride.")
elif height >= 137 and credit >= 10: 
    print("Enjouy the ride.")
elif height < 137:
    if height < 100 or not with_taller_person: #== False:
        print("You're not tall enough to ride yet.")
    elif height >= 100 and with_taller_person: #== True:
        print("Enjoy the ride.")
   # else:
   #     print("Invalid data.")
else:
    print("Invalid data.")