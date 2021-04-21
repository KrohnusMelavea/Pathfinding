from multipledispatch import dispatch
from json import loads
from math import sqrt


def dist(x0:float, y0:float, x1:float, y1:float):
	""" Returns euclidean distance between two sets of x-y coordinates"""
	return sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))

class Node:
	f = float("inf")

	def __init__(self, x:float, y:float, neighbours:list[str]):
		self.x:float = x
		self.y:float = y
		self.neighbours:dict[str,float] = dict((neighbour_id, 0.0) for neighbour_id in neighbours)

nodes:dict[str, Node] = {}


def load_nodes(filepath:str):
	"""Populates a dictionary with data read from a file at the specified location."""
	with open(filepath, "r") as file:
		node_raw:str = file.read()
		node_data:dict = loads(node_raw)
		
		for node_id in node_data:
			node:dict = node_data[node_id]
			nodes[node_id]:Node = Node(node['x'], node['y'], node['neighbours'])

