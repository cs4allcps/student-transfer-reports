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
			g.add_edge(schoolName, school['School Name'], weight = float(school['Count']))
	return g

def draw_graph(filepath):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py 
	and displays a graph representing the data therein.
	'''
	g = generate_graph(filepath)
	edges = g.edges()
	weights = [g[u][v]['weight'] for u,v in edges]
	nx.draw_networkx(g, edges = edges, width = weights, node_shape = [(-150, -10), (150, -10), (150, 10), (-150, 10)], node_size = 20000, font_size = 7)
	plt.show()

def save_graph(input_filepath, output_filepath):
	'''
	Takes a .csv file as outputted from student-transfer-reports.py and
	saves a .png file containing a graph representing the data therein.
	'''
	draw_graph(input_filepath)
	plt.save(output_filepath)

