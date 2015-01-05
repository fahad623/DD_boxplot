import csv
import math

location_input_file = "raw.txt"
location_output_file = "submission.csv"



def sigmoid(x):
    return 1 / (1 + math.exp(-x))
  
def calc_probas(row):
    p0 = sigmoid(float(row[0][2:]))
    p1 = sigmoid(float(row[1][2:]))
    p2 = sigmoid(float(row[2][2:]))
    
    sum = p0+p1+p2
    
    return p0/sum, p1/sum, p2/sum
    
    

def to_csv():
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Operating_Status__Non-Operating', 'Operating_Status__Operating, Not PreK-12',
                         'Operating_Status__PreK-12 Operating'])
                         
        reader = csv.reader(infile, delimiter=" ")
        for row in reader:
            writer.writerow(calc_probas(row))

to_csv()