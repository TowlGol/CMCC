load A1.pdb
load PDB/A1_Cavity.pdb
select A1_Cavity
hide everything, A1_Cavity
show surface, A1_Cavity
cmd.color_deep("white", 'A1_Cavity', 0)
util.cba(33,"A1",_self=cmd)
