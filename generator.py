import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt

class ClassGenerator(object):
	"""docstring for ClassGenerator"""
	def __init__(self, n,size,pos=0,disp=1):
		super(ClassGenerator, self).__init__()
		self.n = n
		self.size = size
		self.pos = pos
		self.disp = disp
		
	def generate(self):
		lst = []
		for x in xrange(0,self.n):
			lst.append(self.disp * np.random.randn(2, self.size) + self.pos)
		return lst

class ClassHolder(object):
	"""docstring for ClassHolder"""
	def __init__(self, classes=[]):
		super(ClassHolder, self).__init__()
		self.classes = classes

	def addClass(self,_class):
		self.classes.append(_class)
	
	def average(self,numArray):
		res = np.zeros( (numArray.ndim,1) )
		index = 0
		for dim in numArray:
			avg = 0.0
			for element in dim:
				avg += element
			avg = avg/dim.size
			res[index] = avg
			index += 1
		return res

	def eculedianDistance(self,avg1,avg2):
		return sqrt(pow(avg1[0]-avg2[0],2)+pow(avg1[1]-avg2[1],2))

	def classifier(self,x,limit):
		lst = [	]
		index = 0
		for i in self.classes:
			temp = {"avg":self.eculedianDistance( x,self.average(i) ),"class":i,"index":index}
			lst.append( temp)
			index += 1
		lst.sort(key=lambda x: x['avg'], reverse=False)
		print lst,"\n"
		print lst[0]['avg']," : ",limit
		if float(lst[0]['avg']) > float(limit):
			print "the limit was passed"
			return None
		return 1+lst[0]['index']

	def classify(self):
		colors = ['b', 'g', 'c', 'm', 'y','k']
		x = raw_input("Coordenada x: ")
		y = raw_input("Coordenada y: ")
		p = np.array([[float(x)],[float(y)]])
		limit = raw_input("Limite : ")
		#print p
		#for _class in classes:
		#	print eculedianDistance(p,average(_class))
		result = self.classifier(p,limit)
		print "\n\n result belong to class {}".format(result)
		
		fig = plt.figure()
		ax = fig.add_subplot(111)
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = ax.scatter(_class[0], _class[1], color=colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1
			if cindex == len(colors):
				cindex = 0

		ax.scatter( x, y, color='red', marker='^')
		ax.legend((label),(title),scatterpoints=1,
	        loc='lower left',
	        ncol=3,
	      	fontsize=8)
		#ax.plot(a, b, color='lightblue', linewidth=3)
		#ax.set_xlim(0, 15)
		#ax.set_ylim(0, 15)
		
		plt.show()