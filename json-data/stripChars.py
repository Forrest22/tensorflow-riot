import csv
import string

input_file = open('matches200_adv.csv', 'r')
output_file = open('matches-test-stripped.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)# dialect='excel')
specials = '[]\'\"'

for line in data:
 new_line = str(line)
 print(line)
 for char in specials: 
    new_line = str.replace(new_line,char,'')
    print(new_line)
 writer.writerow(new_line.split(','))

input_file.close()
output_file.close()
