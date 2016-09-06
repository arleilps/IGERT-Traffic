import networkx
import math
import scipy.optimize
import numpy
import sys
from scipy import linalg
import matplotlib.pyplot as plt
from IPython.display import Image
import pywt
import scipy.fftpack
import random
import operator
import copy
from collections import deque
from sklearn.preprocessing import normalize
from sklearn.cluster import SpectralClustering
import os

def set_f(G,F):
	"""
		Sets values to vertices
	"""
	i = 0
	for v in G.nodes():
		G.node[v]["value"] = F[i]
		i = i + 1

def get_f(G):
	"""
		Collects values from vertices
	"""
	F = []
	for v in G.nodes():
		F.append(G.node[v]["value"])
	
	return numpy.array(F)

def rgb_to_hex(r,g,b):
	return '#%02x%02x%02x' % (r,g,b)

def rgb(minimum, maximum, value):
	"""
		Assigns colors based on values
	"""
	mi, ma = float(minimum), float(maximum)
	ratio = 2 * (value-mi) / (ma - mi)
	b = int(max(0, 255*(1 - ratio)))
	r = int(max(0, 255*(ratio - 1)))
	g = 255 - b - r
	
	return rgb_to_hex(r, g, b)

def draw_graph_with_values(G, dot_output_file_name, maximum=None, minimum=None):
	"""
		Draws a graph with vertex colors based on values and using graphviz
	"""
	output_file = open(dot_output_file_name, 'w')
	output_file.write("graph G{\n")
	output_file.write("rankdir=\"LR\";\n")
	output_file.write("size=\"10,2\";\n")

	if maximum is None:
		maximum = -sys.float_info.max
		minimum = sys.float_info.max

		for v in G.nodes():
			if G.node[v]["value"] > maximum:
				maximum = G.node[v]["value"]
	     
			if G.node[v]["value"] < minimum:
		 		minimum = G.node[v]["value"]

	for v in G.nodes():
		color = rgb(minimum, maximum, G.node[v]["value"])
		if G.node[v]["value"] != 0.0:
			output_file.write("\""+str(v)+"\" [shape=\"circle\",label=\"\",style=filled,fillcolor=\""+str(color)+"\",penwidth=\"2\",fixedsize=true,width=\"1\",height=\"1\"];\n")
		else:
			output_file.write("\""+str(v)+"\" [shape=\"circle\",label=\"\",style=filled,fillcolor=\""+str(color)+"\",penwidth=\"0\",fixedsize=true,width=\"1\",height=\"1\"];\n")

	for edge in G.edges():
		output_file.write("\""+str(edge[0])+"\" -- \""+str(edge[1])+"\"[dir=\"none\",color=\"black\",penwidth=\"1\"];\n")

	
	output_file.write("}")

	output_file.close()

