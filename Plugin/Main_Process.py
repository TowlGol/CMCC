import os
import sys
from pymol import cmd
import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expanding Balloon----Cavity Calculation")
        self.master.geometry("400x240")  # 设置窗口大小
        self.master.resizable(False, False)  # 禁止窗口调整大小

        # 创建一个框架以组织界面
        self.frame = tk.Frame(master, padx=10, pady=6)
        self.frame.pack(padx=10, pady=6)

        self.file_path_label = tk.Label(self.frame, text="File Path Input:")
        self.file_path_label.grid(row=0, column=0, sticky="w")

        self.file_path_input = tk.Entry(self.frame, width=40)
        self.file_path_input.grid(row=0, column=1, pady=5)

        self.file_name_label = tk.Label(self.frame, text="File Name:")
        self.file_name_label.grid(row=1, column=0, sticky="w")

        self.file_name_input = tk.Entry(self.frame, width=40)
        self.file_name_input.grid(row=1, column=1, pady=5)

        self.divide_times_label = tk.Label(self.frame, text="Subdivision Times:")
        self.divide_times_label.grid(row=2, column=0, sticky="w")

        self.divide_times_input = tk.Entry(self.frame, width=40)
        self.divide_times_input.grid(row=2, column=1, pady=5)

        self.output_path_label = tk.Label(self.frame, text="Output Path:")
        self.output_path_label.grid(row=3, column=0, sticky="w")

        self.output_path_input = tk.Entry(self.frame, width=40)
        self.output_path_input.grid(row=3, column=1, pady=5)

        self.execute_button = tk.Button(self.frame, text="Execute", command=self.execute_command, bg='blue', fg='white')
        self.execute_button.grid(row=4, columnspan=2, pady=10)

    def add_cavity_to_last_dot(self,input_string):
        # 找到最后一个 '.' 的位置
        last_dot_index = input_string.rfind('.')

        # 如果找到了 '.'
        if last_dot_index != -1:
            # 在最后一个 '.' 前面添加 '_cavity'
            return input_string[:last_dot_index] + '_cavity' + input_string[last_dot_index:]
        else:
            # 如果没有找到 '.', 返回原字符串
            return input_string


    def execute_command(self):
        file_path = self.file_path_input.get()
        file_name = self.file_name_input.get()
        divide_times = self.divide_times_input.get()
        output_path = self.output_path_input.get()
        file_namelist = file_name.split(",")
        file_path_output = output_path

        command = f"balloon.Calculate_Cavity('{file_name}', '2', '{divide_times}', r'{file_path}/', r'{file_path_output}/')"
        cmd.do(command)
        for name in file_namelist:
            output_filename = self.add_cavity_to_last_dot(name)
            command = f"load {file_path_output}/{output_filename},{output_filename}"
            cmd.do(command)

def run_gui():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

# 确保Python可以找到你的包
plugin_dir = os.path.dirname(__file__)
sys.path.append(plugin_dir)

# 插件入口函数
def __init_plugin__(self=None):

    # for path in sys.path:
    #     if os.path.exists(os.path.join(path, 'startup')):
    #         print(f"Dir: {os.path.join(path, 'startup')}")

    try:
        from Expanding_Balloon.Cavity_Calculation import cavity
        print("import Expanding_Balloon success")
    except ImportError as e:
        print(f"import Expanding_Balloon failed: {e}")

    cmd.do("from Expanding_Balloon.Cavity_Calculation import cavity")
    cmd.do("balloon = cavity()")
    cmd.extend("start_balloon_gui", run_gui)

# PyMOL命令函数
def pymol_Calculate_Cavity(fileName, ball_center_type, subdivision_time, Path=""):
    fileName = str(fileName)
    ball_center_type = str(ball_center_type)
    subdivision_time = int(subdivision_time)
    Path = str(Path)
    Calculate_Cavity(fileName, ball_center_type, subdivision_time, Path)
