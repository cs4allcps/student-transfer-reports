#incoding: utf-8

import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(filename):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py 
	and outputs a graph object representing the data therein.
	'''
	schoolName = filename.split('/')[-1][:-4]
	g = nx.Graph()
	g.add_node('schoolName')
	with open(filename) as f:
		reader = csv.reader(f, skipInitialspace = True)
		header = next(reader)
		for row in reader:
			school = dict(zip(header, row))
			g.add_node(school['School Name'], code = school['School Code'])
			g.add_edge(schoolName, school['School Name'], weight = school['Count'])
	return g

def draw_graph(filename):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py 
	and displays a graph representing the data therein.
	'''
	g = generate_graph(filename)
	nx.draw(g)
	plt.show()

def save_graph(input_filename, output_filename):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py and
	saves a .png file containing a graph representing the data therein.
	'''
	g = generate_graph(input_filename)
	nx.draw(g)
	plt.save(output_filename)

