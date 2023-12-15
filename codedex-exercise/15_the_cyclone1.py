#The Cyclone Rollercoaster

height = int(input('Enter your height: '))
credit = int(input('How many credits do you have: '))

if height >= 137 and credit >= 10:
    print("Enjoy the ride.")
elif height < 137:
    print("You're not tall enough to ride.")
elif credit < 10:
    print("You don't have enough credits to ride.")
else:
    print("Invalid data.")