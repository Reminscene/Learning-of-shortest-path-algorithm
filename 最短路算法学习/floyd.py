# 靡不有初，鲜克有终
# 开发时间：2023/2/21 14:51
import read_network as rn
import copy
import numpy as np
import generate_background_json as gbj


def floyd(matrix):  # 输入网络邻接矩阵，输出多源最短路矩阵，以及路径矩阵
    distance = copy.deepcopy(matrix)
    path = np.ones((len(matrix), len(matrix)))
    for i in range(0, len(path)):
        for j in range(0, len(path)):
            path[i][j] = rn.node_id_lst[i]
        path[i][i] = 0
    for i in range(0, len(rn.node_id_lst)):
        for j in range(0, len(rn.node_id_lst)):
            for k in range(0, len(rn.node_id_lst)):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = rn.node_id_lst[k]
    return distance, path


if __name__ == "__main__":
    source = 1
    destination = 15
    source_index = rn.node_id_lst.index(source)
    destination_index = rn.node_id_lst.index(destination)
    print('路网的多源最短路距离为', '\n', floyd(rn.matrix)[0])
    print('路网的多源最短路路径为', '\n', floyd(rn.matrix)[1])
    print('从结点', source, '出发，到达结点', destination, '的最短路的距离是', floyd(rn.matrix)[0][source_index][destination], '\n')
    print('从结点', source, '出发，到达结点', destination, '的最短路的路径是', floyd(rn.matrix)[1][source_index], '\n')
    gbj.show_shortest_path(floyd(rn.matrix)[1][source_index], destination)  # 从source出发，到达destination的最短路


