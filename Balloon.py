import math
import time
import os
import warnings
import pymeshlab as ml
import numpy as np
from Bio.PDB import *
from Bio.PDB.PDBExceptions import PDBConstructionWarning

cavity = []

# 是否是第一次扩展
first_extension = True
# 膨胀次数
extension_times = 0
# 当前体积大小
volume = 1
# 球心
balloon_center = []
# 气球顶点邻居位置
balloon_vertex_neighbors = {}
# 气球顶点邻居下标
balloon_index_neighbors = []
# 节点是否仍可扩展
balloon_vertex_extensible = {}
# 距离当前节点最近的节点
balloon_nearest_atom2vertex = []
# 存储已经画出的三角形,防止重复绘制
exist = {}
# 初始状态拷贝
balloon_vertex_copy = {}
# list 状态的 balloon_vertex_neighbors.keys()
list_neighbors = []
# 是否召回过 通过设置
balloon_vertex_recall = []
# 顶点分组
balloon_vertex_group = []

# 是否完成扩展
extension_finished = False
balloon_extension_origin = []
balloon_extension_vector = []

file_name = ""
balloon_influence = []
# 限制条件
balloon_influence_condition = []

# 原子种类
atom_names = []
# 范德华半径
vdwR_dict = []
# 原子位置
atom_positions = []
# 原子球面三角形
Faces = []
# 所有的三角形顶点
npTriangle = []

# 三角形顶点数量
vertex_count = 0
# 球体顶点数量
balloon_vertex_count = 0
# 气球顶点
balloon_triangle = []
# 原子顶点数量
atom_vertex_count = 0
# atom 三角形顶点
atom_triangle = []
# 是否更新球体顶点数量
balloon_vertex_count_update = True
# 是否更新原子顶点数量
atom_vertex_count_update = True
# 对当前节点影响最大的点
balloon_vertex_influence_min = {}
# 最大数量
INT_MAX_COUNT = 100005
# 路径
Path = ""


def Init_All_DATA():
    global cavity
    global first_extension
    global extension_times
    global volume
    global balloon_center
    global balloon_vertex_neighbors
    global balloon_index_neighbors
    global balloon_vertex_extensible
    global balloon_nearest_atom2vertex
    global exist
    global balloon_vertex_copy
    global list_neighbors
    global balloon_vertex_recall
    global balloon_vertex_group
    global extension_finished
    global balloon_extension_origin
    global balloon_extension_vector
    global file_name
    global balloon_influence
    global balloon_influence_condition
    global atom_names
    global vdwR_dict
    global atom_positions
    global Faces
    global npTriangle
    global vertex_count
    global balloon_vertex_count
    global balloon_triangle
    global atom_vertex_count
    global atom_triangle
    global balloon_vertex_count_update
    global atom_vertex_count_update
    global balloon_vertex_influence_min
    global INT_MAX_COUNT
    global Path
    cavity = []

    # 是否是第一次扩展
    first_extension = True
    # 膨胀次数
    extension_times = 0
    # 当前体积大小
    volume = 1
    # 球心
    balloon_center = []
    # 气球顶点邻居位置
    balloon_vertex_neighbors = {}
    # 气球顶点邻居下标
    balloon_index_neighbors = []
    # 节点是否仍可扩展
    balloon_vertex_extensible = {}
    # 距离当前节点最近的节点
    balloon_nearest_atom2vertex = []
    # 存储已经画出的三角形,防止重复绘制
    exist = {}
    # 初始状态拷贝
    balloon_vertex_copy = {}
    # list 状态的 balloon_vertex_neighbors.keys()
    list_neighbors = []
    # 是否召回过 通过设置
    balloon_vertex_recall = []
    # 顶点分组
    balloon_vertex_group = []

    # 是否完成扩展
    extension_finished = False
    balloon_extension_origin = []
    balloon_extension_vector = []

    file_name = ""
    balloon_influence = []
    # 限制条件
    balloon_influence_condition = []

    # 原子种类
    atom_names = []
    # 范德华半径
    vdwR_dict = []
    # 原子位置
    atom_positions = []
    # 原子球面三角形
    Faces = []
    # 所有的三角形顶点
    npTriangle = []

    # 三角形顶点数量
    vertex_count = 0
    # 球体顶点数量
    balloon_vertex_count = 0
    # 气球顶点
    balloon_triangle = []
    # 原子顶点数量
    atom_vertex_count = 0
    # atom 三角形顶点
    atom_triangle = []
    # 是否更新球体顶点数量
    balloon_vertex_count_update = True
    # 是否更新原子顶点数量
    atom_vertex_count_update = True
    # 对当前节点影响最大的点
    balloon_vertex_influence_min = {}
    # 最大数量
    INT_MAX_COUNT = 100005
    # 路径
    Path = ""


class XYZ:
    """
        function: Point结构体。
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        if type(x) == list:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def __hash__(self):
        return hash((self.x * 10000, self.y * 10000, self.z * 10000))

    def __eq__(self, other):
        return isinstance(other, XYZ) and self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        if type(other) == list:
            try:
                return XYZ(self.x + other[0], self.y + other[1], self.z + other[2])
            except:
                return self
        return XYZ(self.x + other.x, self.y + other.y, self.z + other.z)

    def __distance__(self, other):
        if type(other) == list:
            x = (self.x - other[0])
            y = (self.y - other[1])
            z = (self.z - other[2])
        else:
            x = (self.x - other.x)
            y = (self.y - other.y)
            z = (self.z - other.z)

        return x * x + y * y + z * z

    def __list__(self):
        return list([self.x, self.y, self.z])


def init_atom(_atom_names, _vdwR_dict, _positions):
    """
    function: 初始化元素信息
    :param _atom_names: 元素名称列表，例如 ['H', 'O', 'C']
    :param _vdwR_dict: 范德华半径字典，例如 {'H': 1.2, 'O': 1.52, 'C': 1.7}
    :param _positions: 原子三维坐标列表，例如 [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
    :return: None
    """
    global atom_names
    global vdwR_dict
    global atom_positions

    # 初始化全局变量
    atom_names = _atom_names
    vdwR_dict = _vdwR_dict
    atom_positions = _positions


def update_vertex_neighbors(triangle):
    """
    function: 设计顶点邻接表。
    :param triangle: 三角面片信息，包含三个顶点
    :return: None
    """
    global balloon_vertex_neighbors, balloon_index_neighbors

    # 遍历三角形的每个顶点
    for v in triangle:
        # if v not in balloon_vertex_neighbors :
        if not balloon_vertex_neighbors.__contains__(v):
            balloon_vertex_neighbors[v] = []  # 初始化邻接表

    # 更新邻接关系
    for i in range(3):
        # 将相邻顶点添加到集合中
        balloon_vertex_neighbors[triangle[i]].append(triangle[(i + 1) % 3])
        balloon_vertex_neighbors[triangle[i]].append(triangle[(i + 2) % 3])


def find_neighborIndex(vertex_neighbor):
    """
    function: 根据位置获取顶点索引
    :param vertex_neighbor: 顶点位置，类型为 XYZ 或者其他可以比较的类型
    :return: 顶点索引，类型为 int，如果未找到则返回 None
    """
    # 遍历所有的邻接顶点
    for i, v in enumerate(balloon_vertex_neighbors):
        # 检查当前顶点是否与给定的邻接顶点相同
        if v == vertex_neighbor:
            return i  # 返回找到的索引

    return None  # 如果未找到，返回 None


def update_index_neighbors():
    """
        function: 更新邻居下标信息。
        :param: None
        :return: None
    """
    global balloon_index_neighbors, balloon_vertex_neighbors
    index = 0
    vertex_dic = {}
    for i, v in enumerate(balloon_vertex_neighbors.keys()):
        vertex_dic[v] = i

    for v, neighbors in balloon_vertex_neighbors.items():
        balloon_index_neighbors.append([])
        for vertex_neighbor in neighbors:
            balloon_index_neighbors[index].append(vertex_dic[vertex_neighbor])
        index += 1


def distSquare(a, b):
    """
    function: 欧氏距离计算
    :param a: 顶点 a，类型为 XYZ
    :param b: 顶点 b，类型为 XYZ
    :return: 距离，类型为 float
    """
    # 计算每个坐标轴上的差值
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z

    # 计算并返回欧氏距离
    return math.sqrt(dx * dx + dy * dy + dz * dz)


# 球体中位点
def midArcPoint(a, b):
    """
    function: 计算球面中点。
    :param a: 顶点 a，类型为 XYZ
    :param b: 顶点 b，类型为 XYZ
    :return: 球面中点，类型为 XYZ
    """
    c = XYZ(a.x + b.x, a.y + b.y, a.z + b.z)
    mod = math.sqrt(c.x * c.x + c.y * c.y + c.z * c.z)
    c.x /= mod
    c.y /= mod
    c.z /= mod
    return c


def normalization(point):
    """
    function: 对三维点进行归一化处理
    :param point: 三维坐标点，格式为列表或数组
    :return: 归一化后的三维坐标点
    """
    length = np.linalg.norm(point)
    return [point[0] / length, point[1] / length, point[2] / length]


def distance_vertex_atom_center(vertex, atom_center):
    """
        function: 计算距离
        :param vertex: 顶点坐标，可以是 XYZ 对象或坐标列表
        :param atom_center: 原子中心坐标，可以是 XYZ 对象或坐标列表
        :return: 顶点到原子中心的平方距离
    """
    if type(vertex) == XYZ and type(atom_center) != XYZ:
        x = vertex.x - atom_center[0]
        y = vertex.y - atom_center[1]
        z = vertex.z - atom_center[2]
    if type(vertex) == XYZ and type(atom_center) == XYZ:
        x = vertex.x - atom_center.x
        y = vertex.y - atom_center.y
        z = vertex.z - atom_center.z
    if type(vertex) != XYZ and type(atom_center) == XYZ:
        x = vertex[0] - atom_center.x
        y = vertex[1] - atom_center.y
        z = vertex[2] - atom_center.z
    if type(vertex) != XYZ and type(atom_center) != XYZ:
        x = vertex[0] - atom_center[0]
        y = vertex[1] - atom_center[1]
        z = vertex[2] - atom_center[2]

    return x * x + y * y + z * z


def collision_influence(influence_point, atom_center):
    """
        function: 碰撞限制扩散。
        :param influence_point: 碰撞顶点下标
        :param atom_center: 最近元素位置
        :return: None
    """
    global balloon_index_neighbors, balloon_nearest_atom2vertex
    global balloon_influence, balloon_influence_condition
    global list_neighbors
    list_neighbors = list(balloon_vertex_neighbors.keys())

    # 传递序列，无线距离的碰撞影响会进行传递的
    influence_arry = []

    # 对当前的相邻节点进行标记
    for index in balloon_index_neighbors[influence_point]:
        result = np.array(balloon_influence_condition[index].__contains__(list_neighbors[influence_point].__list__()))
        if not result.any():
            # 使用顶点进行召回
            balloon_influence[index].append(2)
            balloon_influence_condition[index].append(list_neighbors[influence_point].__list__())

        # 将碰撞的原子中心加入影响因素之中
        exis = False
        for j, tmp_list in enumerate(balloon_influence_condition[index]):
            # 影响是1 并且 已经保存过当前的节点
            if balloon_influence[index][j] == 1 and list(atom_center) == list(tmp_list):
                exis = True
                break
        if exis == False:
            # 由于邻接节点碰撞到导致的限制 使用原子球进行限制
            balloon_influence[index].append(1)
            balloon_influence_condition[index].append(list(atom_center))

            # 如果当前被影响的节点会传递到无限远处，那么这个限制应该被传递
            if balloon_nearest_atom2vertex[index] == INT_MAX_COUNT:
                if influence_arry.__contains__(index) == False:
                    influence_arry.append(index)

    # 向所有的无限远扩散点进行限制
    for index in influence_arry:
        for i in balloon_index_neighbors[index]:
            result = np.array(balloon_influence_condition[i].__contains__(list_neighbors[influence_point].__list__()))
            if not result.any():
                # 使用顶点进行召回
                balloon_influence[i].append(2)
                balloon_influence_condition[i].append(list_neighbors[influence_point].__list__())
            # 如果当前节点影响过
            exis = False
            for tmp_list in balloon_influence_condition[i]:
                if list(atom_center) == list(tmp_list):
                    exis = True
                    break
            if exis == False:
                # 添加影响因素以及因素点
                balloon_influence[i].append(1)
                balloon_influence_condition[i].append(list(atom_center))

                # 将当前影响因素添加进这个内容之中，如果用__contain__方法会更快一些 not in 会有卡顿
                if balloon_nearest_atom2vertex[i] == INT_MAX_COUNT:
                    if influence_arry.__contains__(i) == False:
                        influence_arry.append(i)


def extension_influence_judgement(vertex_index, new_vertex, old_vertex):
    """
        function: 判断顶点是否可以进行扩展
        :param vertex_index: 顶点索引
        :param new_vertex: 扩展后顶点的位置
        :param old_vertex: 扩展前顶点的位置
        :return: 是否允许扩展
    """
    global balloon_influence, balloon_influence_condition
    global balloon_index_neighbors, balloon_vertex_extensible, balloon_vertex_neighbors
    global balloon_center

    judgement_result = True

    min_distance = INT_MAX_COUNT
    neighbors_distance_sum = 0
    step_len = distance_vertex_atom_center(new_vertex, old_vertex)

    for index, condition in enumerate(balloon_influence[vertex_index]):
        # 根据每一个限制条件进行
        # 传递过来的限制条件
        if condition == 1:
            atom_center = balloon_influence_condition[vertex_index][index]

            # 这是对斜边的整个的影响
            distance_newvertex_atom = distance_vertex_atom_center(new_vertex, atom_center)
            distance_oldvertex_atom = distance_vertex_atom_center(old_vertex, atom_center)
            distance = distance_newvertex_atom - distance_oldvertex_atom

            neighbors_distance_sum += distance
            if distance < min_distance:
                balloon_vertex_influence_min[vertex_index] = atom_center

            judgement_result = judgement_result and distance < 0
            if step_len < neighbors_distance_sum:
                # judgement_result = False
                return False

    sum_radis = 0
    num = 0
    avg = INT_MAX_COUNT
    list_neighbors = list(balloon_vertex_neighbors.keys())
    for index in balloon_index_neighbors[vertex_index]:
        if balloon_vertex_extensible.keys().__contains__(index):
            if balloon_vertex_extensible[index] == False:
                sum_radis += distance_vertex_atom_center(list_neighbors[index], balloon_center)
                num += 1
        else:
            num = -INT_MAX_COUNT
            break

    # 如果大于当前的一半的点
    if num > len(balloon_index_neighbors[vertex_index]) / 2:
        return False

    return True


def calculate_centroid(vertices):
    """
        function: 计算顶点数组中心点
        :param: 顶点数组
        :return: 中心点坐标
    """
    sum_x, sum_y, sum_z = 0.0, 0.0, 0.0
    N = len(vertices)

    # 累加顶点坐标
    for vertex in vertices:
        sum_x += vertex[0]
        sum_y += vertex[1]
        sum_z += vertex[2]

    # 计算中心顶点的坐标
    centroid_x = sum_x / N
    centroid_y = sum_y / N
    centroid_z = sum_z / N

    return (centroid_x, centroid_y, centroid_z)


def find_plane_from_points(P1, P2):
    """
        function: 计算平面方程。
        :param: 顶点，平面
        :return: （x,y,z）
    """
    x1, y1, z1 = P1
    x2, y2, z2 = P2

    # 计算法向量
    A = x2 - x1
    B = y2 - y1
    C = z2 - z1

    # 计算 D
    D = - (A * x1 + B * y1 + C * z1)

    return (A, B, C, D)


def get_plane(vertices):
    """
        function: 获取回归平面方程。
        :param: 周围顶点位置信息数组
        :return: 平面方程
    """
    global balloon_center
    center = calculate_centroid(vertices)
    plane = find_plane_from_points(center, balloon_center)
    return plane


def get_group(index):
    """
        function: 获取顶点分组。
        :param index: 顶点的下标
        :return: 顶点的分组索引
    """
    global balloon_vertex_group

    if balloon_vertex_group[index] == -1:
        return -1

    if index != balloon_vertex_group[index]:
        return get_group(balloon_vertex_group[index])
    return index


def project_point_to_plane(C, plane):
    """
        function: 求出顶点到平面的映射。
        :param C: 顶点坐标 (x, y, z)
        :param plane: 平面的参数 (A, B, C, D)，表示平面方程 Ax + By + Cz + D = 0
        :return: 投影点的坐标 (x_p, y_p, z_p)
    """
    x_c, y_c, z_c = C
    A, B, C, D = plane

    # 平面法向量
    normal = (A, B, C)

    # 计算平面法向量的模
    normal_magnitude = math.sqrt(A ** 2 + B ** 2 + C ** 2)

    # 计算点到平面的距离
    d = (A * x_c + B * y_c + C * z_c + D) / normal_magnitude

    # 计算投影点坐标
    x_p = x_c - d * (A / normal_magnitude)
    y_p = y_c - d * (B / normal_magnitude)
    z_p = z_c - d * (C / normal_magnitude)

    return (x_p, y_p, z_p)


# 对于每一组数据咱们采用多顶点拟合平面的方式
def recall():
    """
        function: 球面顶点召回
        :param: None
        :return: None
    """
    global balloon_vertex_neighbors
    global list_neighbors
    global balloon_center
    global balloon_influence
    global balloon_nearest_atom2vertex
    global balloon_vertex_group
    global atom_positions

    balloon_vertex_group = []
    list_neighbors = list(balloon_vertex_neighbors.keys())

    # 判断当前是否进行过分组，如果 分组过则为 True 没分组为 False
    grouped_list = []

    # 初始化默认值
    for i, index in enumerate(balloon_nearest_atom2vertex):
        if index == INT_MAX_COUNT:
            balloon_vertex_group.append(i)
            grouped_list.append(False)
        else:
            balloon_vertex_group.append(-1)
            grouped_list.append(True)

    # 存储所有inf节点的下标
    inf_vertex_list = []

    for i, index in enumerate(balloon_nearest_atom2vertex):
        if balloon_vertex_group[i] != -1:
            inf_vertex_list.append(i)

    # 进行分组
    for i, index in enumerate(inf_vertex_list):
        # 如果是inf的
        if not grouped_list[index]:
            # 把当前节点加入list之中，然后开始扩散
            list_extension = [index]
            grouped_list[index] = True

            # 从下标为 j 这个点进行扩散
            for j in list_extension:
                neighbor_index_list = balloon_index_neighbors[j]

                # 扩散到 k
                for k in neighbor_index_list:
                    if not grouped_list[k]:
                        list_extension.append(k)
                        grouped_list[k] = True
                        balloon_vertex_group[k] = get_group(j)
    # 分组没问题
    # 分组数组
    groups = set()
    # 分组中心
    group_dic = {}
    # 分组数量
    groups_count = {}
    for i in balloon_vertex_group:
        if i != -1:
            groups.add(i)

    for i in groups:
        group_dic[i] = [0, 0, 0]
        groups_count[i] = 0

    for index, i in enumerate(balloon_vertex_group):
        if i != -1:
            group_dic[i] = [group_dic[i][0] + list_neighbors[index].x, group_dic[i][1] + list_neighbors[index].y,
                            group_dic[i][0] + list_neighbors[index].z]
            groups_count[i] += 1

    for i in groups:
        group_dic[i] = [group_dic[i][0] / groups_count[i], group_dic[i][1] / groups_count[i],
                        group_dic[i][2] / groups_count[i]]

    # 每个点到中心的距离
    groups_distance = {}
    # 每个点的下标编号
    groups_index = {}
    # 临近的节点坐标的List
    groups_near = {}
    # 临近的原子
    group_near_atom = {}
    # 根据分组找他们最近的三个碰撞的节点

    for i in groups:
        groups_distance[i] = []
        groups_index[i] = []
        groups_near[i] = []
        group_near_atom[i] = set()

    # 召回后的key数值
    recall_list = []

    for j, vertex in enumerate(list_neighbors):
        recall_list.append(vertex.__list__())

    for i in groups:
        for j, vertex in enumerate(list_neighbors):
            if balloon_vertex_group[j] == -1:
                is_near = False
                for k in balloon_index_neighbors[j]:
                    if get_group(k) == i:
                        is_near = True
                        break
                if is_near:
                    groups_near[i].append(vertex.__list__())
                    group_near_atom[i].add(XYZ(list(atom_positions[balloon_nearest_atom2vertex[j]])))
                    groups_index[i].append(j)

        plane = get_plane(groups_near[i])
        cou = 0
        for j, vertex in enumerate(list_neighbors):
            if get_group(j) == i:
                try:
                    recall_list[j] = list(project_point_to_plane(recall_list[j], plane))
                except:
                    cou += 1

    new_neighbors = {}
    for index, vertex in enumerate(recall_list):
        if distance_vertex_atom_center(list_neighbors[index], balloon_center) < distance_vertex_atom_center(vertex,
                                                                                                            balloon_center):
            XYZ_vertex = list_neighbors[index]
        else:
            XYZ_vertex = XYZ(vertex[0], vertex[1], vertex[2])
        while new_neighbors.keys().__contains__(XYZ_vertex):
            XYZ_vertex = XYZ_vertex.__add__(XYZ(0.00005, 0.00005, 0.00005))
        new_neighbors[XYZ_vertex] = []

    key_list = list(new_neighbors.keys())
    for i, index_list in enumerate(balloon_index_neighbors):
        for j in index_list:
            new_neighbors[key_list[i]].append(key_list[j])

    balloon_vertex_neighbors = new_neighbors
    list_neighbors = list(balloon_vertex_neighbors.keys())


def extension_sphere():
    """
        function: 球面顶点扩散
        :param: None
        :return: None
    """
    # volume 指的是膨胀的倍数
    global balloon_vertex_neighbors
    global balloon_nearest_atom2vertex
    global balloon_vertex_copy
    global balloon_center
    global volume
    global balloon_vertex_count_update, balloon_index_neighbors
    global list_neighbors
    global extension_finished
    global balloon_extension_origin

    if extension_finished:
        return
    # 需要更新球体节点
    # print("balloon_center = "+str(balloon_center[0])+" "+str(balloon_center[1])+" "+str(balloon_center[2])+" ")
    balloon_vertex_count_update = True
    new_neighbors = {}
    stop_extension_count = 0
    # 判断当前点下次是否可以扩展
    for i, vertex in enumerate(balloon_vertex_neighbors.keys()):
        x = balloon_extension_origin[i][0]
        y = balloon_extension_origin[i][1]
        z = balloon_extension_origin[i][2]

        nx = x + balloon_extension_vector[i][0] * volume
        ny = y + balloon_extension_vector[i][1] * volume
        nz = z + balloon_extension_vector[i][2] * volume

        new_vertex = XYZ(nx, ny, nz)
        atom_center = []

        # 获取当前距离最近的节点
        if balloon_nearest_atom2vertex[i] != INT_MAX_COUNT:
            atom_center = atom_positions[balloon_nearest_atom2vertex[i]]

        index = balloon_nearest_atom2vertex[i]

        # 如果当前是 无限点 或者 下一步会距离节点更近
        if balloon_nearest_atom2vertex[i] == INT_MAX_COUNT or len(balloon_vertex_extensible) == i \
                or distance_vertex_atom_center(new_vertex, atom_center) < distance_vertex_atom_center(vertex,
                                                                                                      atom_center) \
                and vdwR_dict[atom_names[index]][0] * vdwR_dict[atom_names[index]][0] < distance_vertex_atom_center(
            new_vertex, atom_positions[index]):
            # 当前节点为 无限点 and 当前节点无法再次扩展
            if balloon_vertex_extensible.keys().__contains__(i) and balloon_vertex_extensible[i] == False:
                stop_extension_count += 1
                continue
            # 根据 周围节点的限制 以及 距离限制
            balloon_vertex_extensible[i] = extension_influence_judgement(i, new_vertex, vertex)

        #     如果上一次可以扩展，这次不可以扩展了，那么我们进行一次扩散
        elif balloon_vertex_extensible[i] == True:

            # 当前是因为碰撞不可以在扩展了
            balloon_vertex_extensible[i] = False
            # 当前点不可以被召回
            balloon_vertex_recall[i] = False
            # 散播碰撞信息
            collision_influence(i, atom_center)

        if balloon_vertex_extensible[i] == False:
            stop_extension_count += 1

    # 如果所有节点全部都受到了
    if stop_extension_count == len(balloon_index_neighbors):
        extension_finished = True
        recall()
        return False

    vertex_index = 0
    # 扩大球体，更新邻居信息
    for vertex, neighbors in balloon_vertex_neighbors.items():
        new_vertex = []
        if balloon_vertex_extensible[vertex_index]:

            x = balloon_extension_origin[vertex_index][0]
            y = balloon_extension_origin[vertex_index][1]
            z = balloon_extension_origin[vertex_index][2]

            nx = x + balloon_extension_vector[vertex_index][0] * volume
            ny = y + balloon_extension_vector[vertex_index][1] * volume
            nz = z + balloon_extension_vector[vertex_index][2] * volume
            # 新的节点位置
            new_vertex = XYZ(nx, ny, nz)

            # 在这里先不管相邻节点,让相邻节点自己去更新,等整个节点更新完了,在通过索引更新相邻节点
        else:
            new_vertex = vertex

        # 添加相邻节点
        new_neighbors[new_vertex] = []
        tmp_List = list(neighbors)
        for i, neighbor in enumerate(tmp_List):
            neighbor_index = balloon_index_neighbors[vertex_index][i]

            if balloon_vertex_extensible[neighbor_index]:
                x = balloon_extension_origin[i][0]
                y = balloon_extension_origin[i][1]
                z = balloon_extension_origin[i][2]

                nx = x + balloon_extension_vector[neighbor_index][0] * volume
                ny = y + balloon_extension_vector[neighbor_index][1] * volume
                nz = z + balloon_extension_vector[neighbor_index][2] * volume
                new_neighbor = XYZ(nx, ny, nz)

            else:
                new_neighbor = neighbor
            new_neighbors[new_vertex].append(new_neighbor)
        vertex_index += 1

    balloon_vertex_neighbors = new_neighbors
    list_neighbors = list(balloon_vertex_neighbors.keys())
    return True


def Init_balloon_influence():
    """
    function: 初始化气球的影响力扩散信息
    :return: None
    """
    global balloon_influence, balloon_vertex_neighbors
    global balloon_extension_origin
    global balloon_extension_vector
    global balloon_center
    list_neighbors = balloon_vertex_neighbors.keys()

    for i, item in enumerate(list_neighbors):
        balloon_influence.append([])
        balloon_influence_condition.append([])

        # 添加扩散起点
        balloon_extension_origin.append([balloon_center[0], balloon_center[1], balloon_center[2]])
        x = item.x - balloon_center[0]
        y = item.y - balloon_center[1]
        z = item.z - balloon_center[2]
        # 添加扩散方向
        balloon_extension_vector.append([x, y, z])


# 初始化球的顶点
def Init_Vertex(time, r, mess_center, center, balloon_center_type, cage_cavity, path):
    """
    function: 初始化球的顶点
    :param time: 初始三角形递归细分的次数
    :param r: 球的半径
    :param mess_center: 质心坐标
    :param center: 球心坐标
    :param balloon_center_type: 球心类型
    :param cage_cavity: 空腔
    :return: None
    """

    # Dictionary to store neighboring vertices
    global balloon_vertex_neighbors
    global balloon_vertex_copy
    global list_neighbors
    global cavity
    global balloon_center
    global Path

    Path = path
    cavity = cage_cavity
    # 三角形数列
    triangles = []
    # 球心
    if balloon_center_type == '1':
        balloon_center = [center[0], center[1], center[2]]
    # 质心
    elif balloon_center_type == '3':

        balloon_center = [center[0] * 2 - mess_center[0], center[1] * 2 - mess_center[1],
                          center[2] * 2 - mess_center[2]]
    # 对称点
    else:
        balloon_center = [mess_center[0], mess_center[1], mess_center[2]]

    #  初始化数值
    triangles.append([XYZ(r, 0, 0), XYZ(0, r, 0), XYZ(0, 0, r), int(time)])

    if len(balloon_vertex_neighbors) != 0:
        return
    while len(triangles) > 0:
        t = triangles[0]
        triangles.pop(0)
        if t[0].__eq__(t[1]) or t[1].__eq__(t[2]) or t[2].__eq__(t[0]):
            continue

        if t[3] != 0:
            d = midArcPoint(t[0], t[1])
            e = midArcPoint(t[1], t[2])
            f = midArcPoint(t[2], t[0])
            triangles.append([t[0], f, d, t[3] - 1])
            triangles.append([t[1], d, e, t[3] - 1])
            triangles.append([t[2], e, f, t[3] - 1])
            triangles.append([d, e, f, t[3] - 1])
        else:
            vertex_point_1 = XYZ(t[0].x, t[0].y, t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(t[1].x, t[1].y, t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(t[2].x, t[2].y, t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # 第二象限
            vertex_point_1 = XYZ(-t[0].x, t[0].y, t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(-t[1].x, t[1].y, t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(-t[2].x, t[2].y, t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # 第三象限
            vertex_point_1 = XYZ(-t[0].x, -t[0].y, t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(-t[1].x, -t[1].y, t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(-t[2].x, -t[2].y, t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            #
            # # 第四象限
            vertex_point_1 = XYZ(t[0].x, -t[0].y, t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(t[1].x, -t[1].y, t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(t[2].x, -t[2].y, t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # # 第五象限
            vertex_point_1 = XYZ(t[0].x, -t[0].y, -t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(t[1].x, -t[1].y, -t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(t[2].x, -t[2].y, -t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # # 第六象限
            vertex_point_1 = XYZ(-t[0].x, -t[0].y, -t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(-t[1].x, -t[1].y, -t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(-t[2].x, -t[2].y, -t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # # 第七象限
            vertex_point_1 = XYZ(-t[0].x, t[0].y, -t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(-t[1].x, t[1].y, -t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(-t[2].x, t[2].y, -t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

            # # 第八象限
            vertex_point_1 = XYZ(t[0].x, t[0].y, -t[0].z).__add__(balloon_center)
            vertex_point_2 = XYZ(t[1].x, t[1].y, -t[1].z).__add__(balloon_center)
            vertex_point_3 = XYZ(t[2].x, t[2].y, -t[2].z).__add__(balloon_center)
            update_vertex_neighbors([vertex_point_1, vertex_point_2, vertex_point_3])

    for i, vertex in enumerate(list(balloon_vertex_neighbors.keys())):
        # 当前点可以被召回
        balloon_vertex_recall.append(True)
        if (type(vertex) == list):
            vertex = XYZ(vertex[0], vertex[1], vertex[2])

        balloon_vertex_copy[i] = [vertex.x - balloon_center[0], vertex.y - balloon_center[1],
                                  vertex.z - balloon_center[2]]

    list_neighbors = list(balloon_vertex_neighbors.keys())
    # 更新邻居信息
    update_index_neighbors()
    # 初始化影响
    Init_balloon_influence()
    return balloon_vertex_neighbors


def read_obj_file(file_path):
    """
    function: 从 OBJ 文件中读取顶点和面片数据。
    :param file_path: 文件路径
    :return: 顶点数组和面片数组
    """
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                # 读取顶点
                parts = line.split()
                vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                vertices.append(vertex)
            elif line.startswith('f '):
                # 读取面片
                parts = line.split()
                # OBJ 文件的面片索引从1开始，因此需要减去1
                face = [int(part.split('/')[0]) - 1 for part in parts[1:]]
                faces.append(face)

    return np.array(vertices), np.array(faces)


def Init_atom_vertex(r, position):
    """
    function: 初始化顶点定点信息
    :param time: 迭代次数，用于细分三角形
    :param r: 气球半径
    :param mess_center: 质心位置 (x, y, z)
    :param center: 球心位置 (x, y, z)
    :param balloon_center_type: 气球中心类型 (1: 球心, 2: 质心, 3: 对称点)
    :param cage_cavity: 笼空腔信息
    :return: None
    """
    floor_num = 4
    pointCount = 6
    Vertexs = []
    step = 2 * r / floor_num
    nowfloor = 0
    angle_step = 360 / pointCount

    if len(Vertexs) == 0:
        while nowfloor < floor_num:
            nowFloor_dep = (nowfloor + 1) * step - r
            r_floor = math.sqrt(r * r - nowFloor_dep * nowFloor_dep)
            angle = 0
            Vertexs.append([])
            # 制造顶点
            while angle < 360:
                if (360 - angle < 0.05):
                    break
                x = r_floor * math.sin(angle * math.pi / 180)
                z = r_floor * math.cos(angle * math.pi / 180)
                Vertexs[nowfloor].append((x + position[0], nowFloor_dep + position[1], z + position[2]))
                angle += angle_step
            nowfloor += 1

    for i, vertex in enumerate(Vertexs):
        length = len(vertex)
        for j, vertex_point in enumerate(vertex):
            # 与最下面的顶点链接
            if i == 0:
                Faces.append([vertex_point, vertex[(j + 1) % length], [position[0], -r + position[1], position[2]]])
            else:
                Faces.append([vertex_point, Vertexs[i - 1][j], Vertexs[i - 1][(j + 1) % length]])
                Faces.append([vertex_point, vertex[(j + 1) % length], vertex[(j + 2) % length]])
            # 顶层的顶点链接
            if i == len(Vertexs) - 1:
                Faces.append([vertex_point, vertex[(j + 1) % length], [position[0], r + position[1], position[2]]])


def compute_normal_vector(point1, point2, point3):
    """
        function: 计算由三个点定义的平面的法向量
        :param point1: 第一个点坐标
        :param point2: 第二个点坐标
        :param point3: 第三个点坐标
        :return: 单位法向量
    """
    vector1 = np.array(point2) - np.array(point1)
    vector2 = np.array(point3) - np.array(point1)
    normal_vector = np.cross(vector1, vector2)
    sum = abs(normal_vector[0]) + abs(normal_vector[1]) + abs(normal_vector[2])
    return [normal_vector[0] / sum, normal_vector[1] / sum, normal_vector[2] / sum]


def calculate_angle(a, b):
    """
        function: 计算两个向量之间的角度
        :param a: 第一个向量
        :param b: 第二个向量
        :return: 两个向量之间的角度（度数）
    """
    a_norm = np.sqrt(np.sum(a[0] * a[0] + a[1] * a[1] + a[2] * a[2]))
    b_norm = np.sqrt(np.sum(b[0] * b[0] + b[1] * b[1] + b[2] * b[2]))
    cos_value = np.dot(a, b) / (a_norm * b_norm)
    arc_value = np.arccos(cos_value)
    angle = arc_value * 180 / np.pi

    if angle > 270:
        angle -= 360

    return angle


def get_extent_vector(point_1, point_2, point_3, origin_point, now_point, result_type=list):
    """
        function: 计算法向量是否与扩散方向相同
        :param: 三角形平面a,b,c,射线起点，射线重点
        :return: True/False
    """
    point_1 = point_1.__list__()
    point_2 = point_2.__list__()
    point_3 = point_3.__list__()
    normal_vector = compute_normal_vector(point_1, point_2, point_3)
    ray_vector = [now_point[0] - origin_point[0], now_point[1] - origin_point[1], now_point[2] - origin_point[2]]
    angle = calculate_angle(normal_vector, ray_vector)
    if angle <= 90 and angle >= -90:
        if result_type == bool:
            return True
        return normal_vector
    if result_type == bool:
        return False
    return [normal_vector[0] * -1, normal_vector[1] * -1, normal_vector[2] * -1]


def save_Calculation_Result():
    """
        function: 计算结果
        :param: None
        :return: None
    """
    global file_name
    global list_neighbors
    global balloon_index_neighbors
    global balloon_center
    global balloon_vertex_neighbors
    global Path

    list_neighbors = list(balloon_vertex_neighbors.keys())
    faces = []

    list_neighbor = []
    for i in list_neighbors:
        point = i.__list__()
        list_neighbor.append([point[0] - balloon_center[0], point[1] - balloon_center[1], point[2] - balloon_center[2]])
    vertices = np.array(list_neighbor)

    index = 0

    all_vertices = []
    all_faces = []
    # 遍历每个原子
    new_vertices = []

    for i, vertex in enumerate(vertices):
        vx, vy, vz = vertex
        new_vertices.append([vx, vy, vz])

    all_vertices.extend(new_vertices)

    face_set = set()
    for index, neighbors_list in enumerate(balloon_index_neighbors):
        for j, neighbors_index in enumerate(neighbors_list):
            if j % 2 == 0:
                tmp = [index, neighbors_list[j], neighbors_list[j + 1]]
                tmp.sort()
                tmp_XYZ = XYZ(tmp)
                if not face_set.__contains__(tmp_XYZ):  # tmp_XYZ not in face_set
                    if get_extent_vector(list_neighbors[index], list_neighbors[neighbors_list[j]],
                                         list_neighbors[neighbors_list[j + 1]], balloon_center,
                                         list_neighbors[index].__list__(), bool):
                        faces.append([index, neighbors_list[j], neighbors_list[j + 1]])
                    else:
                        faces.append([neighbors_list[j + 1], neighbors_list[j], index])
                    face_set.add(tmp_XYZ)

    # 创建新的网格对象并设置顶点和面
    tmp_name = file_name[:-4]
    pdb_out_path = Path
    obj_out_path = Path + "/OBJ/"
    obj_out_path = ""

    vertices = np.asarray(new_vertices, dtype=np.float32)
    faces = np.asarray(faces, dtype=np.int32)

    ms = ml.MeshSet()
    mesh = ml.Mesh(vertices, faces)
    ms.add_mesh(mesh, 'my_mesh')
    ms.save_current_mesh(obj_out_path + tmp_name + '.obj')

    name = tmp_name
    obj_file_path = obj_out_path + name + '.obj'
    pdb_file_path = pdb_out_path + name + '_Cavity.pdb'

    vertices = parse_obj(obj_file_path)
    write_pdb(vertices, pdb_file_path)

    vertices, faces = read_obj_file(obj_out_path + name + '.obj')
    print(f"volume: {volume_of_mesh(vertices, faces)}")

    os.remove(obj_out_path + name + '.obj')
    # 创建pml文件
    # name = name+"_Cavity"
    # pml_name = Path+tmp_name + '.pml'
    # with open(pml_name, 'w') as file:
    #     file.write(f"load " + tmp_name + ".pdb\n")
    #     file.write(f"load " + name +'.pdb' + "\n")
    #
    #     file.write(f"select " + name + "\n")
    #     file.write(f"hide everything, " + name + "\n")
    #     file.write(f"show surface, " + name + "\n")
    #     file.write(f"cmd.color_deep(\"white\", '" + name + "', 0)\n")
    #     file.write(f"util.cba(33,\"" + tmp_name + "\",_self=cmd)\n")


def parse_obj(obj_file_path):
    """
        function: 解析obj文件。
        :param: 问及那路径
        :return: None
    """
    global balloon_center
    vertices = []

    with open(obj_file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.strip().split()
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                nor = normalization([x, y, z])
                vertices.append((x + balloon_center[0] - 1.7 * nor[0], y + balloon_center[1] - 1.7 * nor[1],
                                 z + balloon_center[2] - 1.7 * nor[2]))
    return vertices


def write_pdb(vertices, pdb_file_path):
    global balloon_center
    with open(pdb_file_path, 'w') as file:
        for i, (x, y, z) in enumerate(vertices, start=1):
            file.write(f"ATOM  {i:5d}  C   UNK     1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00           C\n")


def calulate_volme():
    """
        function: 球面单词扩展。
        :param: None
        :return: None
    """
    global volume
    global balloon_nearest_atom2vertex
    global list_neighbors
    global balloon_center

    distance = INT_MAX_COUNT
    min_atom_index = 0

    for i, vertex in enumerate(list_neighbors):
        # 获取当前距离最近的节点
        if balloon_nearest_atom2vertex[i] != INT_MAX_COUNT:
            atom_center = atom_positions[balloon_nearest_atom2vertex[i]]
            tmp_dis = distance_vertex_atom_center(balloon_center, atom_center)
            if math.sqrt(tmp_dis) < math.sqrt(distance):
                distance = tmp_dis
                min_atom_index = balloon_nearest_atom2vertex[i]

    atom_type = atom_names[min_atom_index]
    volume = math.sqrt(distance) - vdwR_dict[atom_type][0] - 0.1
    volume = "{:.1f}".format(volume)
    volume = float(volume)
    # try:
    extension_sphere()
    # except:
    #     volume = 1.1
    #     extension_sphere()


def signed_volume_of_triangle(v1, v2, v3):
    """
    function: 计算三角面片体积。
    :param: 顶点1，2，3
    :return: 三角面体积
    """
    return np.dot(np.cross(v1, v2), v3) / 6.0


def volume_of_mesh(vertices, faces):
    """
        function: 计算由顶点和面片定义的封闭三角网格的体积。
        :param: 顶点坐标，面片索引
        :return: 体积
    """
    volume = 0.0
    for face in faces:
        if len(face) == 4:
            # 将四边形分解为两个三角形
            v1 = vertices[face[0]]
            v2 = vertices[face[1]]
            v3 = vertices[face[2]]
            v4 = vertices[face[3]]
            volume += abs(signed_volume_of_triangle(v1, v2, v3))
            volume += abs(signed_volume_of_triangle(v1, v3, v4))
        elif len(face) == 3:
            # 处理三角形
            v1 = vertices[face[0]]
            v2 = vertices[face[1]]
            v3 = vertices[face[2]]
            volume += abs(signed_volume_of_triangle(v1, v2, v3))
        else:
            raise ValueError("Unsupported face with more than 4 vertices")
    return volume


def run_process():
    """
    function: 计算由顶点和面片定义的封闭三角网格的体积。
    :param: None
    :return: None
    """
    global first_extension
    global extension_times
    global extension_finished
    global volume

    start_time = time.time()
    while extension_finished == False:
        if first_extension:
            calulate_volme()
            first_extension = False
            # break
        else:
            volume = volume + 0.1
            extension_sphere()
            if extension_finished == False:
                extension_times += 1

    save_Calculation_Result()

    end_time = time.time()
    execution_time = end_time - start_time
    print("iteration times: " + str(extension_times))
    print(f"execution time: {execution_time} 秒")


def read_pdb_file(file_name):
    """
        function: 纠正PDB位置信息。
        :param: 文件名称
        :return: None
        """
    global Path

    file_name = Path + file_name
    atom_info = []
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                atom_name = line[12:16].strip()
                element = line[76:78].strip()
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])

                atom_info.append({
                    'name': atom_name,
                    'element': element,
                    'coord': (x, y, z)
                })

    return atom_info


def Start_Imitation(atom_names, vdwR_dict, positions, nearest_atom2vertex, fileName):
    global balloon_nearest_atom2vertex
    global file_name
    file_name = fileName
    balloon_nearest_atom2vertex = nearest_atom2vertex

    if file_name != "":
        init_atom(atom_names, vdwR_dict, positions)
        # for atom_idx, cage_name in enumerate(atom_names):
        #     atom_type = cage_name
        #     # Init_atom_vertex(vdwR_dict[atom_type][0], positions[atom_idx])
    run_process()
    Init_All_DATA()


warnings.simplefilter('ignore', PDBConstructionWarning)