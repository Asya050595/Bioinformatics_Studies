from IPython.display import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
import scipy
from scipy import stats
from scipy.stats import median_test
from scipy import interpolate
from io import StringIO
from scipy.optimize import curve_fit
from scipy.stats import f_oneway

#Get raw data and process it

path1 = 'ELISA1.xlsx'
path2 = 'ELISA2.xlsx'


df1 = pd.read_excel(path1, usecols = [1,2,3,4,5,6,7,8,9,10,11,12, 13], sheet_name='RawData')
df1.rename(columns={df1.columns[0]:"Lunki", df1.columns[1]: "1", df1.columns[2]:"2", df1.columns[3]:"3", df1.columns[4]:"4", df1.columns[5]:"5", \
           df1.columns[6]: "6", df1.columns[7]: "7", df1.columns[8]:"8", df1.columns[9]: "9", df1.columns[10]: "10", df1.columns[11]: "11", \
           df1.columns[12]: "12"}, inplace = True)

df2 = pd.read_excel(path2, usecols = [1, 2,3,4,5,6], sheet_name='RawData')
df2.rename(columns={df2.columns[0]:"Lunki", df2.columns[1]: "1", df2.columns[2]:"2", df2.columns[3]:"3", df2.columns[4]:"4", df2.columns[5]:"5"}, inplace = True)

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


df2_mean2 = df2["2"][2:10]
df2_mean3 = df2["3"][2:10]
df2_mean4 = df2["4"][2:10]
df2_mean5 = df2["5"][2:8]



dfs = [df1_mean1, df1_mean2, df1_mean3, df1_mean4, df1_mean5, df1_mean6, df1_mean7, df1_mean8, \
       df1_mean9, df1_mean10, df1_mean11, df1_mean12, df2_mean2, df2_mean3, df2_mean4, df2_mean5]
dfs_concat = pd.concat(dfs)
df_list = dfs_concat.tolist()


number_of_groups = int(input("Number of groups: "))
number_of_mice = int(input("Number of mice per group: "))



def round_robin_sublists(l, number_of_mice):
    lists = [[] for _ in range(number_of_groups)]
    i = 0
    for elem in l:
        lists[i].append(elem)
        i = (i + 1) % number_of_mice
    return lists


my_lst = []
for i in range(1, len(df_list)):
    if i == 0 or i % 2 != 0:
        numbers = (df_list[i]+df_list[i-1])/2
        my_lst.append(numbers)
        nest_list = round_robin_sublists(my_lst, number_of_groups)

#export processed data to output file

with open('mean_data_ELISA.xlsx', 'w', encoding='utf-8') as file:
    file.write(str(nest_list))


print(nest_list)

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

fig.suptitle('Kruskal-Wallis Test = 61.98253197745673, p-value = 2.4172623988169253e-07', fontsize=15)

plt.show()

# Assess median with Kruskal test

mediana = [0.331, 0.332]

result1 = stats.kruskal(mediana, df1_mean1, df1_mean2, df1_mean3, df1_mean4, df1_mean5, df1_mean6, df1_mean7, df1_mean8, \
                       df1_mean9, df1_mean10, df1_mean11, df1_mean12, df2_mean2, df2_mean3, df2_mean4, df2_mean5)

print(result1)

# Here starts beautiful boxplot + scatterplot =)

x1 = [1, 1, 1, 1, 1, 1, 1]
y1 = nest_list[0]

x2 = [2, 2, 2, 2, 2, 2, 2]
y2 = nest_list[1]

x3 = [3, 3, 3, 3, 3, 3, 3]
y3 = nest_list[2]

x4 = [4, 4, 4, 4, 4, 4, 4]
y4 = nest_list[3]

x5 = [5, 5, 5, 5, 5, 5, 5]
y5 = nest_list[4]

x6 = [6, 6, 6, 6, 6, 6, 6]
y6 = nest_list[5]

x7 = [7, 7, 7, 7, 7, 7, 7]
y7 = nest_list[6]

x8 = [8, 8, 8, 8, 8, 8, 8]
y8 = nest_list[7]

x9 = [9, 9, 9, 9, 9, 9, 9]
y9 = nest_list[8]



bplot = plt.boxplot([nest_list[0], nest_list[1], nest_list[2], nest_list[3], nest_list[4], nest_list[5], nest_list[6], nest_list[7], nest_list[8]], \
                    showfliers=False, whis=(10, 90), boxprops=dict(alpha=0.5), patch_artist=True)
colors = ['peachpuff', 'peachpuff', 'peachpuff']

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.scatter([x1, x2, x3, x4, x5, x6, x7, x8, x9], [y1, y2, y3, y4, y5, y6, y7, y8, y9], s=150, c='firebrick')

plt.title('Kruskal-Wallis Test = 61.98253197745673, p-value = 2.4172623988169253e-07', fontsize=15)

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

plt.savefig('foo.png')
ax = Image('foo.png')
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


mediana2 = array([[0.331, 0.332]])

# Calculate and add to plot one-way ANOVA test

s, p = f_oneway(mediana2, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9)
result2 = f_oneway(mediana2, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9)
print(result2)
plt.title('One-Way ANOVA: {}. p-value: {}'.format(s, p))
plt.show()
