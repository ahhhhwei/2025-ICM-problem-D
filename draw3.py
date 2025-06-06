# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.random_graphs.barabasi_albert_graph(100,1)   #生成一个BA无标度网络G
# # G=nx.MultiDiGraph()
# nx.draw(G)
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node('spam')       # adds node "spam"
G.add_nodes_from('spam') # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)
nx.draw(G, with_labels = True)
# 设置标题
plt.title("Complex Directed Graph with Weighted Edges", fontsize=16)

# 显示图形
plt.axis('off')  # 关闭坐标轴
plt.show()