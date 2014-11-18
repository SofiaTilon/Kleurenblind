'''
13/11/2014
graphs.py
Insert nodes/edges from a csv file into a graph file,
assign colors to nodes for visualisation. Connecting 
nodes are supposed to have different colors. Goal: use
the least amount of colours necessary. 
'''

import networkx as nx
import matplotlib.pyplot as plt
import csv

# constants
CSV_FILENAME = "con2.csv"
COLOR_LIST = ["y", "w", "b", "g", "r"]

def populate_graph(vertices, edges):
	'''
	Populate the graph with the vertices/edges.
	@param vertices: list containing every vertex
	@param edges: list of tuples containing the connections
	'''
	# create graph
	temp_graph = nx.Graph()

	# populate graph with vertices/edges
	temp_graph.add_nodes_from(vertices)
	temp_graph.add_edges_from(edges)

	# return populated graph
	return temp_graph

def create_vertices(filename):
	'''
	Create list of vertices from csv.
	@param filename: csv file to be read
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

def draw_save_graph(graph, filename):
	'''
	Draw the elements of the graph (nodes/edges/labels/axis)
	& Save the figure to disk.
	@param graph: input graph file
	@param filename: output filename	
	'''
	# spatial distribution of the nodes
	# k = val between 0 and 1, controls distance between nodes
	coordinates = nx.spring_layout(graph, k=0.07, iterations=45)

	# color algorithm to color the nodes
	color_algorithm(graph, COLOR_LIST, coordinates)
	
	# draw the edges/labels/turn axis off
	nx.draw_networkx_edges(graph, coordinates, width=0.3, alpha=0.5)
	nx.draw_networkx_labels(graph, coordinates, font_size=8)
	plt.axis('off')

	# save to disk
	plt.savefig(filename)

def color_algorithm(graph, colorlist, coordinates):
	'''
	Algorithm to color the nodes.
	@param graph: input graph file
	@colorlist: list of colors to assign to nodes
	@coordinates: dictionary containing vertices and their xy data
	'''

	# create color dictionary to store colors
	color_dictionary = {}
	for vertex in graph:
		color_dictionary[vertex] = ''

	# create function that sorts the vertices from
	# most to least neighbors


	# for every node in the graph
	for vertex in graph:

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


		# draw the vertex with the assigned color
		nx.draw_networkx_nodes(graph, coordinates, nodelist=[vertex]\
						,node_color=node_color, node_size=100, alpha=0.5)

		# update the color dictionary
		color_dictionary[vertex] = node_color

	# print "this is the color_dictionary:", color_dictionary

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

	# draw the graph
	draw_save_graph(new_graph, "new_graph.jpg")

if __name__ == '__main__':
	main()

