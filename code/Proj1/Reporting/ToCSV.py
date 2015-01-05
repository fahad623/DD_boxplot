import csv
import math

location_input_file = "raw.txt"
location_output_file = "submission.csv"
location_input_operating = "../Operating_Status/submission.csv"

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
  
def calc_probas(row, row2):
    
    sum = 1.0
    if (float(row2[0]) > float(row2[1])) and (float(row2[0]) > float(row2[2])):
        p0 = float(row2[0])
        p1=p2 = (1-p0)/2.0
    else:
        p0 = sigmoid(float(row[0][2:]))
        p1 = sigmoid(float(row[1][2:]))
        p2 = sigmoid(float(row[2][2:]))
        
        sum = p0+p1+p2
    
    return p0/sum, p1/sum, p2/sum
    
    

def to_csv():
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile, open(location_input_operating) as infile2:
        writer = csv.writer(outfile)
        writer.writerow(['Reporting__NO_LABEL','Reporting__Non-School',
                         'Reporting__School'])
                         
        reader = csv.reader(infile, delimiter=" ")
        reader2 = csv.reader(infile2)
        row2 = reader2.next()
        for row in reader:
            row2 = reader2.next()
            writer.writerow(calc_probas(row, row2))

to_csv()