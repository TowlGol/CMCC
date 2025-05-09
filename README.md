[//]: # (<h1 align="center"><strong><em>EXPANDING BALLOONS</em></strong></h1>)

<div align="center">
  <img src="./image/head.png" alt="计算时间与网格划分之间的关系" style="width:100%;">
</div>

<div align="center">
  <img src="./image/main.png" alt="计算时间与网格划分之间的关系" style="width:100%;">


</div>

# Instructions

EXPANDING BALLOONS is a Python-based tool for calculating the cavity morphology of a supramolecular cage. It can accurately support the calculation of many types of cavities. EXPANDING BALLOONS are available in two versions, the Python Project Version and the Pymol Plugin Version. In addition, a visual UI interface is provided in the Pymol Plugin to facilitate user use.

## Quick installation:

### Video:
[![观看视频](https://img.youtube.com/vi/mEkdtQ0SalM/maxresdefault.jpg)](https://youtu.be/mEkdtQ0SalM)

### Tutorial:
Installation of the tool is very simple and requires only a few steps:

<b>

1. Ensure the system has a python environment.
2. install the modle in Python environment:
  ```python
  # If you have these environments installed, skip this step.
  pip install numpy
  pip install scipy
  pip install pymeshlab
  pip install Bio
  
  ```
3. Put the supramolecular cage file in the "example" folder and modify the "filename" property in the Main_Process.py file.
4. Run Main_Process.py.

</b>

All the results will be placed in the "example" folder. The PDB folder will store the PDB file of the cavity calculation result. The OBJ folder holds the cavity data information of the vertex type.


#### Install plugin in PyMOL


There are only two step need to be finished:
<b>

1. Find the local plugin installation path of PyMOL. 
2. Copy all plugin files to startup path.
3. Start Pymol. 
4. Enter the command "start_balloon_gui"

</b>

Typically, you can find plugin installation path in "C:\Users\pc\AppData\Roaming\pymol\startup". If "import Expanding_Balloon success" is displayed in the pymol window, the plug-in is successfully installed.
#### Possible Problems
<b>

1. No module named 'scipy'.
2. No module named 'pymeshlab'.
3. No module named 'Bio'.
4. Failed to install the model automatically.
5. Folder not found.

</b>

#### Solution

<b>

- pip install 'scipy' and rerun.
- pip install 'pymeshlab' and rerun.
- pip install 'Bio' and rerun.
- Find the python environment path used by PyMOL, such as C:\PyMOL\Scripts, and install the missing python library in this path.
- Find the local installation path of PyMOL(Example: C:\PyMOL\Lib\site-packages\pmg_tk\startup). Copy all plugin files to your startup path.

</b>

## Data Collection and Processing
 [![观看视频](https://img.youtube.com/vi/lDFa2aPsj_M/maxresdefault.jpg)](https://youtu.be/lDFa2aPsj_M)


## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

You are **free to use, modify, and distribute** this software **for non-commercial purposes only**.  
For any **commercial use**, please contact the author for permission.

📜 [View License](https://creativecommons.org/licenses/by-nc/4.0/)

<hr>



<!-- # Supporting Information

The document serves as supporting material for "EXPANDING BALLOONS — A Robust Computational Method for Determining Supramolecular Cage Cavity Morphology Based on the 'Inflating Balloon' Metaphor." It provides further explanations of four parts of the paper: comparison of working parameters [(S1)](#s1-compare-working-parameter), center selection experiment [(S2)](#s2-center-selection-experiment-reult), SCB vertex result conversion [(S3)](#s3-SCB-Result-Convert), and experimental parameters and results of the baseline dataset [(S4)](#s4-experimental-results). If you want to know the detil about how to install and use SCB, you can visit GitHub for details and code.

## S1: Compare Working Parameter
<div align="center">

### Table S1 : KVFinder project detecte properties. 

| Supramolecular Cage Identifier | Step (Å) | Probe Out (Å) | Removal Distance (Å) | Volume Cutoff (Å³) |
|:------------------------------:|:-------:|:------------:|:--------------------:|:------------------:|
|              A1                |  0.25   |      10      |         0.75         |         80         |
|              B1                |  0.25   |      10      |         2.00         |          5         |
|              B2                |  0.25   |      10      |         1.75         |          5         |
|              B3                |  0.25   |      10      |         1.50         |         20         |
|              B4                |  0.25   |      10      |         1.50         |          5         |
|              B5                |  0.25   |      10      |         1.50         |          5         |
|              B6                |  0.25   |      10      |         1.50         |          5         |
|              B7                |  0.25   |      10      |         1.50         |         110        |
|              B8                |  0.25   |      10      |         1.50         |         25         |
|              B9                |  0.25   |      10      |         1.50         |          5         |
|              B10               |  0.25   |      10      |         1.50         |          5         |
|              B11               |  0.25   |      10      |         1.50         |          5         |
|              B12               |  0.25   |       6      |         1.50         |          5         |
|              B13               |  0.25   |       6      |         1.50         |          5         |
|              C1                |  0.25   |      10      |         1.00         |          5         |
|              F1                |  0.25   |      10      |         1.25         |          5         |
|              F2                |  0.60   |      20      |         3.50         |          5         |
|              H1                |  0.25   |      10      |         2.00         |          5         |
|              N1                |  0.25   |      10      |         1.50         |          5         |
|              O1                |  0.25   |      10      |         1.25         |         80         |
|              O2                |  0.25   |      20      |         1.25         |          5         |
|              W1                |  0.25   |      10      |         1.75         |         20         |



### Table S2 : Fpocket detection parameters for each supramolecular cage. 
| Supramolecular Cage Identifier | Minimum Radius of an Alpha Sphere (Å) | Maximum Radius of an Alpha Sphere (Å) |
|:------------------------------:|:------------------------------------:|:------------------------------------:|
|              A1                |                 3.4                  |                 8.0                  |
|              B1                |                 3.4                  |                 8.0                  |
|              B2                |                 3.4                  |                 8.0                  |
|              B3                |                 3.4                  |                 8.0                  |
|              B4                |                 3.4                  |                 8.0                  |
|              B5                |                 3.0                  |                 6.2                  |
|              B6                |                 3.4                  |                 8.0                  |
|              B7                |                 3.4                  |                 8.0                  |
|              B8                |                 3.4                  |                 8.0                  |
|              B9                |                 3.4                  |                 8.0                  |
|             B10                |                 3.4                  |                 8.0                  |
|             B11                |                 3.4                  |                 8.0                  |
|             B12                |                 3.4                  |                 8.0                  |
|             B13                |                 3.4                  |                 8.0                  |
|              C1                |                 3.4                  |                 8.0                  |
|              F1                |                 2.0                  |                 6.2                  |
|              F2                |                 3.4                  |                40.0                  |
|              H1                |                 3.4                  |                 6.2                  |
|              N1                |                 3.7                  |                 8.0                  |
|              O1                |                 3.4                  |                 6.2                  |
|              O2                |                 3.4                  |                 6.2                  |
|              W1                |                 4.0                  |                 7.0                  |



### Table S3 : Cavity volumes calculated with C3 using a grid spacing of 0.5 Å and a distance threshold for the 90-degree calculation of 2 times the window size. For the Dataset 2, all run properties are default.
| Supramolecular Cage Identifier | C3 Calculated Volume (Å³) | Guest vdW Volume (Å³) | Estimated Cavity Volume Using Rebek’s Rule (Å³) | Relative Error (%) |
|:------------------------------:|:-------------------------:|:---------------------:|:--------------------------------------------:|:------------------:|
|              B1                |            298            |          150          |                     273                      |        9.2         |
|              B2                |            292            |          155          |                     281                      |        3.8         |
|              B3                |            267            |          137          |                     248                      |        7.7         |
|              B4                |            422            |          309          |                     562                      |       -24.9        |
|              B5                |             63            |           50          |                      90                      |       -29.8        |
|              B6                |             64            |           53          |                      96                      |       -33.4        |
|              B7                |            749            |          519          |                     944                      |       -20.6        |
|              B8                |            726            |          512          |                     930                      |       -21.9        |
|              B9                |             85            |          141          |                     257                      |       -66.9        |
|             B10                |            263            |          151          |                     274                      |        -4.1        |
|             B11                |            448            |          307          |                     558                      |       -19.8        |
|             B12                |            708            |          524          |                     954                      |       -25.8        |
|             B13                |            828            |          618          |                    1123                      |       -26.2        |
|                                |                           |                       |               **MRAE (%)**                   |        22.6        |

</div>


## S2:Center Selection Experiment Reult

The following tables demonstrate the impact of the choice of sphere center on the results. The first row for each data presents the estimated cavity volume results, the cavity volume results calculated based on different sphere center, and division time parameter. The second row is the number of extension time(ET) for each result calculation. The third row is the relative error(RE) for each result calculation. As described in the paper, because many of the molecular cage data are affected by other forces such as hydrogen bonding, the actual cavity volume is smaller than the Rebek's rule based estimate. Therefore, we introduced the publication volume of the supramolecular cage to revise our results during the evaluation. The final result is the average of the two calculated results.

<div align="center">

### Table S4 : Sphere Center Influence

| Supramolecular Cage | Estimated\Reference Cavity Volume (Å³) | Center(Å³) | Centroid(Å³) | Symmetrical Point(Å³) | Division Time |
|:------------------------------:|:-------------------:|:------:|:--------:|:-----------------:|:-----:|
|              B1                |         273         | 312    | 303      |  314              |   4   |
|                                |         ET =         |  31  | 31   |   31   |       |
|                                |         RE =         | 14.2 |10.9  |15.0    |       |
|              B2                |       281/285       | 318  | 314  |  318   |   4   |
|                                |        ET =          |  33  | 33   | 33     |       |
|                              |          RE =        | 13.1/11.5 |11.7/10.1  |13.1/11.5    |       |
|              B3                |       248/270       | 293  | 296  |  296   |   4   |
|                                |        ET =         |  32  | 30   |   32   |       |
|                                |        RE =          |  18.1/8.5|19.3/9.6  |  19.3/9.6  |       |
|              B4                |       562/434       | 464  | 455  |  482   |   4   |
|                                |        ET =        |         21          | 18   | 22   |        |       |
|                                |        RE =          |     -17.4/6.9     |-19.0/4.8|-14.2/11.0|    |       |
|              B5                |        90/52        | 77   | 78   |   79   |   4   |
|                                |        ET =        |         20          | 20   | 18   |        |       |
|                                |       RE =          |     -14.4/48.0     |-13.3/51.9|-12.2/51.9|    |       |
|              B6                |        96/55        | 74   | 74   |   74   |   4   |
|                                |        ET =         |         16          | 16   | 16   |        |       |
|                                |        RE =         |     -22.9/34.5     |-22.9/34.5|-22.9/34.5|    |       |
|              B7                |       944/810       | 860  | 826  |  893   |   4   |
|                                |        ET =         |         32          | 25   | 32   |        |       |
|                                |       RE =         |      -8.8/6.1    | -12.5/1.9 |-5.4/10.2|    |       |
|              B8                |         930         | 825  | 822  |  861   |   4   |
|                                |        ET =         |         21          | 27   | 28   |        |       |
|                                |        RE =         |    -11.2    |-11.6|-7.4|    |       |
|              B9                |       257/184       | 225  | 226  |  225   |   4   |
|                                |        ET =         |         20          | 20   | 18   |        |       |
|                                |        RE =         |     -12.4/22.2     |-12.0/22.8|-12.4/22.2|    |       |
|             B10                |       274/261       | 291  | 288  |  291   |   4   |
|                                |        ET =        |         34          | 34   | 35   |        |       |
|                                |        RE =         |      6.2/11.4    |5.1/10.3|6.2/11.4|    |       |
|             B11                |         558         | 516  | 517  |  514   |   4   |
|                                |        ET =         |         23          | 23   | 24   |        |       |
|                                |       RE =          |      -7.5    |-7.3|-7.8|    |       |
|             B12                |        954/718      | 720  | 720  |  721   |   5   |
|                                |         ET =         |         29          | 29   | 31   |        |       |
|                                |        RE =         |     -24.5/0.2     |-24.5/0.2|-24.4/0.4|    |       |
|             B13                |      1123/925       | 845  | 846  |  850   |   5   |
|                                |       ET =          |         39          | 39   | 38   |        |       |
|                                |       RE =          |     -24.7/-8.6     |-24.6/-8.5|-24.3/-8.1|    |       |
|           **MEAE (%)**         |                     |15.0/14.7|15.0/14.2|14.2/15.5|   -   |
|             **Times**          |                     |    27    |26.5|27.5|       |

</div>

## S3: SCB Result Convert
Current mainstream biomolecular results are typically saved and presented in formats such as pdb and mol2. However, the results from SCB are displayed in the form of vertex meshes. This format is not conducive for experts to further analyze supramolecular cages using SCB. To address this, we have developed a method to convert vertex data into pdb data for better presentation of our results. In this method, each vertex is replaced by a carbon atom. Compared to the vertex, a carbon atom has a van der Waals radius (1.7 Å). Therefore, we need to perform a reverse translation of 1.7 Å in the direction of atomic expansion. Figure 1 illustrates the corresponding conversion process. The black outline represents the outer contour of the surface before vertex conversion. The red and yellow outlines represent the inner and outer surface contours after conversion. Figure 1C shows the result after the vertices have been translated.

<div align="center">
  <img src="./image/4.png" alt="计算时间与网格划分之间的关系" style="width:100%;">
  <p><em>Figure 1 : SCB Result Convert Process.</em></p>
</div>


## S4: Experimental Results

<div align="center">

### Table S5 : Calculation Result of Dataset 1  

<div align="center">

| **Cage**                      | **Estimated Volume (Å³)** | **SCB Result (Å³)** | **Division Time** | **Result**                           |
|:----------------------------------:|:-------------------------:|:--------------:|:-----------------:|:-----------------------------------:|
| **B1**                        | 273                       | 303            | 4                 | <img src="./image/B1.png" width="100" height="100"/>   |
| **B2**                        | 281                       | 314            | 4                 | <img src="./image/B2.png" width="100" height="100"/>   |
| **B3**                        | 248                       | 296            | 4                 | <img src="./image/B3.png" width="100" height="100"/>   |
| **B4**                        | 562                       | 455            | 5                 | <img src="./image/B4.png" width="100" height="100"/>   |
| **B5**                        | 90                        | 78             | 4                 | <img src="./image/B5.png" width="100" height="100"/>   |
| **B6**                        | 96                        | 74             | 4                 | <img src="./image/B6.png" width="100" height="100"/>   |
| **B7**                        | 944                       | 890            | 5                 | <img src="./image/B7.png" width="100" height="100"/>   |
| **B8**                        | 930                       | 861            | 5                 | <img src="./image/B8.png" width="100" height="100"/>   |
| **B9**                        | 257                       | 226            | 4                 | <img src="./image/B9.png" width="100" height="100"/>   |
| **B10**                       | 274                       | 288            | 4                 | <img src="./image/B10.png" width="100" height="100"/>  |
| **B11**                       | 558                       | 517            | 5                 | <img src="./image/B11.png" width="100" height="100"/>  |
| **B12**                       | 954                       | 720            | 5                 | <img src="./image/B12.png" width="100" height="100"/>  |
| **B13**                       | 1123                      | 846            | 5                 | <img src="./image/B13.png" width="100" height="100"/>  |

</div>


### Table S6 : Calculation Result of Dataset 2

| **Cage** | **Reference/Average Volume (Å³)** | **SCB Result (Å³)** | **Division Time** | **Result** |
|:--------:|:----------------------------------:|:--------------:|:-----------------:|:----------:|
| **A1**   | 1375                               | 1455           | 5                 | <img src="./image/A1.png" width="100" height="100"/> |
| **C1**   | 549                                | 592            | 5                 | <img src="./image/C1.png" width="100" height="100"/> |
| **F1**   | 500                                | 480            | 5                 | <img src="./image/F1.png" width="100" height="100"/> |
| **F2**   | 42572                               | 32350          | 5                 | <img src="./image/F2.png" width="100" height="100"/> |
| **H1**   | 259                                | 167            | 4                 | <img src="./image/H1.png" width="100" height="100"/> |
| **N1**   | 434                                | 407            | 4                 | <img src="./image/N1.png" width="100" height="100"/> |
| **O1**   | 142                                | 95             | 4                 | <img src="./image/O1.png" width="100" height="100"/> |
| **O2**   | 400                                | 433            | 4                 | <img src="./image/O2.png" width="100" height="100"/> |
| **W1**   | 20                                 | 27             | 4                 | <img src="./image/W1.png" width="100" height="100"/> |

</div>


The selection of parameters in the experiment is primarily based on two principles: data analysis results of division times and comparison of visualization results.   First, we examine the impact of division times on the calculation results for dataset 1 from the paper.   The SCB method's first step is the grid's surface division.   This step is similar to grid partitioning in grid-based methods, where the number of divisions affects the precision and computation time of the final results.   Figure 2 shows the relationship between Division Time (DT) and SCB computation time.  Due to the subdivision surface algorithm causing an exponential increase in the number of vertices, the corresponding computation time also increases with the times of subdivision surface.  It is evident that after six grid divisions, the computation time reaches an unacceptable magnitude (55 seconds).   Therefore, the division parameters should only be between 3, 4, and 5.   In Figure 2, the blue, green, and yellow lines represent the calculation results for subdivision times of 3, 4, and 5, respectively.


<p align="center">
  <img src="./image/1.png" alt="计算时间与网格划分之间的关系" style="width:50%;">
  <br><em>图2:计算时间与网格划分之间的关系。</em>
</p>


By observing the graphs, it can be concluded that SCB yields better results for larger supramolecular cages (Cavity Volume > 500) when DT = 5. However, for other supramolecular cage cavity calculations, the impact of DT on the results is not significant, as shown in Figure 3A. Hence, we introduced the Origin Publication cavity volume as a comparison parameter based on Rebek's rule (Figure 3B). DT = 3 has higher calculation accuracy for smaller supramolecular cages. DT = 4 shows more stable and higher accuracy across both calculation references. To further explore the choice of calculation parameters, we visualized the data with smaller cavity volumes (B5, B6).


By comparing the visualization results, the shape of the calculated results did not change, the size did.    We believe the change in size is due to finer probes exploring small spaces between atoms—spaces that cavity guest molecules cannot physically reach.    moreover, by combining the charts, It is evident that these small spaces are not considered part of the supramolecular cage's cavity (fewer vertices result in higher accuracy).    Therefore, we conclude that results for DT = 3 or 4 are acceptable compared to DT = 5.    Considering the comparison with mean absolute error(Figure 3 dotted line) in Figure 2, we ultimately recommend using DT = 4 as the parameter when the volume of the supramolecular cage is less than 500.
<p align="center">
  <img src="./image/2.png" alt="分裂次数对最终效果的影响。" style="width:100%;">
  <br><em>图3:分裂次数对最终效果的影响。</em>
</p>

<p align="center">
  <img src="./image/3.png" alt="B5、B6的空腔计算可视化结果。" style="width:50%;">
  <br><em>图4:B5、B6的空腔计算可视化结果。</em>
</p>



 -->
