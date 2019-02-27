import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
path = '/Users/bee0_0/Desktop/数学建模/污染问题/工作簿1.xlsx'
data = xlrd.open_workbook(path)

sheets = data.sheets()
sheet_1_by_name=data.sheet_by_name(u'Sheet1')

raw_data_X = []
raw_data_y = []

for i in range(0, 319):
	raw_data_X.append(sheet_1_by_name.row_values(i))


raw_data_y.append(sheet_1_by_name.col_values(4))

data_y = raw_data_y[0]

X_train = np.array(raw_data_X)
y_train = np.array(data_y)

x = X_train
y = y_train

print(x)
print(y)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(x[y == 5, 1], x[y == 5, 2], x[y == 5, 3], color = 'orange')
ax.scatter(x[y == 4, 1], x[y == 4, 2], x[y == 4, 3], color = 'blue')
ax.scatter(x[y == 3, 1], x[y == 3, 2], x[y == 3, 3], color = 'green')
ax.scatter(x[y == 2, 1], x[y == 2, 2], x[y == 2, 3], color = 'red')
ax.scatter(x[y == 1, 1], x[y == 1, 2], x[y == 1, 3], color = 'purple')

ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_zlabel('Altitude')

plt.show()



