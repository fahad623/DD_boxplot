import csv
from string import maketrans

location_train = "../../../data/TrainingData.csv"
location_test = "../../../data/TestData.csv"

location_train_vw = "train.vw" #will be created
location_test_vw = "test.vw" #will be created

predict_list = ['Function', 'Object_Type', 'Operating_Status', 'Position_Type', 'Pre_K', 
                'Reporting', 'Sharing', 'Student_Type', 'Use']
                
labels_dict = {    
    
    'NO_LABEL' : 1,
    'Non-School' : 2,
    'School' : 3

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

        reader = csv.DictReader(infile)
        for row in reader:
            if not test and row['Operating_Status'] == 'Non-Operating':
                continue
            if test:
                label = "1"
            else:
                label_int = labels_dict[row['Reporting']]
                label = str(label_int)
            
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
            

to_vw(location_train, location_train_vw)
to_vw(location_test, location_test_vw, test=True)