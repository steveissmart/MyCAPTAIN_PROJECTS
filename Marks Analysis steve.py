import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the Dataset i.e. the 1_Year_Results.csv file
df = pd.read_csv('November.csv')
Sem_1 = df[df['Sem'] == 1]
Sem_2 = df[df['Sem'] == 2]
Sem_1_percent = []
for x in range(0,1):
    Sem_1_percent.append((Sem_1['Marks Received '] / Sem_1['Maximum Marks'])*100)
Sem_1_percent_data = pd.DataFrame(Sem_1_percent)
Sem_1_percent_data.transpose()
Sem_1['Percentage'] = Sem_1_percent_data.transpose()

#Similarly add percentage column to Sem_2 Dataset
Sem_2_percent = []
for x in range(0,1):
    Sem_2_percent.append((Sem_2['Marks Received '] / Sem_2['Maximum Marks'])*100)
Sem_2_percent_data = pd.DataFrame(Sem_2_percent)
Sem_2_percent_data.transpose()
Sem_2['Percentage'] = Sem_2_percent_data.transpose()

Sem_1.plot(x='Paper Name', y = ['Marks Received ','Maximum Marks'], kind = 'barh', figsize = (10,5), grid = True)

Sem_1.plot(x='Paper Name', y = 'Percentage', kind = 'bar', figsize = (10,5), grid = True)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(Sem_1['Percentage'], labels = Sem_1['Paper Name'],autopct='%1.2f%%')
plt.show()

Sem_2.plot(x='Paper Name', y = ['Marks Received ','Maximum Marks'], kind = 'barh', figsize = (10,5), grid = True)
Sem_2.plot(x='Paper Name', y = 'Percentage', kind = 'bar', figsize = (10,5), grid = True)


#Pie Graph plotting of Sem_2 percentage
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(Sem_2['Percentage'], labels = Sem_2['Paper Name'],autopct='%1.2f%%')
plt.show()

Total_marks_in_sem_1 = Sem_1['Maximum Marks'].sum()
Total_marks_scored_in_sem_1 = Sem_1['Marks Received '].sum()
percentage_in_sem_1 = ((Total_marks_scored_in_sem_1/Total_marks_in_sem_1) * 100 )

Total_marks_in_sem_2 = Sem_2['Maximum Marks'].sum()
Total_marks_scored_in_sem_2 = Sem_2['Marks Received '].sum()
percentage_in_sem_2 = ((Total_marks_scored_in_sem_2/Total_marks_in_sem_2) * 100 )

Marks = { 'Sem 1' : [Total_marks_in_sem_1, Total_marks_scored_in_sem_1, percentage_in_sem_1],
          'Sem 2' : [Total_marks_in_sem_2, Total_marks_scored_in_sem_2, percentage_in_sem_2]
}
Sem_1_2_marks = pd.DataFrame(Marks)

sns.heatmap(Sem_1_2_marks, annot=True, linecolor='yellow',linewidths=3)