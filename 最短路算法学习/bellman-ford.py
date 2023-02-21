# 靡不有初，鲜克有终
# 开发时间：2023/2/20 22:11
import read_network as rn
import copy
import generate_background_json as gbj


def bellman_ford(origin):  # 输入起点id，输出从起点到其他结点的最短路距离，以及最短路径
    dis = list(copy.deepcopy(rn.matrix[rn.node_id_lst.index(origin)]))  # 相当于标签
    dis_pre = copy.deepcopy(dis)
    lam = [999 for i in range(0, len(dis))]  # 使用lam来存储最优路径
    for i in range(0, len(dis)):
        if dis[i] != 999:
            lam[i] = origin
    lam[rn.node_id_lst.index(origin)] = 0
    k = 0
    while dis_pre != dis or k == 0:
        dis_pre = copy.deepcopy(dis)
        for i in range(0, len(rn.network.link_list)):
            a_id = rn.network.link_list[i].from_node_id
            b_id = rn.network.link_list[i].to_node_id
            weight = rn.network.link_list[i].length
            a_index = rn.node_id_lst.index(a_id)
            b_index = rn.node_id_lst.index(b_id)
            if dis[a_index] + weight < dis[b_index]:  # 松弛
                dis[b_index] = dis[a_index] + weight
                lam[b_index] = a_id
        k += 1
        if k > len(dis)-1:
            print("存在负环，最短路距离无意义")
            break
    return dis, lam


if __name__ == "__main__":
    source = 1
    destination = 15
    print('从结点', source, '到结点', destination, '的最短路距离为', bellman_ford(source)[0][rn.node_id_lst.index(destination)])
    # print(bellman_ford(source)[1])
    gbj.show_shortest_path(bellman_ford(source)[1], destination)  # 从source出发，到达destination的最短路
