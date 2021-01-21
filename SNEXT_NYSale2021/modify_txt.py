namein = open('names.txt', 'r+', encoding='utf-8')
names = namein.readlines()

new_names = []
for i in names:
    j = i.split('\n')[0]
    if j != '\n' and j != '':
        new_names.append(j)
pricein = open('prices.txt', 'r+', encoding='utf-8')
prices = pricein.readlines()
print(len(new_names))
print(len(prices))
nameout = open('2021_NYSale.txt', 'w+', encoding='utf-8')
for j in range(len(new_names)):
    line = new_names[j] + ' - ' + prices[j]
    nameout.write(line)