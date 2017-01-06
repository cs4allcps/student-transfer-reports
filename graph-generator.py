#incoding: utf-8

import networkx as nx
import matplotlib.pyplot as plt
import csv

def generate_graph(filepath):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py 
	and outputs a graph object representing the data therein.
	'''
	schoolName = filepath.split('/')[-1][:-4]
	g = nx.Graph()
	g.add_node('schoolName')
	with open(filepath) as f:
		reader = csv.reader(f, skipinitialspace=True)
		header = next(reader)
		for row in reader:
			school = dict(zip(header, row))
			g.add_node(school['School Name'], code = school['School Code'])
			g.add_edge(schoolName, school['School Name'], weight = school['Count'])
	return g

def draw_graph(filepath):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py 
	and displays a graph representing the data therein.
	'''
	g = generate_graph(filepath)
	nx.draw(g)
	plt.show()

def save_graph(input_filepath, output_filepath):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py and
	saves a .png file containing a graph representing the data therein.
	'''
	g = generate_graph(input_filepath)
	nx.draw(g)
	plt.save(output_filepath)

