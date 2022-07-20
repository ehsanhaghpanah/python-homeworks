
import pandas as pd
import scipy
import matplotlib.pyplot as plt

def hoo() -> None:
	#Create a Dictionary of series
	d = {
		'Name': pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack', 'Lee','David','Gasper','Betina','Andres']), 
		'Age': pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]), 
		'Rating': pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
		}
	#Create a DataFrame
	df = pd.DataFrame(d)
	df = pd.DataFrame(d)
	print(df.sum())
	print(df.mean())
	print(df.std())
	print(df.describe())

def foo() -> None:
	hist, bin_edges = scipy.histogram([1, 1, 2, 2, 2, 2, 3], bins = range(5))
	# Checking the results
	print ("No. of points in each bin : ", hist)
	print ("Size of the bins          : ", bin_edges)
	# plotting the histogram
	plt.bar(bin_edges[:-1], hist, width = 1)
	plt.xlim(min(bin_edges), max(bin_edges))
	plt.show()  
	labels = 'Cricket', 'Football', 'Hockey', 'F1'
	sizes = [15, 30, 45, 10]
	# labels = 'Cricket', 'Football', 'Hockey', 'F1'
	# sizes = [15, 30, 45, 10]
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels)
	ax1.axis('equal')  
	plt.show()

def goo() -> None:
	labels = 'Cricket', 'Football', 'Hockey', 'F1'
	sizes = [15, 30, 45, 10]
	explode = (0.4, 0.2, 0.2, 0.2) 
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels)
	plt.show()

def doo() -> None:
	labels = 'Cricket', 'Football', 'Hockey', 'F1'
	sizes = [15, 30, 45, 10]
	fig1, ax1 = plt.subplots()
	explode = (0, 0.1, 0, 0) 
	ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
	plt.show()

def joo() -> None:	
	x = ['A', 'B', 'C', 'D', 'E']
	y = [22, 9, 40, 27, 55]
	plt.bar(x, y)
	plt.show()

joo()