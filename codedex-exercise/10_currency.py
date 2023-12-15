#Currency

#1 usd 
cn = 0.14
jp = 0.0075
kr = 0.0076

#inputs
yuan = int(input('What do you have left in yuan? '))
yen = int(input('What do you have left in yen? '))
won = int(input('What do you have left in won? '))

usd_yuan = yuan * cn #yuan to dolar 
usd_yen = yen * jp   #yen to dolar
usd_won = won * kr   #won to dolar

usd = usd_yuan + usd_yen + usd_won  #total dolar

print('You have left:', usd)