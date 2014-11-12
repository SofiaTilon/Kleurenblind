'''
11 nov 14
Functions to import a csv file into a graph & plot graph

'''

import networkx as nx
import graphviz as pgv
import matplotlib.pyplot as plt
import csv

# where the csv file is stored..
CSV_FILENAME = "con2.csv"

def populate_graph(vertices, edges):
	# create graph
	temp_graph = nx.Graph()

	# populate graph with 
	temp_graph.add_nodes_from(vertices)
	temp_graph.add_edges_from(edges)

	# return populated graph
	return temp_graph

def create_vertices(filename):
	'''
	@param filename:	csv file to be read
	'''
	vertices = []

	# append the first entry of every row to vertices list
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] not in vertices:
				vertices.append(row[0])
	return vertices

def create_edges(filename):
	'''
	@param filename:	csv file to be read
	'''
	edges = []

	# append entries to edges list, strip trailing whitespaces
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			tup = (row[0], str.strip(row[1]))
			edges.append(tup)

	return edges

def draw_save_graph(graph, filename):
	'''
	@param graph: 		input graph file
	@param filename: 	output filename	
	'''
	# spatial distribution of the nodes
	# k = val between 0 and 1, controls distance between nodes
	coordinates = nx.spring_layout(graph, k=0.12, iterations=45)

	# draw the nodes
	nx.draw_networkx_nodes(graph, coordinates, node_color='b', node_size=180, alpha=0.5)

	# draw the edges
	nx.draw_networkx_edges(graph, coordinates, width=0.7, alpha=0.2)

	# draw labels
	nx.draw_networkx_labels(graph, coordinates, font_size=8)


	plt.axis('off')

	# save to disk
	plt.savefig(filename)

################### main function ######################

def main():
	'''
	Graph functions
	'''
	# get vertices/edges from csv
	vertices = create_vertices(CSV_FILENAME)
	edges = create_edges(CSV_FILENAME)

	# create graph and populate with vertices/edges
	new_graph = populate_graph(vertices, edges)

	# find neighbors!
	print new_graph.neighbors('7')

	# draw the graph
	draw_save_graph(new_graph, "new_graph.png")

if __name__ == '__main__':
	main()

