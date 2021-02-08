types = int(input('Input kinds of liquid ingredients: '))
total_volume = 0
upper_part = 0
for i in range(types):
    abv = float(input('Input ABV of ingredients {} :'.format(i)))
    abv = abv / 100
    vol = float(input('Input volume of ingredients {} :'.format(i)))
    total_volume += vol
    item = abv * vol
    upper_part += item

final_ABV = (upper_part / total_volume) * 100
alcohol = total_volume * (final_ABV / 100)

print('The drink is {}ml, ABV {}%. {}ml of alcohol'.format(total_volume, final_ABV, alcohol))