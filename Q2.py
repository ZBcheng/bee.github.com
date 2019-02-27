import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
	path = '/Users/bee0_0/Desktop/数学建模/污染问题/工作簿1.xlsx'
	data = xlrd.open_workbook(path)

	sheets = data.sheets()
	sheet_1_by_name = data.sheet_by_name(u'Sheet1')
	sheet_2_by_name = data.sheet_by_name(u'Sheet2')

	raw_data_X = []
	raw_data_y = []

	for i in range(0, 319):
		raw_data_X.append(sheet_1_by_name.row_values(i))

	raw_data_y.append(sheet_1_by_name.col_values(4))

	data_y = raw_data_y[0]

	x = np.array(raw_data_X)
	y = np.array(data_y)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	pull_info = []

	for i in range(0, 318):
		pull_info.append(sheet_2_by_name.row_values(i))

	#污染源比例统计
	pullution = False
	As = 0
	Cd = 0
	Cr = 0
	Cu = 0
	Hg = 0
	Ni = 0
	Pb = 0
	Zn = 0
	total = 0

	for item in pull_info:
		if item[1] > 5.4:
			print('%s As超标'%(item[0]))
			As += 1
			total += 1
			pullution = True
		if item[2] > 190:
			print('%s Cd超标'%(item[0]))
			Cd += 1
			total += 1
			pullution = True
		if item[3] > 49:
			print('%s Cr超标'%(item[0]))
			Cr += 1
			total += 1
			pullution = True
		if item[4] > 20.4:
			print('%s Cu超标'%(item[0]))
			Cu += 1
			total += 1
			pullution = True
		if item[5] > 51:
			print('%s Hg超标'%(item[0]))
			Hg += 1
			total += 1
			pullution = True
		if item[6] > 19.9:
			print('%s Ni超标'%(item[0]))
			Ni += 1
			total += 1
			pullution = True
		if item[7] > 43:
			print('%s Pb超标'%(item[0]))
			Pb += 1
			total += 1
			pullution = True
		if item[8] > 97:
			print('%s Zn超标'%(item[0]))
			Zn += 1
			total += 1
			pullution = True

		pla = int(item[0])
		if pullution == False:
			if x[pla][4] == 5:
				col = 'green'
			elif x[pla][4] == 4:
				col = 'blue'
			elif x[pla][4] == 3:
				col = 'gray'
			elif x[pla][4] == 2:
				col = 'yellow'
			elif x[pla][4] == 1:
				col = 'red'
			ax.scatter(x[pla, 1], x[pla, 2], x[pla, 3], color = col)

		pullution = False
		#被污染地区空间分布


	ax.scatter(x[y == 5, 1], x[y == 5, 2], x[y == 5, 3], color = 'green', label = '公园绿地区')
	ax.scatter(x[y == 4, 1], x[y == 4, 2], x[y == 4, 3], color = 'blue', label = '交通区')
	ax.scatter(x[y == 3, 1], x[y == 3, 2], x[y == 3, 3], color = 'gray', label = '山区')
	ax.scatter(x[y == 2, 1], x[y == 2, 2], x[y == 2, 3], color = 'yellow', label = '工业区')
	ax.scatter(x[y == 1, 1], x[y == 1, 2], x[y == 1, 3], color = 'red', label = '生活区')

	plt.axis('equal')

	ax.set_xlabel('X(m)')
	ax.set_ylabel('Y(m)')
	ax.set_zlabel('Altitude')

	plt.show()

	plt.figure(figsize=(6,9))
	labels = [u'As', 'Cd', 'Cr', 'Cu', 'Hg', 'Ni', 'Pb', 'Zn']
	size = [As / total, Cd / total, Cr / total, Cu / total, Hg / total, Ni / total, Pb / total, Zn / total]
	patches,l_text,p_text = plt.pie(size,labels=labels,
	                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
	                                startangle = 90,pctdistance = 0.6)
	plt.axis('equal')
	plt.show()