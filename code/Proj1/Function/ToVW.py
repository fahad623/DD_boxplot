import csv
from string import maketrans

location_train = "../../../data/TrainingData.csv"
location_test = "../../../data/TestData.csv"

location_train_vw = "train.vw" #will be created
location_test_vw = "test.vw" #will be created

predict_list = ['Function', 'Object_Type', 'Operating_Status', 'Position_Type', 'Pre_K', 
                'Reporting', 'Sharing', 'Student_Type', 'Use']
                
labels_dict = {
    'Aides Compensation' : 1,
    'Career & Academic Counseling' : 2,
    'Communications' : 3,
    'Curriculum Development' : 4,
    'Data Processing & Information Services' : 5,
    'Development & Fundraising' : 6,
    'Enrichment' : 7,
    'Extended Time & Tutoring' : 8,
    'Facilities & Maintenance' : 9,
    'Facilities Planning' : 10,
    'Finance, Budget, Purchasing & Distribution' : 11,
    'Food Services' : 12,
    'Governance' : 13,
    'Human Resources' : 14,
    'Instructional Materials & Supplies' : 15,
    'Insurance' : 16,
    'Legal' : 17,
    'Library & Media' : 18,
    'NO_LABEL' : 19,
    'Other Compensation' : 20,
    'Other Non-Compensation' : 21,
    'Parent & Community Relations' : 22,
    'Physical Health & Services' : 23,
    'Professional Development' : 24,
    'Recruitment' : 25,
    'Research & Accountability' : 26,
    'School Administration' : 27,
    'School Supervision' : 28,
    'Security & Safety' : 29,
    'Social & Emotional' : 30,
    'Special Population Program Management & Support' : 31,
    'Student Assignment' : 32,
    'Student Transportation' : 33,
    'Substitute Compensation' : 34,
    'Teacher Compensation' : 35,
    'Untracked Budget Set-Aside' : 36,
    'Utilities' : 37,
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
                label_int = labels_dict[row['Function']]
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