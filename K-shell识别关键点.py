import networkx as nx
def weighted_k_shell_with_node_weights(graph, node_weights):
    # 初始化每个节点的加权度数
    weighted_degree = {node: sum(data['weight'] for _, data in graph[node].items()) for node in graph.nodes}

    # 初始化k-shell结果字典
    k_shell = {}
    k = 0
    α = 0.5

    while graph.number_of_nodes() > 0:
        # 计算每个节点的综合评分：加权度数 + 节点权重
        composite_score = {node: α * weighted_degree[node] + (1-α)*node_weights[node] for node in graph.nodes}

        # 找出当前最小的综合评分
        min_composite_score = min(composite_score.values())

        # 找出所有满足条件的节点
        to_remove = [node for node, score in composite_score.items() if score <= min_composite_score]

        # 分配这些节点到当前k-shell层
        for node in to_remove:
            k_shell[node] = k

        # 移除这些节点并更新剩余节点的加权度数
        for node in to_remove:
            # 获取该节点的所有邻居
            neighbors = list(graph.neighbors(node))

            # 移除该节点
            graph.remove_node(node)
            del weighted_degree[node]

            # # 更新邻居节点的加权度数
            # for neighbor in neighbors:
            #     if neighbor in graph.nodes:
            #         weighted_degree[neighbor] -= graph[neighbor][node]['weight'] if neighbor in graph[node] else 0
            # 更新邻居节点的加权度数
            for neighbor in neighbors:
                if neighbor in graph.nodes:
                    if neighbor in graph and node in graph[neighbor]:
                        weighted_degree[neighbor] -= graph[neighbor][node].get('weight', 0)
        k += 1

    return k_shell

# 示例用法
if __name__ == "__main__":
    # 创建一个有向图
    G = nx.DiGraph()

    # 添加带权重的边
    edges = [
        ('A', 'B', {'weight': 3}),
        ('A', 'C', {'weight': 2}),
        ('B', 'D', {'weight': 4}),
        ('C', 'D', {'weight': 1}),
        ('D', 'E', {'weight': 5}),
        ('E', 'F', {'weight': 2})
    ]
    G.add_edges_from(edges)

    # 定义节点权重
    node_weights = {
        'A': 2.1,
        'B': 1.1,
        'C': 3.1,
        'D': 2.2,
        'E': 1.1,
        'F': 4.1
    }

    # 计算加权K-shell
    result = weighted_k_shell_with_node_weights(G, node_weights)

    print("加权K-shell分解结果（考虑节点权重）：")
    for node, shell in result.items():
        print(f"节点 {node}: K-shell 层 {shell}")
