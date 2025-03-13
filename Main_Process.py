from Cavity_Calculation import cavity
cav = cavity()
Path = "examples/"
Output_Path = "examples/"
# split name by ","
#    Dataset 1:
fileName = "B1.pdb,B2.pdb,B3.pdb,B4.pdb,B5.pdb,B6.pdb,B7.pdb,B8.pdb,B9.pdb,B10.pdb,B11.pdb,B12.pdb,B13.pdb"
#    Dataset 2:
# fileName = "A1.pdb,C1.pdb,F1.pdb,F2.pdb,H1.pdb,N1.pdb,O1.pdb,O2.pdb,W1.pdb"
# 1.Centroid 2.Center of Mass 3.Symmetrical Point
ball_center_type = 2
# recommend 3, 4, and 5
subdivision_time = 4
cav.Calculate_Cavity(fileName, ball_center_type, subdivision_time,Path,Output_Path)