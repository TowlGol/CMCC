import numpy as np
import math
import os
import shutil
from scipy.spatial import KDTree

from Balloon import Start_Imitation, Init_Vertex
from data import vdw_radii
from Input_methond import read_positions_and_atom_names_from_file


class cavity():
    def __init__(self):
        self.atom_type_list = None
        self.atom_idx_dict = None
        self.dummy_atom_radii = 1
        self.distanceFromCOMFactor = 1
        # proporties of the loaded cage:
        self.positions = None
        self.atom_names = None
        self.atom_masses = None
        self.atom_vdw = None
        self.n_atoms = 0
        self.filename = None  # original file of the cage (might be needed to conversion to rdkit in case of hydrophobicity calculation)
        self.INT_MAX = 100005
        self.vdwR_dict = {}  # 存储每种原子类型的范德华半径
        # Init_All_DATA()

    def read_file(self, Path, filename):
        """
        从指定文件读取原子位置信息和名称。

        :param filename: 要读取的文件名
        """
        self.__init__()
        self.filename = filename
        self.positions, self.atom_names, self.atom_masses, self.atom_vdw = read_positions_and_atom_names_from_file(
            str(Path) + str(filename))
        self.n_atoms = len(self.positions)

    def distance_point_to_ray(self, point, ray_origin, ray_direction):
        """
            计算点到射线的最短距离。

            :param point: 要计算距离的点
            :param ray_origin: 射线的起始点
            :param ray_direction: 射线的方向
            :return: 点到射线的最短距离
        """
        # 将输入转换为 NumPy 数组以便进行数学运算
        point = np.array(point)
        ray_origin = np.array(ray_origin)
        ray_direction = np.array(ray_direction)

        # 计算射线上的最近点
        t = np.dot(point - ray_origin, ray_direction) / np.dot(ray_direction, ray_direction)

        if t < 0:
            return self.INT_MAX

        nearest_point = ray_origin + t * ray_direction

        # 计算点到射线上的最近点的距离
        distance = np.linalg.norm(point - nearest_point)

        return distance

    def get_atomInfomations(self):
        """
        获取原子的相关信息，包括名称、范德华半径和位置。
        :return: 原子名称、范德华半径字典和位置列表
        """
        return self.atom_names, self.vdwR_dict, self.positions

    def get_nearest_atom(self, origin_point, ray_dir, type):
        """
        根据起始点和射线方向找到最近的原子。
        :param origin_point: 射线起始点
        :param ray_dir: 射线方向
        :param return_type: 返回值类型，int或原点位置
        :return: 最近原子的索引或原点位置
        """

        nearest_atom_index = -1
        nearest_atom_type = -1

        next_point = [origin_point[0] + 0.1 * ray_dir[0], origin_point[1] + 0.1 * ray_dir[1],
                      origin_point[2] + 0.1 * ray_dir[2]]

        for atom_index, cage_name in enumerate(self.atom_names):
            # 获取当前原子位置信息
            atom_type = cage_name
            pos = self.positions[atom_index]
            # 如果原子中心点到当前射线的距离小于半径
            if self.distance_point_to_ray(pos, origin_point, ray_dir) < self.vdwR_dict[atom_type][0]:
                # 当前原子距离球心更近,就取当前原子
                if nearest_atom_index == -1 or math.sqrt(self.distance(origin_point, pos)) < math.sqrt(
                        self.distance(origin_point, self.positions[nearest_atom_index])):
                    nearest_atom_index = atom_index
                    nearest_atom_type = cage_name

        if nearest_atom_index == -1:
            if type == int:
                return nearest_atom_index
            return origin_point

        while self.distance(origin_point, self.positions[nearest_atom_index]) + 0.1 >= \
                self.vdwR_dict[nearest_atom_type][0] and \
                self.distance(origin_point, self.positions[nearest_atom_index]) > self.distance(next_point,
                                                                                                self.positions[
                                                                                                    nearest_atom_index]):
            origin_point = next_point
            next_point = [origin_point[0] + 0.1 * ray_dir[0], origin_point[1] + 0.1 * ray_dir[1],
                          origin_point[2] + 0.1 * ray_dir[2]]
        if type == int:
            return nearest_atom_index
        return origin_point

    def calculate_pore_center(self):
        pore_center = np.array(sum(self.positions[i] for i in range(self.n_atoms))) / len(self.atom_masses)
        return pore_center

    def calculate_volum_by_balloon(self, Path="", centerType=1, times=0):
        pore_center_of_mass, pore_radius = self.calculate_center_and_radius()
        self.atom_type_list = []  # 存储所有原子类型
        cords_dict = {}  # 存储每种原子类型的下标
        self.vdwR_dict = {}  # 存储每种原子类型的范德华半径
        self.atom_idx_dict = {}  # 存储每种原子类型的索引

        for atom_idx, cage_name in enumerate(self.atom_names):
            # atom_type 记录原子名称 pos 当前的原子位置
            atom_type = cage_name
            pos = self.positions[atom_idx]

            # 如果原子类型不在列表中，则添加到列表中
            if atom_type not in self.atom_type_list:
                self.atom_type_list.append(atom_type)

                # 设置字典的默认值并添加范德华半径
                self.vdwR_dict.setdefault(atom_type, []).append(self.atom_vdw[atom_idx])

            # 这两个检索应该会很有用，
            # 添加坐标和索引到相应的字典中 即创造一个根据原子类型搜索位置以及在 atom_names中的下标位置
            cords_dict.setdefault(atom_type, []).append(list(pos))
            self.atom_idx_dict.setdefault(atom_type, []).append(atom_idx)

        pore_center = self.calculate_pore_center()
        # 初始化节点

        balloon_vertex_neighbors = Init_Vertex(times, 1, pore_center_of_mass, pore_center, centerType, self, Path)
        nearest_atom2vertex = []

        # 这里应该计算出每个顶点射出后距离最近的原子，然后开始梯度下降的问题。
        for vertex_idx, vertex in enumerate(balloon_vertex_neighbors):
            nearest_atom2vertex.append(self.INT_MAX)
            for atom_idx, cage_name in enumerate(self.atom_names):
                # 获取当前原子位置信息
                atom_type = cage_name
                pos = self.positions[atom_idx]
                # 如果原子中心点到当前射线的距离小于半径
                if (self.distance_point_to_ray(pos, pore_center_of_mass, [vertex.x - pore_center_of_mass[0],
                                                                          vertex.y - pore_center_of_mass[1],
                                                                          vertex.z - pore_center_of_mass[2]]) <
                        self.vdwR_dict[atom_type][0]):
                    # 当前原子距离球心更近,就取当前原子
                    if (nearest_atom2vertex[vertex_idx] == self.INT_MAX or self.distance(vertex, pos) < self.distance(
                            vertex, self.positions[nearest_atom2vertex[vertex_idx]])):
                        nearest_atom2vertex.pop()
                        nearest_atom2vertex.append(atom_idx)
        Start_Imitation(self.atom_names, self.vdwR_dict, self.positions, nearest_atom2vertex, self.filename)

    def distance(self, vertex_position, atom_position):
        if type(vertex_position) != list:
            x = vertex_position.x - atom_position[0]
            y = vertex_position.y - atom_position[1]
            z = vertex_position.z - atom_position[2]
        else:
            x = vertex_position[0] - atom_position[0]
            y = vertex_position[1] - atom_position[1]
            z = vertex_position[2] - atom_position[2]
        return x * x + y * y + z * z

    def calculate_center_of_mass(self):
        pore_center_of_mass = np.array(sum(self.atom_masses[i] * self.positions[i] for i in range(self.n_atoms))) / sum(
            self.atom_masses)
        return pore_center_of_mass.tolist()

    def Calculate_Cavity(self, fileName, ball_center_type, divide_times, file_input_path="", file_output_path=""):
        fileName = fileName.split(',')
        path = os.path.dirname(os.path.abspath(__file__)) + "/examples"
        for file in fileName:
            self.read_file(file_input_path, file)
            self.calculate_volum_by_balloon(file_input_path, ball_center_type, divide_times)
            filepath = file_input_path + "" + file.split('.')[0] + "_cavity.pdb"
            filepath = filepath.replace("\\", "/")
            try:
                shutil.copy(filepath, file_output_path)
                os.remove(filepath)
            except:
                pos = filepath.rfind("/")  # 查找最后一个"/"的位置
                if pos != -1:
                    filepath = filepath[:pos+1]
                if not file_output_path.endswith("/"):
                    file_output_path += "/"
                if filepath != file_output_path:
                    print("Please check the path!")

    #
    def calculate_center_and_radius(self):
        # 计算孔的质心，使用 RDKit
        pore_center_of_mass = np.array(sum(self.atom_masses[i] * self.positions[i] for i in range(self.n_atoms))) / sum(
            self.atom_masses)

        # 以分子的质心作为孔的质心
        kdtxyzAtoms = KDTree(self.positions, leafsize=20)  # 计算孔原子位置的 KDTree
        distancesFromCOM = kdtxyzAtoms.query(pore_center_of_mass, k=self.n_atoms, p=2)

        # 根据质心到最近原子的距离和一个距离修正因子计算孔的半径
        pore_radius = distancesFromCOM[0][0] * self.distanceFromCOMFactor

        # 根据最近原子的类型、其半径以及虚拟原子的半径，对孔半径进行修正
        pore_radius = pore_radius - 1.01 * vdw_radii[
            self.atom_names[distancesFromCOM[1][0]]] - 1.01 * self.dummy_atom_radii
        if pore_radius < 0:
            pore_radius = 0

        return pore_center_of_mass, pore_radius
