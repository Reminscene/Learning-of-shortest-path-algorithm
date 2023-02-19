# 靡不有初，鲜克有终
# 开发时间：2023/2/19 14:46
import pandas as pd
import json
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import geometry
import read_network as rn

fpath_node = "C://Users//张晨皓//Desktop//最短路算法学习//data//node.csv"
Node_df = pd.read_csv(fpath_node, sep=",")
fpath_link = "C://Users//张晨皓//Desktop//最短路算法学习//data//link.csv"
Link_df = pd.read_csv(fpath_link, sep=",")


def show_shortest_path(path_lst, destination):  # 输入由结点id组成的最短路结果（列表）、目的地id，可视化输出路径
    corrent_node_id = destination
    former_node_id = path_lst[rn.node_id_lst.index(corrent_node_id)]
    path = []
    while former_node_id != 0:
        corrent_node_id_x = list(Node_df[Node_df['node_id'] == corrent_node_id]['x_coord'])[0]
        corrent_node_id_y = list(Node_df[Node_df['node_id'] == corrent_node_id]['y_coord'])[0]
        former_node_id_x = list(Node_df[Node_df['node_id'] == former_node_id]['x_coord'])[0]
        former_node_id_y = list(Node_df[Node_df['node_id'] == former_node_id]['y_coord'])[0]
        path.append([(corrent_node_id_x, corrent_node_id_y), (former_node_id_x, former_node_id_y)])
        corrent_node_id = former_node_id
        former_node_id = path_lst[rn.node_id_lst.index(corrent_node_id)]
    path_gdf = gpd.GeoSeries([geometry.MultiLineString(path )], index=['a'])
    with open("C://Users//张晨皓//Desktop//最短路算法学习//data//node.json",'r',encoding='utf8') as fp1:
        node_json = json.load(fp1)
        node_gdf = gpd.GeoDataFrame.from_features(node_json["features"])
    with open("C://Users//张晨皓//Desktop//最短路算法学习//data//link.json",'r',encoding='utf8') as fp2:
        link_json = json.load(fp2)
        link_gdf = gpd.GeoDataFrame.from_features(link_json["features"])
    fig, ax = plt.subplots(figsize=(10, 10), dpi=60)
    ax = link_gdf.plot(ax=ax, lw=2, edgecolor='black', facecolor=None, zorder=1)
    ax = path_gdf.plot(ax=ax, lw=3, edgecolor='red', facecolor=None, zorder=2)
    ax = node_gdf.plot(ax=ax, lw=2, edgecolor='blue', facecolor='yellow', markersize = 150, zorder=3)
    for i in range(0, len(Node_df)):
        x = Node_df.loc[i, 'x_coord']+3000
        y = Node_df.loc[i, 'y_coord']+3000
        label = Node_df.loc[i, 'node_id']
        plt.text(x, y, str(label), family='serif', style='italic',fontsize=15, verticalalignment="bottom", ha='left', color='blue')
    plt.savefig("C://Users//张晨皓//Desktop//最短路算法学习//figure//最短路径.png")
    plt.show()


if __name__ == "__main__":
    MultiLine_lst = []
    for i in range(0, len(Link_df)):
        start_id = Link_df.loc[i, "from_node_id"]
        end_id = Link_df.loc[i, "to_node_id"]
        start_id_x = list(Node_df[Node_df['node_id'] == start_id]['x_coord'])[0]
        start_id_y = list(Node_df[Node_df['node_id'] == start_id]['y_coord'])[0]
        end_id_x = list(Node_df[Node_df['node_id'] == end_id]['x_coord'])[0]
        end_id_y = list(Node_df[Node_df['node_id'] == end_id]['y_coord'])[0]
        MultiLine_lst.append([(start_id_x,start_id_y), (end_id_x,end_id_y)])
    Node_gdf = gpd.GeoDataFrame(Node_df, geometry=gpd.points_from_xy(Node_df.x_coord, Node_df.y_coord))
    Link_gdf = gpd.GeoSeries([geometry.MultiLineString(MultiLine_lst)], index=['a'])

    # 保存网络结点和路段的json文件
    with open('C://Users//张晨皓//Desktop//最短路算法学习//data//node.json', 'w') as f:
        f.write(Node_gdf.to_json())
    with open('C://Users//张晨皓//Desktop//最短路算法学习//data//link.json', 'w') as f:
        f.write(Link_gdf.to_json())
    # 调取json并可视化展示
    with open("C://Users//张晨皓//Desktop//最短路算法学习//data//node.json",'r',encoding='utf8') as fp1:
        node_json = json.load(fp1)
        node_gdf = gpd.GeoDataFrame.from_features(node_json["features"])
    with open("C://Users//张晨皓//Desktop//最短路算法学习//data//link.json",'r',encoding='utf8') as fp2:
        link_json = json.load(fp2)
        link_gdf = gpd.GeoDataFrame.from_features(link_json["features"])
    fig, ax = plt.subplots(figsize=(10, 10), dpi=60)
    ax = link_gdf.plot(ax=ax, lw=2, edgecolor='black', facecolor=None, zorder=1)
    ax = node_gdf.plot(ax=ax, lw=2, edgecolor='blue', facecolor='yellow', markersize = 150, zorder=2)
    for i in range(0, len(Node_df)):
        x = Node_df.loc[i, 'x_coord'] + 3000
        y = Node_df.loc[i, 'y_coord'] + 3000
        label = Node_df.loc[i, 'node_id']
        plt.text(x, y, str(label), family='serif', style='italic', fontsize=15, verticalalignment="bottom", ha='left',
                 color='blue')
    plt.savefig("C://Users//张晨皓//Desktop//最短路算法学习//figure//Sioux_Falls网络.png")
    plt.show()