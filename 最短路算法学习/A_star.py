# 靡不有初，鲜克有终
# 开发时间：2023/2/21 16:32
import read_network as rn
import copy
import generate_background_json as gbj
# 缺点：无法处理带负权的网络


def distance_estimation(current, destination):  # 输入当前点的id和终点id，输出从该点到目标点的欧式距离
    destination_index = rn.node_id_lst.index(destination)
    destination_x = rn.network.node_list[destination_index].x
    destination_y = rn.network.node_list[destination_index].y
    current_index = rn.node_id_lst.index(current)
    current_x = rn.network.node_list[current_index].x
    current_y = rn.network.node_list[current_index].y
    estimation = ((destination_x-current_x)**2+(destination_y-current_y)**2)**0.5

    return estimation/45000


def dijkstra(origin, destination):  # 输入起点id和终点id，输出从起点到终点的最短路距离，以及最短路径
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
    while destination in no_passed:  # 选择最小的标签对应的结点放入pass
        id_min = no_passed[0]
        # 贪心算法
        for i in no_passed:  # i是结点的id, # 在no_pass的结点里面找到“最好优先”（best-first）的结点，及其对应的结点id，id_min
            if dis[rn.node_id_lst.index(i)]+ distance_estimation(i, destination)< dis[rn.node_id_lst.index(id_min)]+ distance_estimation(id_min, destination):
                id_min = i
        # 更新标签
        passed.append(id_min)
        no_passed.remove(id_min)
        for i in no_passed:
            if dis[rn.node_id_lst.index(id_min)] + rn.matrix[rn.node_id_lst.index(id_min)][rn.node_id_lst.index(i)] < dis[rn.node_id_lst.index(i)]:
                dis[rn.node_id_lst.index(i)] = dis[rn.node_id_lst.index(id_min)] + rn.matrix[rn.node_id_lst.index(id_min)][rn.node_id_lst.index(i)]
                lam[rn.node_id_lst.index(i)] = id_min
    return dis, lam


if __name__ == "__main__":
    source = 1
    destination = 15
    print('从结点', source, '到结点', destination, '的最短路距离为', dijkstra(source, destination)[0][rn.node_id_lst.index(destination)])
    print("最短路径为", dijkstra(source, destination)[1])
    gbj.show_shortest_path(dijkstra(source, destination)[1], destination)  # 从source出发，到达destination的最短路