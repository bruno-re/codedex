#Checks pH's

ph = int(input('Insert pH (0-14): '))

if ph > 7:
    print('Basic.')
elif ph < 7:
    print('Acidic.')
else:
    print('Neutral')