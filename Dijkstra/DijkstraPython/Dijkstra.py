from json import loads
from math import sqrt


def dist(x0:float, y0:float, x1:float, y1:float):
	"""Returns euclidean distance between two sets of x-y coordinates"""
	return sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))

class Node:
	"""Node class with constructor which takes position and list of connected node"""
	t:float = float("inf")		#tentative score
	path:list[str] = []

	def __init__(self, x:float, y:float, neighbours:dict[str,float]):
		self.x:float = x
		self.y:float = y
		self.neighbours:dict[str,float] = neighbours

nodes:dict[str,Node] = {}


def dijkstra(nodes:dict[str,Node], start:str, end:str):
	nodes[start].t:float = 0.0
	nodes[start].path:list[str] = [start,]
	nodes[start].path:list[str] = [start,]

	unvisited:set[str] = set(nodes.keys())
	visited:set[str] = set()

	new_dist:float
	min_dist:float
	min_node:str
	while unvisited:
		min_dist = float("inf")
		for node_id in unvisited:
			if nodes[node_id].t < min_dist:
				min_dist = nodes[node_id].t
				min_node = node_id
		
		unvisited.remove(min_node)
		visited.add(min_node)

		for neighbour_id in nodes[min_node].neighbours:
			if neighbour_id in unvisited:
				new_dist = nodes[min_node].t + nodes[min_node].neighbours[neighbour_id]
				if new_dist < nodes[neighbour_id].t:
					nodes[neighbour_id].t = new_dist
					nodes[neighbour_id].path = nodes[min_node].path + [neighbour_id,]

	return nodes[end].path if len(nodes[end].path) else []




def load_nodes(filepath:str):
	"""Populates a dictionary with data read from a file at the specified location."""
	with open(filepath, "r") as file:
		node_raw:str = file.read()
		node_data:dict = loads(node_raw)
		
		for node_id in node_data:
			node:dict = node_data[node_id]
			#list comprehension to calculate distance between node and its neighbours.
			neighbour:dict[str,float] = dict((neighbour_id, 
				dist(node['x'], node['y'], 
					node_data[neighbour_id]['x'], node_data[neighbour_id]['y'])) 
					for neighbour_id in node['neighbours'])
			nodes[node_id]:Node = Node(node['x'], node['y'], neighbour)

