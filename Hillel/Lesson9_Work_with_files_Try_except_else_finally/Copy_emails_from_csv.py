import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    with open('new_names.csv', 'w', newline='') as csv_file_new:
        csv_writer = csv.writer(csv_file_new)

        for line in csv_reader:
            email = line[2]
            csv_writer.writerow([email])

