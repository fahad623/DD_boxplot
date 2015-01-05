import csv
from string import maketrans

location_train = "../../../data/TrainingData.csv"
location_preds = "preds.txt"
location_out = "diff.txt"
                
labels_dict = {
    'Non-Operating' : 1, 
    'Operating, Not PreK-12' : 2,
    'PreK-12 Operating' : 3
    }

def test():
    with open(location_train) as infile1, open(location_preds) as infile2, open(location_out, "wb") as outfile:

        reader1 = csv.DictReader(infile1)
        reader2 = csv.DictReader(infile2, delimiter=' ')
        for row1 in reader1:
            row2 = reader2.next()
            actual = labels_dict[row1['Operating_Status']]
            if actual == 1:
                pred = int(float(row2['pred']))
                if pred != 1:
                    outfile.write(row1[''] + " " + str(pred) + '\n')
           

test()