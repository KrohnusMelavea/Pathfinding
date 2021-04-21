from Dijkstra import Node, load_nodes, nodes, dijkstra
from threading import Thread
import pygame, time
pygame.init()

DISPLAY_INFO = pygame.display.Info()
WINDOW_W:int = DISPLAY_INFO.current_w
WINDOW_H:int = DISPLAY_INFO.current_h

window = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.FULLSCREEN)
pygame.display.set_caption("Dijkstra")

font = pygame.font.SysFont("couriernew", 20)

load_nodes("nodes.json")
path:list[str] = dijkstra(nodes, "A", "F")

node_radius:int = 10

running:bool = True
while running:
	#Event Loop
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			#Exit main loop if user presses "ESC" key.
			if event.key == pygame.K_ESCAPE: running = False

	#Clear screen
	window.fill((0, 0, 0))

	#Drawing the connecting lines before the nodes, otherwise it looks weird.
	for node_id in nodes:	#Connections
		node:Node = nodes[node_id]
		for neighbour_id in node.neighbours:
			neighbour:Node = nodes[neighbour_id]
			pygame.draw.line(window, (255, 255, 255), (node.x, node.y), (neighbour.x, neighbour.y), width=1)
	pygame.draw.lines(window, (255, 0, 0), False, 
				   [(nodes[node_id].x, nodes[node_id].y) for node_id in path], width=3)	#path
	for node_id in nodes:	#Nodes
		node:Node = nodes[node_id]
		pygame.draw.circle(window, (255, 255, 255), (node.x, node.y), node_radius)
		window.blit(font.render(node_id, 1, (0, 255, 0)), (node.x + node_radius, node.y - node_radius))
	

	pygame.display.update()

#Unloading the display object before the module makes the closing process feel snappier.
pygame.display.quit()
pygame.quit()