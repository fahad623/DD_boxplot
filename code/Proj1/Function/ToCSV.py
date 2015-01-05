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
        p18 = float(row2[0])
        p0=p1=p2=p3=p4=p5=p6=p7=p8=p9=p10=p11=p12=p13=p14=p15=p16=p17=p19=p20=p21=p22=p23=p24=p25=p26=p27=p28=p29=p30=p31=p32=p33=p34=p35=p36 = (1-p18)/36.0
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
        p25 = sigmoid(float(row[25][3:]))    
        p26 = sigmoid(float(row[26][3:]))
        p27 = sigmoid(float(row[27][3:]))
        p28 = sigmoid(float(row[28][3:]))
        p29 = sigmoid(float(row[29][3:]))
        p30 = sigmoid(float(row[30][3:]))
        p31 = sigmoid(float(row[31][3:]))
        p32 = sigmoid(float(row[32][3:]))
        p33 = sigmoid(float(row[33][3:]))
        p34 = sigmoid(float(row[34][3:]))
        p35 = sigmoid(float(row[35][3:]))    
        p36 = sigmoid(float(row[36][3:]))
        
        sum = p0+p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15+p16+p17+p18+p19+p20+p21+p22+p23+p24+p25+p26+p27+p28+p29+p30+p31+p32+p33+p34+p35+p36
        
    return row[37],p0/sum,p1/sum,p2/sum,p3/sum,p4/sum,p5/sum,p6/sum,p7/sum,p8/sum,p9/sum,p10/sum,p11/sum,p12/sum,p13/sum,p14/sum,p15/sum,p16/sum,p17/sum,p18/sum,p19/sum,p20/sum,p21/sum,p22/sum,p23/sum,p24/sum,p25/sum,p26/sum,p27/sum,p28/sum,p29/sum,p30/sum,p31/sum,p32/sum,p33/sum,p34/sum,p35/sum,p36/sum   
    

def to_csv():
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile, open(location_input_operating) as infile2:
        writer = csv.writer(outfile)
        writer.writerow(['id',
                         'Function__Aides Compensation',
                         'Function__Career & Academic Counseling',
                         'Function__Communications',
                         'Function__Curriculum Development',
                         'Function__Data Processing & Information Services',
                         'Function__Development & Fundraising',
                         'Function__Enrichment',
                         'Function__Extended Time & Tutoring',
                         'Function__Facilities & Maintenance',
                         'Function__Facilities Planning',
                         'Function__Finance, Budget, Purchasing & Distribution',
                         'Function__Food Services',
                         'Function__Governance',
                         'Function__Human Resources',
                         'Function__Instructional Materials & Supplies',
                         'Function__Insurance',
                         'Function__Legal',
                         'Function__Library & Media',
                         'Function__NO_LABEL',
                         'Function__Other Compensation',
                         'Function__Other Non-Compensation',
                         'Function__Parent & Community Relations',
                         'Function__Physical Health & Services',
                         'Function__Professional Development',
                         'Function__Recruitment',
                         'Function__Research & Accountability',
                         'Function__School Administration',
                         'Function__School Supervision',
                         'Function__Security & Safety',
                         'Function__Social & Emotional',
                         'Function__Special Population Program Management & Support',
                         'Function__Student Assignment',
                         'Function__Student Transportation',
                         'Function__Substitute Compensation',
                         'Function__Teacher Compensation',	
                         'Function__Untracked Budget Set-Aside',
                         'Function__Utilities'])
                         
        reader = csv.reader(infile, delimiter=" ")
        reader2 = csv.reader(infile2)
        row2 = reader2.next()
        for row in reader:
            row2 = reader2.next()
            writer.writerow(calc_probas(row, row2))

to_csv()