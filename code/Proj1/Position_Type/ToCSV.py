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
        p8 = float(row2[0])
        p0=p1=p2=p3=p4=p5=p6=p7=p9=p10=p11=p12=p13=p14=p15=p16=p17=p18=p19=p20=p21=p22=p23=p24 = (1-p8)/24.0
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
        p9 = sigmoid(float(row[9][3:]))
        p10 = sigmoid(float(row[10][3:]))
        p11 = sigmoid(float(row[11][3:]))
        p12 = sigmoid(float(row[12][3:]))
        p13 = sigmoid(float(row[13][3:]))
        p14 = sigmoid(float(row[14][3:]))
        p15 = sigmoid(float(row[15][3:]))    
        p16 = sigmoid(float(row[16][3:]))
        p17 = sigmoid(float(row[17][3:]))
        p18 = sigmoid(float(row[18][3:]))
        p19 = sigmoid(float(row[19][3:]))
        p20 = sigmoid(float(row[20][3:]))
        p21 = sigmoid(float(row[21][3:]))
        p22 = sigmoid(float(row[22][3:]))
        p23 = sigmoid(float(row[23][3:]))
        p24 = sigmoid(float(row[24][3:]))
        
        sum = p0=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15+p16+p17+p18+p19+p20+p21+p22+p23+p24
        
    return p0/sum,p1/sum,p2/sum,p3/sum,p4/sum,p5/sum,p6/sum,p7/sum,p8/sum,p9/sum,p10/sum,p11/sum,p12/sum,p13/sum,p14/sum,p15/sum,p16/sum,p17/sum,p18/sum,p19/sum,p20/sum,p21/sum,p22/sum,p23/sum,p24/sum    
    

def to_csv():
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile, open(location_input_operating) as infile2:
        writer = csv.writer(outfile)
        writer.writerow(['Position_Type__(Exec) Director',	'Position_Type__Area Officers',
                         'Position_Type__Club Advisor/Coach',	'Position_Type__Coordinator/Manager',
                         'Position_Type__Custodian','Position_Type__Guidance Counselor',
                         'Position_Type__Instructional Coach',	'Position_Type__Librarian',
                         'Position_Type__NO_LABEL',	'Position_Type__Non-Position',
                         'Position_Type__Nurse',	'Position_Type__Nurse Aide',
                         'Position_Type__Occupational Therapist',	'Position_Type__Other',
                         'Position_Type__Physical Therapist', 'Position_Type__Principal',
                         'Position_Type__Psychologist',	'Position_Type__School Monitor/Security',
                         'Position_Type__Sec/Clerk/Other Admin',	'Position_Type__Social Worker',
                         'Position_Type__Speech Therapist','Position_Type__Substitute',
                         'Position_Type__TA','Position_Type__Teacher',	'Position_Type__Vice Principal'])
                         
        reader = csv.reader(infile, delimiter=" ")
        reader2 = csv.reader(infile2)
        row2 = reader2.next()
        for row in reader:
            row2 = reader2.next()
            writer.writerow(calc_probas(row, row2))

to_csv()