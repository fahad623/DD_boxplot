import pandas as pd

predict_list = ['Function', 'Object_Type', 'Operating_Status', 'Position_Type', 'Pre_K', 
                'Reporting', 'Sharing', 'Student_Type', 'Use']

df_list = []
for item in predict_list:
    path = item + '/' + 'submission.csv'
    df_list.append(pd.read_csv(path))


df_output = df_list[0].join(df_list[1:])
print df_output.shape
df_output.to_csv("finalout.csv", index = False)