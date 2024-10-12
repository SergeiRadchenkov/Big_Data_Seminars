import csv

input_file = 'prices.csv'

total_price = 0.0
total_count = 0
prices = []

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)

    for row in reader:
        if len(row) != 2:
            continue
        
        try:
            price = float(row[0])
            count = int(row[1])
        except ValueError:
            continue

        total_price += price * count
        total_count += count
        prices.extend([price] * count)

mean_price = total_price / total_count if total_count else 0

if len(prices) > 1:
    variance = sum((p - mean_price) ** 2 for p in prices) / (len(prices) - 1)
else:
    variance = 0

print(f'Средняя цена: {mean_price:.2f}')
print(f'Дисперсия: {variance:.2f}')
