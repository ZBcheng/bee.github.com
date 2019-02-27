import xlrd
import numpy as np
import matplotlib.pyplot as plt
import math
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

	for i in range(0, 319):
		raw_data_y.append(sheet_2_by_name.row_values(i))

	#data_y = raw_data_y[0]
	print(raw_data_X)
	print(raw_data_y)
	greenland = []
	traffic = []
	mountain = []
	industry = []
	neighbor = []

	for item in raw_data_X:
		if item[4] == 5:
			greenland.append(item)
		elif item[4] == 4:
			traffic.append(item)
		elif item[4] == 3:
			mountain.append(item)
		elif item[4] == 2:
			industry.append(item)
		elif item[4] == 1:
			neighbor.append(item)

	def draw(area, title):
		if title == 'greenland':
			col = 'green'
		elif title == 'traffic':
			col = 'blue'
		elif title == 'industry':
			col = 'purple'
		elif title == 'neighbor':
			col = 'red'

		num = []
		distances = []
		box = []
		As = []
		Cd = []
		Cr = []
		Cu = []
		Hg = []
		Ni = []
		Pb = []
		Zn = []


		x = []
		y = []

		y.append(As)
		y.append(Cd)
		y.append(Cr)
		y.append(Cu)
		y.append(Hg)
		y.append(Ni)
		y.append(Pb)
		y.append(Zn)

		dis_area = []
		for item in area:
			for each in mountain:
				distances.append({'number': item[0], 'dis': math.sqrt((item[1] - each[1])**2 + (item[2] - each[2])**2 + (item[3] - each[3])**2)})
			for i in distances:
				box.append(i['dis'])
			for j in distances:
				if j['dis'] == min(box):
					dis_area.append(j)
			box.clear()
			distances.clear()

		for i in range(1, 9):
			if i == 1:
				til = 'As'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][1] < 5.4:
						dis_area.remove(each)
			elif i == 2:
				til = 'Cd'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][2] < 190:
						dis_area.remove(each)
			elif i == 3:
				til = 'Cr'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][3] < 49:
						dis_area.remove(each)
			elif i == 4:
				til = 'Cu'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][4] < 20.4:
						dis_area.remove(each)
			elif i == 5:
				til = 'Hg'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][5] < 51:
						dis_area.remove(each)
			elif i == 6:
				til = 'Ni'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][6] < 19.9:
						dis_area.remove(each)
			elif i == 7:
				til = 'Pb'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][7] < 43:
						dis_area.remove(each)
			elif i == 8:
				til = 'Zn'
				for each in dis_area:
					if raw_data_y[int(each['number']) - 1][8] < 97:
						dis_area.remove(each)
			for each in dis_area:
				x.append(each['dis'])
				y[i - 1].append(raw_data_y[int(each['number']) - 1][i])


			plt.title(title + ' ' + til)
			plt.xlabel('distance')
			plt.ylabel('%')
			plt.grid(True)
			plt.scatter(x, y[i - 1], alpha = 0.5, s = 100, color = col)
			plt.show()
			x.clear()

	draw(greenland, 'greenland')
	draw(traffic, 'traffic')
	draw(industry, 'industry')
	draw(neighbor, 'neighbor')