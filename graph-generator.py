#incoding: utf-8

import networkx as nx

def generate_graph(filename):
	'''
	Takes a .csv file outputted from student-transfer-reports.py 
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
