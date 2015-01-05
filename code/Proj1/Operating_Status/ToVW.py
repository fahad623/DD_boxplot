import csv
from string import maketrans

location_train = "../../../data/TrainingData.csv"
location_test = "../../../data/TestData.csv"

location_train_vw = "train.vw" #will be created
location_test_vw = "test.vw" #will be created

predict_list = ['Function', 'Object_Type', 'Operating_Status', 'Position_Type', 'Pre_K', 
                'Reporting', 'Sharing', 'Student_Type', 'Use']
                
labels_dict = {
    'Non-Operating' : 1, 
    'Operating, Not PreK-12' : 2,
    'PreK-12 Operating' : 3
    }


def clean_string(string):
    trantab = maketrans(' :', '__')
    str1 = string.strip().translate(trantab);
    
    if str1 != "":
        str1 = " " + str1
        
    return str1
    
def num(s):
    if not s:
        return 0.0
    else:
        try:
            return float(int(s))
        except ValueError:
            return float(s)
    
#creates Vowpal Wabbit-formatted file from tsv file
def to_vw(location_input_file, location_output_file, test = False):
    print "\nReading:",location_input_file,"\nWriting:",location_output_file
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile:
        count1 = 0
        count2 = 0
        count3 = 0
        reader = csv.DictReader(infile)
        for row in reader:
            if test:
                label = "1"
            else:
                label_int = labels_dict[row['Operating_Status']]
                label = str(label_int)
                if label_int == 1:
                    label = label + ' 8.33'
                    count1 = count1 + 1
                elif label_int == 2:
                    label = label + ' 46.19'
                    count2 = count2 + 1
                elif label_int == 3:
                    label = label + ' 1.165'
                    count3 = count3 + 1
            
            fte = ''
            if row['FTE']:
                fte = " FTE:" + row['FTE']

            outfile.write(
                str(label) +
                " '" + row[''] + " |f" +           
                fte +
                clean_string(row['Facility_or_Department']) +
                clean_string(row['Function_Description']) +
                clean_string(row['Fund_Description']) +
                clean_string(row['Job_Title_Description']) +
                clean_string(row['Location_Description']) +
                clean_string(row['Object_Description']) +
                clean_string(row['Position_Extra']) +
                clean_string(row['Program_Description']) +
                clean_string(row['SubFund_Description']) +
                clean_string(row['Sub_Object_Description']) +
                clean_string(row['Text_1']) +
                clean_string(row['Text_2']) +
                clean_string(row['Text_3']) +
                clean_string(row['Text_4']) +
                " Total:" + str(num(row['Total'])) + 
                "\n" )
        print count1, count2, count3

to_vw(location_train, location_train_vw)
to_vw(location_test, location_test_vw, test=True)