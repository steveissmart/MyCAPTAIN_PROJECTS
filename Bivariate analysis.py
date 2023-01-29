import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('Daily_routine.csv')
#Converting the Start time column to float type data and storing it in a list 'Start_time_list_float'
Start_time_list = []
for i in df['Start time']:
    Start_time_list.append(i.split(':'))
Start_time_array = np.array(Start_time_list)
Start_time_list_float = []
for j in Start_time_array[:,0].astype(float):
    Start_time_list_float.append(j)
#Converting the End time column to float type data and storing it in a list 'End_time_list_float'
End_time_list = []
for i in df['End time']:
    End_time_list.append(i.split(':'))
End_time_array = np.array(End_time_list)
End_time_list_float = []
for j in End_time_array[:,0].astype(float):
    End_time_list_float.append(j)

Start_time_list_float_Series = pd.Series(Start_time_list_float)
End_time_list_float_Series = pd.Series(End_time_list_float)

#Creating a new dataset named 'Daily_Routine' which has Start time and End time values as float
data = [df['Productivity Level'], df['Activity done']]
headers = ['Productivity Level', 'Activity done']
Daily_Routine = pd.concat(data, axis = 1, keys=headers)
Daily_Routine.insert(0, 'Start time', Start_time_list_float_Series)
Daily_Routine.insert(1, 'End time', End_time_list_float_Series)

Activity_productivity_relation = pd.crosstab(Daily_Routine['Productivity Level'], Daily_Routine['Activity done'])

fig,ax = plt.subplots(figsize = (20,10))
ax.bar(Daily_Routine['Activity done'], Daily_Routine['Productivity Level'])
ax.set(title="Activity done and Productivity Level",
xlabel="Activity done",
ylabel="Productivity Level")
fig.show()

Daily_Routine_dict = dict(Daily_Routine)

Daily_Routine_dict_dataframe = pd.DataFrame(Daily_Routine_dict)

fig,ax = plt.subplots(figsize = (20,10))
plt.grid(color = 'black', linewidth = 0.5)
width = 0.75
ax.bar(Daily_Routine_dict_dataframe['Start time'], Daily_Routine_dict_dataframe['Productivity Level'])
ax.set(title="Time and Productivity Level",
xlabel="Start Time",
ylabel="Productivity Level")
ax.set_xticks(Daily_Routine_dict_dataframe['Start time'])
ax.set_xticklabels(Daily_Routine_dict_dataframe['Start time'].astype(str))
fig.show()