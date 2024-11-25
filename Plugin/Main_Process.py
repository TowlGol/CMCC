import os
import sys
from pymol import cmd
import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expanding Balloon----Cavity Calculation")
        self.master.geometry("400x300")  # 设置窗口大小
        self.master.resizable(False, False)  # 禁止窗口调整大小

        # 创建一个框架以组织界面
        self.frame = tk.Frame(master, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.file_path_label = tk.Label(self.frame, text="File Path Input:")
        self.file_path_label.grid(row=0, column=0, sticky="w")

        self.file_path_input = tk.Entry(self.frame, width=40)
        self.file_path_input.grid(row=0, column=1, pady=5)

        self.file_name_label = tk.Label(self.frame, text="File Name:")
        self.file_name_label.grid(row=1, column=0, sticky="w")

        self.file_name_input = tk.Entry(self.frame, width=40)
        self.file_name_input.grid(row=1, column=1, pady=5)

        self.divide_times_label = tk.Label(self.frame, text="Divide Times:")
        self.divide_times_label.grid(row=2, column=0, sticky="w")

        self.divide_times_input = tk.Entry(self.frame, width=40)
        self.divide_times_input.grid(row=2, column=1, pady=5)

        self.ball_center_type_label = tk.Label(self.frame, text="Ball Center Type:")
        self.ball_center_type_label.grid(row=3, column=0, sticky="w")

        self.ball_center_type_input = tk.Entry(self.frame, width=40)
        self.ball_center_type_input.grid(row=3, column=1, pady=5)

        self.execute_button = tk.Button(self.frame, text="Execute", command=self.execute_command, bg='blue', fg='white')
        self.execute_button.grid(row=4, columnspan=2, pady=10)

    def execute_command(self):
        file_path = self.file_path_input.get()
        file_name = self.file_name_input.get()
        divide_times = self.divide_times_input.get()
        ball_center_type = self.ball_center_type_input.get()
        
        file_path_output = os.path.dirname(os.path.abspath(__file__)) + "/Extension_Balloon/examples"
        
        command = f"balloon.Calculate_Cavity('{file_name}', '{ball_center_type}', '{divide_times}', r'{file_path}/', r'{file_path_output}/')"
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

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'startup')):
            print(f"插件目录: {os.path.join(path, 'startup')}")

    try:
        from Extension_Balloon.Cavity_Calculation import cavity
        print("成功导入 cavity 模块")
    except ImportError as e:
        print(f"导入 cavity 模块失败: {e}")

    cmd.do("from Extension_Balloon.Cavity_Calculation import cavity")
    cmd.do("balloon = cavity()")
    cmd.extend("start_balloon_gui", run_gui)

# PyMOL命令函数
def pymol_Calculate_Cavity(fileName, ball_center_type, divide_times, Path=""):
    fileName = str(fileName)
    ball_center_type = str(ball_center_type)
    divide_times = int(divide_times)
    Path = str(Path)
    Calculate_Cavity(fileName, ball_center_type, divide_times, Path)
