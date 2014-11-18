'''
13/11/2014
algorithm.py
Insert nodes/edges from a csv file into a graph file,
assign colors to nodes for visualisation. Connecting 
nodes are supposed to have different colors. Goal: use
the least amount of colours necessary. 
'''

import networkx as nx
import matplotlib.pyplot as plt
import csv
import random

# constants
CSV_FILENAME = "con1.csv"
COLOR_LIST = ["y", "w", "b", "g", "r", "k"]
ITERATIONS = 10000

def populate_graph(edges):
	'''
	Populate the graph with the edges.
	@param edges: list of tuples containing the connections
	'''
	# create graph
	temp_graph = nx.Graph()

	# populate graph with edges (vertices added from edges)
	temp_graph.add_edges_from(edges)

	# return populated graph
	return temp_graph

def create_edges(filename):
	'''
	Create list of edges from csv.
	@param filename: csv file to be read
	'''
	edges = []

	# append entries to edges list, strip trailing whitespaces
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			tup = (row[0], str.strip(row[1]))
			edges.append(tup)

	return edges

def color_algorithm(graph, colorlist):
	'''
	Algorithm to color the nodes.
	@param graph: input graph file
	@colorlist: list of colors to assign to nodes
	'''

	used_colors_list = []

	# create color dictionary (store colors) and vertices list
	color_dictionary = {}
	vertices = []
	for vertex in graph:
		color_dictionary[vertex] = ''
		vertices.append(vertex)

	# randomize the vertices' order
	random.shuffle(vertices)

	# for every vertex in vertices list
	for vertex in vertices:

		# create a list of neighbors, and find their colors
		neighbors = graph.neighbors(vertex)
		neighbor_colors = []

		for neighbors in neighbors:
			neighbor_colors.append(color_dictionary[neighbors])

		# find a color that is not in use by the neighbors
		node_color = '' 

		for i in range(len(colorlist)):
			if colorlist[i] not in neighbor_colors:
				node_color = colorlist[i]

		# update the color dictionary
		color_dictionary[vertex] = node_color

		if node_color not in used_colors_list and node_color != '':
			used_colors_list.append(node_color);

	return len(used_colors_list), used_colors_list, vertices


################### main function ######################

def main():
	'''
	Graph functions
	'''
	# get edges from csv
	edges = create_edges(CSV_FILENAME)

	# create graph and populate with edges/vertices
	new_graph = populate_graph(edges)


	# write to csv file
	b = open('new.csv', 'wb')
	a = csv.writer(b)
	for i in range(ITERATIONS):
		a.writerows([color_algorithm(new_graph, COLOR_LIST)])
	b.close()


# run it :)
if __name__ == '__main__':
	main()

