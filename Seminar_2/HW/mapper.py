import csv

input_file = 'AB_NYC_2019.csv'
output_file = 'prices.csv'

with (
    open(input_file, 'r', encoding='utf-8') as infile,
    open(output_file, 'w', newline='', encoding='utf-8') as outfile
    ):

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) == 0:
            continue

        try:
            price = float(row[9])
        except ValueError:
            continue

        
        writer.writerow([price, 1])
