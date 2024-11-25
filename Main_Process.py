# import sys
# print(sys.path)
# from Extension_Balloon.Cavity_Calculation import cavity

from Cavity_Calculation import cavity


cav = cavity()
Path = "examples/"
fileName = "A1.pdb"
ball_center_type = 2
division_times = 5
cav.Calculate_Cavity(fileName, ball_center_type, division_times,Path,Path)