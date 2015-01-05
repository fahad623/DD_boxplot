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
        p4 = float(row2[0])
        p0=p1=p2=p3=p5=p6=p7=p8 = (1-p4)/8.0
    else:
        p0 = sigmoid(float(row[0][2:]))
        p1 = sigmoid(float(row[1][2:]))
        p2 = sigmoid(float(row[2][2:]))
        p3 = sigmoid(float(row[3][2:]))
        p4 = sigmoid(float(row[4][2:]))
        p5 = sigmoid(float(row[5][2:]))
        p6 = sigmoid(float(row[6][2:]))
        p7 = sigmoid(float(row[7][2:]))
        p8 = sigmoid(float(row[8][2:]))
        
        sum = p0+p1+p2+p3+p4+p5+p6+p7+p8
    
    return p0/sum, p1/sum, p2/sum, p3/sum, p4/sum, p5/sum, p6/sum, p7/sum, p8/sum
    
    

def to_csv():
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile, open(location_input_operating) as infile2:
        writer = csv.writer(outfile)
        writer.writerow(['Student_Type__Alternative', 'Student_Type__At Risk',
                         'Student_Type__ELL', 'Student_Type__Gifted',
                         'Student_Type__NO_LABEL',	'Student_Type__Poverty',
                         'Student_Type__PreK',	'Student_Type__Special Education',
                         'Student_Type__Unspecified'])
                         
        reader = csv.reader(infile, delimiter=" ")
        reader2 = csv.reader(infile2)
        row2 = reader2.next()
        for row in reader:
            row2 = reader2.next()
            writer.writerow(calc_probas(row, row2))

to_csv()