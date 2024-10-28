from IPython.display import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from scipy import stats


#Get raw data and process it

path1 = '/home/asik/Документы/ELISA2(1).xlsx'
path2 = '/home/asik/Документы/ELISA2 (2).xlsx'
path3 = '/home/asik/Документы/ELISA2(3).xlsx'


df1 = pd.read_excel(path1, usecols = [1,2,3,4,5,6,7,8,9,10,11,12, 13], sheet_name='RawData')
df1.rename(columns={df1.columns[0]:"Lunki", df1.columns[1]: "1", df1.columns[2]:"2", df1.columns[3]:"3", df1.columns[4]:"4", df1.columns[5]:"5", \
           df1.columns[6]: "6", df1.columns[7]: "7", df1.columns[8]:"8", df1.columns[9]: "9", df1.columns[10]: "10", df1.columns[11]: "11", \
           df1.columns[12]: "12"}, inplace = True)

df2 = pd.read_excel(path2, usecols = [1,2,3,4,5,6,7,8,9,10,11,12, 13], sheet_name='RawData')
df2.rename(columns={df2.columns[0]:"Lunki", df2.columns[1]: "1", df2.columns[2]:"2", df2.columns[3]:"3", df2.columns[4]:"4", df2.columns[5]:"5", \
           df2.columns[6]: "6", df2.columns[7]: "7", df2.columns[8]:"8", df2.columns[9]: "9", df2.columns[10]: "10", df2.columns[11]: "11", \
           df2.columns[12]: "12"}, inplace = True)

df3 = pd.read_excel(path3, usecols = [1, 2, 3], sheet_name='RawData')
df3.rename(columns={df3.columns[0]:"Lunki", df3.columns[1]: "1", df3.columns[2]: "2"}, inplace = True)

df1_mean1 = df1["1"][2:10]
df1_mean2 = df1["2"][2:10]
df1_mean3 = df1["3"][2:10]
df1_mean4 = df1["4"][2:10]
df1_mean5 = df1["5"][2:10]
df1_mean6 = df1["6"][2:10]
df1_mean7 = df1["7"][2:10]
df1_mean8 = df1["8"][2:10]
df1_mean9 = df1["9"][2:10]
df1_mean10 = df1["10"][2:10]
df1_mean11 = df1["11"][2:10]
df1_mean12 = df1["12"][2:10]


df2_mean1 = df2["1"][2:10]
df2_mean2 = df2["2"][2:10]
df2_mean3 = df2["3"][2:10]
df2_mean4 = df2["4"][2:10]
df2_mean5 = df2["5"][2:10]
df2_mean6 = df2["6"][2:10]
df2_mean7 = df2["7"][2:10]
df2_mean8 = df2["8"][2:10]
df2_mean9 = df2["9"][2:10]
df2_mean10 = df2["10"][2:10]
df2_mean11 = df2["11"][2:10]
df2_mean12 = df2["12"][2:10]

df3_mean1 = df3["1"][4:10]
df3_mean2 = df3["2"][2:8]

dfs = [df1_mean1, df1_mean2, df1_mean3, df1_mean4, df1_mean5, df1_mean6, df1_mean7, df1_mean8, \
       df1_mean9, df1_mean10, df1_mean11, df1_mean12, df2_mean1, df2_mean2, df2_mean3, df2_mean4, \
       df2_mean4, df2_mean6, df2_mean7, df2_mean8, df2_mean9, df2_mean10, df2_mean11, df2_mean12, \
       df3_mean1, df3_mean2]
dfs_concat = pd.concat(dfs)
df_list = dfs_concat.tolist()

number_of_groups = int(input("Number of groups: "))
#number_of_mice = int(input("Number of mice per group: "))

def round_robin_sublists(l, number_of_mice):
    lists = [[] for _ in range(number_of_groups)]
    i = 0
    for elem in l:
        lists[i].append(elem)
        i = (i + 1) % number_of_mice
    return lists

my_lst = []
for i in range(1, len(df_list) + 1):
    if i == 0 or i % 2 != 0:
        numbers = (df_list[i]+df_list[i-1])/2
        my_lst.append(numbers)

group1 = my_lst[:3]
group2 = my_lst[3:13]
group3 = my_lst[13:28]
group4 = my_lst[28:43]
group5 = my_lst[43:58]
group6 = my_lst[58:61]
group7 = my_lst[61:70]
group8 = my_lst[70:85]
group9 = my_lst[85:99]

nest_list = [group1, group2, group3, group4, group5, group6, group7, group8, group9]

#make plot to assess distribution type

fig, axes = plt.subplots(ncols = 3, nrows = 3, figsize=(10,10))
plt.subplots_adjust(hspace=0.5, wspace=0.5)
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9 = axes.flatten()

ax1.hist(nest_list[0])
ax1.set_title('Group 1')
ax1.set_xlabel('Expression level')
ax1.set_ylabel('Number of mice')


ax2.hist(nest_list[1])
ax2.set_title('Group 2')
ax2.set_xlabel('Expression level')
ax2.set_ylabel('Number of mice')


ax3.hist(nest_list[2])
ax3.set_title('Group 3')
ax3.set_xlabel('Expression level')
ax3.set_ylabel('Number of mice')


ax4.hist(nest_list[3])
ax4.set_title('Group 4')
ax4.set_xlabel('Expression level')
ax4.set_ylabel('Number of mice')


ax5.hist(nest_list[4])
ax5.set_title('Group 5')
ax5.set_xlabel('Expression level')
ax5.set_ylabel('Number of mice')


ax6.hist(nest_list[5])
ax6.set_title('Group 6')
ax6.set_xlabel('Expression level')
ax6.set_ylabel('Number of mice')


ax7.hist(nest_list[6])
ax7.set_title('Group 7')
ax7.set_xlabel('Expression level')
ax7.set_ylabel('Number of mice')


ax8.hist(nest_list[7])
ax8.set_title('Group 8')
ax8.set_xlabel('Expression level')
ax8.set_ylabel('Number of mice')


ax9.hist(nest_list[8])
ax9.set_title('Group 9')
ax9.set_xlabel('Expression level')
ax9.set_ylabel('Number of mice')

fig.text(s='Kruskal-Wallis Test p-value = 0.041244626235673584', x=0.5, y=0.98, fontsize=12, ha='center', va='center')
fig.text(s='Kruskal-Wallis Test p-value = 0.07205091172127985', x=0.5, y=0.95, fontsize=12, ha='center', va='center')


plt.show()

# Here starts beautiful boxplot + scatterplot =)

x1 = [1, 1, 1]
y1 = nest_list[0]

x2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
y2 = nest_list[1]

x3 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
y3 = nest_list[2]

x4 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
y4 = nest_list[3]

x5 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
y5 = nest_list[4]

x6 = [6, 6, 6]
y6 = nest_list[5]

x7 = [7, 7, 7, 7, 7, 7, 7, 7, 7]
y7 = nest_list[6]

x8 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
y8 = nest_list[7]

x9 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
y9 = nest_list[8]

# Assess median with Kruskal test

control = [1.463, 0.371] #контрольные образцы внутри плашки, нормально ли работает сама плашка
result1 = stats.kruskal(control, nest_list[1], nest_list[2], nest_list[3], nest_list[4])
result2 = stats.kruskal(control, nest_list[6], nest_list[7], nest_list[8])
print(result1)
print(result2)

bplot = plt.boxplot([nest_list[0], nest_list[1], nest_list[2], nest_list[3], nest_list[4], nest_list[5], nest_list[6], nest_list[7], nest_list[8]], \
                    showfliers=False, whis=(10, 90), boxprops=dict(alpha=0.5), patch_artist=True)
colors = ['peachpuff', 'darkslategrey', 'midnightblue', 'midnightblue', 'midnightblue', 'peachpuff',\
          'darkslategrey', 'midnightblue', 'midnightblue']

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.scatter(x1, y1, s=150, c='firebrick')
plt.scatter(x2, y2, s=150, c='firebrick')
plt.scatter(x3, y3, s=150, c='firebrick')
plt.scatter(x4, y4, s=150, c='firebrick')
plt.scatter(x5, y5, s=150, c='firebrick')
plt.scatter(x6, y6, s=150, c='firebrick')
plt.scatter(x7, y7, s=150, c='firebrick')
plt.scatter(x8, y8, s=150, c='firebrick')
plt.scatter(x9, y9, s=150, c='firebrick')

axes = plt.gca()

text_values = ['BALB/c Control Buffer', 'BALB/c DPT strain', 'BALB/c group1', 'BALB/c group2', 'BALB/c group3', \
               'CD-1 Control Buffer', 'CD-1 DPT strain', 'CD-1 group1', 'CD-1 group2']
x_values = np.arange(1, len(text_values) + 1, 1)
plt.xticks(x_values, text_values)

axes.set_ylim([0,4])

axes.annotate('ns', xy=(0.775, 0.75), xytext=(0.775, 0.8), xycoords='axes fraction',
            fontsize=11*1.25, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=4.2, lengthB=2.0', lw=2.5, color='k'))

axes.annotate('ns', xy=(0.834, 0.85), xytext=(0.834, 0.9), xycoords='axes fraction',
            fontsize=11*1.25, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=8.5, lengthB=2.0', lw=2.5, color='k'))

axes.annotate('*', xy=(0.223, 0.6), xytext=(0.223, 0.65), xycoords='axes fraction',
            fontsize=11*1.25, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=4.2, lengthB=2.0', lw=2.5, color='k'))

axes.annotate('*', xy=(0.278, 0.75), xytext=(0.278, 0.8), xycoords='axes fraction',
           fontsize=11*1.25, ha='center', va='bottom',
          arrowprops=dict(arrowstyle='-[, widthB=8.33, lengthB=2.0', lw=2.5, color='k'))

axes.annotate('*', xy=(0.335, 0.85), xytext=(0.335, 0.9), xycoords='axes fraction',
           fontsize=11*1.25, ha='center', va='bottom',
          arrowprops=dict(arrowstyle='-[, widthB=12.5, lengthB=2.0', lw=2.5, color='k'))

plt.text(s='Kruskal-Wallis Test p-value = 0.041244626235673584', x=5.3, y=4.5, fontsize=12, ha='center', va='center')
plt.text(s='Kruskal-Wallis Test p-value = 0.07205091172127985', x=5.3, y=4.3, fontsize=12, ha='center', va='center')

plt.show()

# And here starts even more beautiful plot =)

df = pd.DataFrame(nest_list)

df.reindex(range(9,29))

constanta = np.array([1, 1, 1, 1, 1, 1, 1, 1]).astype('float64')

new_df1 = df1_mean1.to_numpy().astype('float64')
new_df2 = df1_mean2.to_numpy().astype('float64')
new_df3 = df1_mean3.to_numpy().astype('float64')
new_df4 = df1_mean4.to_numpy().astype('float64')
new_df5 = df1_mean5.to_numpy().astype('float64')
new_df6 = df1_mean6.to_numpy().astype('float64')
new_df7 = df1_mean7.to_numpy().astype('float64')
new_df8 = df1_mean8.to_numpy().astype('float64')
new_df9 = df1_mean9.to_numpy().astype('float64')

model1 = np.poly1d(np.polyfit(constanta, new_df1, 2))
model2 = np.poly1d(np.polyfit(constanta, new_df2, 2))
model3 = np.poly1d(np.polyfit(constanta, new_df3, 2))
model4 = np.poly1d(np.polyfit(constanta, new_df4, 2))
model5 = np.poly1d(np.polyfit(constanta, new_df5, 2))
model6 = np.poly1d(np.polyfit(constanta, new_df6, 2))
model7 = np.poly1d(np.polyfit(constanta, new_df7, 2))
model8 = np.poly1d(np.polyfit(constanta, new_df8, 2))
model9 = np.poly1d(np.polyfit(constanta, new_df9, 2))


#add fitted polynomial line to scatterplot
polyline = np.linspace(1, 60, 50)

plt.plot(polyline, model1(polyline), color='green')
plt.plot(polyline, model2(polyline), color='red')
plt.plot(polyline, model3(polyline), color='yellow')
plt.plot(polyline, model4(polyline), color='mediumblue')
plt.plot(polyline, model5(polyline), color='magenta')
plt.plot(polyline, model6(polyline), color='purple')
plt.plot(polyline, model7(polyline), color='pink')
plt.plot(polyline, model8(polyline), color='olive')
plt.plot(polyline, model9(polyline), color='crimson')

plt.legend(['Group 1','Group 2', 'Group 3','Group 4','Group 5','Group 6','Group 7','Group 8','Group 9'])

plt.savefig('/home/asik/Документы/foo2.png')
ax = Image('/home/asik/Документы/foo2.png')
ax = plt.gca()

line1 = ax.lines[0]
xy1 = line1.get_xydata()

line2 = ax.lines[1]
xy2 = line2.get_xydata()


line3 = ax.lines[2]
xy3 = line3.get_xydata()

line4 = ax.lines[3]
xy4 = line4.get_xydata()


line5 = ax.lines[4]
xy5 = line5.get_xydata()


line6 = ax.lines[5]
xy6 = line6.get_xydata()


line7 = ax.lines[6]
xy7 = line7.get_xydata()


line8 = ax.lines[7]
xy8 = line8.get_xydata()


line9 = ax.lines[8]
xy9 = line9.get_xydata()
print(xy9)


control2 = array([[1.463, 0.371]])

# Calculate and add to plot one-way ANOVA test


plt.text(s='One-Way ANOVA Test p-value: 0.000080783181500288', x=30.3, y=2150.5, fontsize=12, ha='center', va='center')
plt.text(s='One-Way ANOVA Test p-value: 0.000000000159714685921131', x=30.3, y=2080.3, fontsize=12, ha='center', va='center')

plt.show()
