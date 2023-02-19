# 靡不有初，鲜克有终
# 开发时间：2023/2/15 20:27

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl


class Node:  # 定义Node类
    def __init__(self):
        self.node_id = None
        self.x = None
        self.y = None
        self.flow_in_link = []
        self.flow_out_link = []
        self.flow_in_node = []
        self.flow_out_node = []


class Link:  # 定义Link类
    def __init__(self):
        self.link_id = None
        self.length = None
        self.lanes = None
        self.free_speed = None
        self.from_node_id = None
        self.to_node_id = None


class ReadData:  # 读取Sioux_Falls路网数据
    def read_node(self):  # 针对Node类的实例方法,这里的self是ReadData()
        self.node_list = []
        df_node = pd.read_csv('C://Users//张晨皓//Desktop//最短路算法学习//data//node.csv')  # 此文件中的结点id从1开始
        for i in range(0, len(df_node)):
            a = Node()  # 实例化Node
            a.node_id = df_node.loc[i, 'node_id']
            a.x = df_node.loc[i, 'x_coord']
            a.y = df_node.loc[i, 'y_coord']
            self.node_list.append(a)

    def read_link(self):  # 针对Link类的实例方法
        self.link_list = []
        df_link = pd.read_csv('C://Users//张晨皓//Desktop//最短路算法学习//data//link.csv')
        df_node = pd.read_csv('C://Users//张晨皓//Desktop//最短路算法学习//data//node.csv')
        node_uni_lst = list(pd.unique(df_node['node_id']))
        # 存在以下情况：结点id不一定从0开始，结点也不一定连续（可能被删除），为不失一般性做上述处理

        for i in range(0, len(df_link)):
            b = Link()  # 实例化Link
            b.link_id = df_link.loc[i, 'link_id']
            b.length = df_link.loc[i, 'length']
            b.lanes = df_link.loc[i, 'lanes']
            b.free_speed = df_link.loc[i, 'free_speed']
            b.from_node_id = df_link.loc[i, 'from_node_id']
            b.to_node_id = df_link.loc[i, 'to_node_id']

            from_node = self.node_list[node_uni_lst.index(b.from_node_id)]  # 名为from_node的结点实例
            from_node.flow_out_link.append(b.link_id)
            from_node.flow_out_node.append(b.to_node_id)

            to_node = self.node_list[node_uni_lst.index(b.to_node_id)]  # 名为to_node的结点实例
            to_node.flow_in_link.append(b.link_id)
            to_node.flow_in_node.append(b.from_node_id)

            self.link_list.append(b)


network = ReadData()
network.read_node()
network.read_link()

size = len(network.node_list)
matrix = 999*np.ones((size, size))  # 邻接矩阵
node_id_lst = []  # 结点id所构成的列表，
for i in range(0, size):
    node_id_lst.append(network.node_list[i].node_id)
    matrix[i][i] = 0
for i in range(0, len(network.link_list)):
    matrix[node_id_lst.index(network.link_list[i].from_node_id)][node_id_lst.index(network.link_list[i].to_node_id)] = network.link_list[i].length


if __name__ == "__main__":  # 可视化展示并存储
    print("结点", network.node_list[3].node_id, '的横坐标为', network.node_list[3].x, '，纵坐标为', network.node_list[3].y)
    print("邻接矩阵为")
    print(matrix)

    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
    fig, ax = plt.subplots(dpi=90)
    plt.imshow(matrix, vmin=0, vmax=10, cmap='YlGnBu_r',)
    plt.colorbar()
    plt.xlabel("node id")
    plt.ylabel("node id")
    lables = [i for i in range(0, size, 20)]
    plt.xticks(range(0, size, 20), labels=lables, rotation=30)  # x轴刻度
    plt.yticks(range(0, size, 20), labels=lables)
    plt.savefig('C://Users//张晨皓//Desktop//最短路算法学习//figure//邻接矩阵.png')
    plt.show()