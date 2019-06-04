import csv
read_file = open('13주차\csv.csv','r')
reader = csv.reader(read_file,delimiter=',')
with open('13주차/transfer.tsv','w')as writer_file:
    writer=csv.writer(writer_file,delimiter=',')
    for row in reader:
        writer.writerow(row)


