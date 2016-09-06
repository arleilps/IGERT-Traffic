import networkx
import math
import scipy.optimize
import numpy
import sys
import matplotlib.pyplot as plt
from IPython.display import Image
import random
import operator
import copy
from datetime import datetime, date, time, timedelta

def read_graph(input_graph_name, input_data_name):
	"""
		Reads a graph
	"""
	input_data = open(input_data_name, 'r')
	values = {}
    
	for line in input_data:
		line = line.rstrip()
		vec = line.rsplit(',')
        
		vertex = vec[0]
		value = float(vec[1])
		values[vertex] = value
        
	input_data.close()
    
	G = networkx.Graph()
    
	input_graph = open(input_graph_name, 'r')
    
	for line in input_graph:
		line = line.rstrip()
		vec = line.rsplit(',')
		v1 = vec[0]
		v2 = vec[1]

		if v1 in values and v2 in values:
			G.add_edge(v1,v2, weight=1.)
   
	Gcc=sorted(networkx.connected_component_subgraphs(G), key = len, reverse=True)

	G = Gcc[0]

	values_in_graph = {}

	for v in values.keys():
		if v in G:
			values_in_graph[v] = values[v]
	
	input_graph.close()
	networkx.set_node_attributes(G, "value", values_in_graph)
    
	return G

def read_values(input_data_name, G):
	"""
		Reads vertex values
	"""
	D = {}
	input_data = open(input_data_name, 'r')

	for line in input_data:
		line = line.rstrip()
		vec = line.rsplit(',')

		vertex = vec[0]
		value = float(vec[1])
		D[vertex] = value

	input_data.close()
    
	F = []
	for v in G.nodes():
		if v in D:
			F.append(float(D[v]))
		else:
			F.append(0.)
   
	F = numpy.array(F) 
    
	return F 

def read_all_values(path, num_snapshots, G):
	"""
		Reads values from all snapshots
	"""
	FT = []
	for t in range(num_snapshots):
		in_file = path + "_" + str(t) + ".data"
		F = read_values(in_file, G)
		FT.append(F)
 
	return numpy.array(FT)
