from igraph import *

g = Graph()
g.add_vertices(4)
g.add_edges([(1,2),(2,3),(0,3)])

plot(g, "graph.png", vertex_label=["A", "B", "C", "D"], vertex_color=["green"])  
