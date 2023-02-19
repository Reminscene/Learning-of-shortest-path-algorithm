import read_network as rn
import copy
import generate_background_json as gbj


def dijkstra(origin):  # 输入起点id，输出从起点到其他结点的最短路距离，以及最短路径
    passed = [origin]
    no_passed = copy.deepcopy(rn.node_id_lst)
    no_passed.remove(origin)
    dis = copy.deepcopy(rn.matrix[rn.node_id_lst.index(origin)])  # 相当于标签，label
    # 使用lam来存储最优路径
    lam = [999 for i in range(0, len(dis))]
    for i in range(0, len(rn.matrix[rn.node_id_lst.index(origin)])):
        if rn.matrix[rn.node_id_lst.index(origin)][i] != 999:
            lam[i] = origin
    lam[rn.node_id_lst.index(origin)] = 0
    while len(no_passed):  # 选择最小的标签对应的结点放入pass
        id_min = no_passed[0]
        # 贪心算法
        for i in no_passed:  # i是结点的id, # 在no_pass的结点里面找到最小的标签，及其对应的结点id，id_min
            if dis[rn.node_id_lst.index(i)] <= dis[rn.node_id_lst.index(id_min)]:
                id_min = i
        # 更新标签
        passed.append(id_min)
        no_passed.remove(id_min)
        for i in no_passed:
            if dis[rn.node_id_lst.index(id_min)] + rn.matrix[rn.node_id_lst.index(id_min)][rn.node_id_lst.index(i)] <= dis[rn.node_id_lst.index(i)]:
                dis[rn.node_id_lst.index(i)] = dis[rn.node_id_lst.index(id_min)] + rn.matrix[rn.node_id_lst.index(id_min)][rn.node_id_lst.index(i)]
                lam[rn.node_id_lst.index(i)] = id_min
    return dis, lam


if __name__ == "__main__":
    source = 3
    destination = 15
    print('最短路距离为', dijkstra(source)[0][rn.node_id_lst.index(destination)])
    gbj.show_shortest_path(dijkstra(source)[1], destination)  # 从source出发，到达9结点的最短路

