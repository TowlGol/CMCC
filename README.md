# Instructions
### Install Python environment
### Install PyMOL
### Use plugin to calculate cavity volume and output pml file
#### Possible problems
1. No module named 'scipy'
2. No module named 'pymeshlab'
3. No module named 'Bio'
- Solution: Install missing Python library
- pip install 'scipy' and rerun
- pip install 'pymeshlab' and rerun
- pip install 'Bio' and rerun

### Install plugin in PyMOL
1. Find the local installation path of PyMOL2
2. Example: C:\PyMOL2\Lib\site-packages\pmg_tk\startup
3. Copy all plugin files to your startup path

### Possible problems after installing plugin in PyMOL
1. No module named 'scipy'
2. No module named 'pymeshlab'
3. No module named 'Bio'
- Solution: Find the python environment path used by PyMOL, such as C:\PyMOL2\Scripts, and install the missing python library in this path
- pip install 'scipy' and rerun
- pip install 'pymeshlab' and rerun
- pip install 'Bio' and rerun

# Use Method


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Supporting Information

The document serves as supporting material for "EXPANDING BALLOONS — A Robust Computational Method for Determining Supramolecular Cage Cavity Morphology Based on the 'Inflating Balloon' Metaphor." It provides further explanations of four parts of the paper: comparison of working parameters (S1), center selection experiment (S2), SCB vertex result conversion (S3), and experimental parameters and results of the baseline dataset (S4). If you want to know the detil about how to install and use SCB, you can visit GitHub for details and code.

## S1： Compare Working Parameter
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



### Table S3 : Cavity volumes calculated with C3 using a grid spacing of 0.5 Å and a distance threshold for the 90-degree calculation of 2 times the window size.For the Dataset 2, all run properties are default.
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


## S2：Center Selection Experiment Reult

The following tables demonstrate the impact of the choice of sphere center on the results.The first row for each data presents the estimated cavity volume results, the cavity volume results calculated based on different sphere center, and division time parameter.The second row is the number of extension time(ET) for each result calculation.The third row is the relative error(RE) for each result calculation. As described in the paper, because many of the molecular cage data are affected by other forces such as hydrogen bonding, the actual cavity volume is smaller than the Rebek's rule based estimate. Therefore, we introduced the publication volume of the supramolecular cage to revise our results during the evaluation. The final result is the average of the two calculated results.

<!-- 下列图表展示了球心选择对于结果的影响。对于每个数据的第一行是估算结果或出版物结果不同点计算的空腔体积结果与分裂参数选择。第二行中的数据是每个结果计算所需要的分裂次数。第三行是计算结果与估算结果或出版物结果的误差值。正如论文中所描述的，由于许多分子笼数据受到氢键等其他作用力影响，实际空腔体积要小于基于Rebek's rule所估计的空腔体积。因此，在评估时我们引入超分子笼的出版物体积来修正我们的结果。最终的结果取两者的平均值。 -->
  
<div align="center">

### Table S4 : Sphere Center Influence

| Supramolecular Cage Identifier | Estimated\Reference Cavity Volume (Å³) | Center | Centroid | Symmetrical Point | Division Time |
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

<!-- 当前主流的生物分子结果通常都以pdb、mol2等形式进行保存与展示。然而，SCB的结果都以顶点网格的形式进行展现。并且展示效果通常只有空腔计算结果。我们认为这不利于专家使用SCB对超分子笼进行进一步分析。为此，我们实现了一种将顶点数据转化为pdb数据的方法来更好的展示我们的结果。每一个顶点被一个碳原子代替。相比于顶点，碳原子存在范德华半径(1.7Å)。因此我们需要向原子扩展方向的反向平移1.7Å的距离。图1展示了相应的转化过程。黑色的边框是顶点未转化前的表面外轮廓。红色和黄色边框分别是是转化后但未平移的内外表面轮廓。图1C展示是顶点平移后的结果。 -->
Current mainstream biomolecular results are typically saved and presented in formats such as pdb and mol2. However, the results from SCB are displayed in the form of vertex meshes. This format is not conducive for experts to further analyze supramolecular cages using SCB. To address this, we have developed a method to convert vertex data into pdb data for better presentation of our results. In this method, each vertex is replaced by a carbon atom. Compared to the vertex, a carbon atom has a van der Waals radius (1.7 Å). Therefore, we need to perform a reverse translation of 1.7 Å in the direction of atomic expansion. Figure 1 illustrates the corresponding conversion process. The black outline represents the outer contour of the surface before vertex conversion. The red and yellow outlines represent the inner and outer surface contours after conversion. Figure 1C shows the result after the vertices have been translated.

<div style="text-align: center;">
  <img src="./image/4.png" alt="计算时间与网格划分之间的关系" style="width:100%;">
  <p><em>Figure 1 : SCB Result Convert Process.</em></p>
</div>


## S4: Experimental Results

<div align="center">

### Table S5 : Calculation Result of Dataset 1  

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="text-align: center; width: 10%;">Cage</th>
      <th style="text-align: center; width: 6.9%;">B1</th>
      <th style="text-align: center; width: 6.9%;">B2</th>
      <th style="text-align: center; width: 6.9%;">B3</th>
      <th style="text-align: center; width: 6.9%;">B4</th>
      <th style="text-align: center; width: 6.9%;">B5</th>
      <th style="text-align: center; width: 6.9%;">B6</th>
      <th style="text-align: center; width: 6.9%;">B7</th>
      <th style="text-align: center; width: 6.9%;">B8</th>
      <th style="text-align: center; width: 6.9%;">B9</th>
      <th style="text-align: center; width: 6.9%;">B10</th>
      <th style="text-align: center; width: 6.9%;">B11</th>
      <th style="text-align: center; width: 6.9%;">B12</th>
      <th style="text-align: center; width: 6.9%;">B13</th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td style="width: 10%;">Estimated cavity Volume (Å<sup>3</sup>)</td>
      <td style="width: 6.9%;">273</td>
      <td style="width: 6.9%;">281</td>
      <td style="width: 6.9%;">248</td>
      <td style="width: 6.9%;">562</td>
      <td style="width: 6.9%;">90</td>
      <td style="width: 6.9%;">96</td>
      <td style="width: 6.9%;">944</td>
      <td style="width: 6.9%;">930</td>
      <td style="width: 6.9%;">257</td>
      <td style="width: 6.9%;">274</td>
      <td style="width: 6.9%;">558</td>
      <td style="width: 6.9%;">954</td>
      <td style="width: 6.9%;">1123</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">SCB result</td>
      <td style="width: 6.9%;">303</td>
      <td style="width: 6.9%;">314</td>
      <td style="width: 6.9%;">296</td>
      <td style="width: 6.9%;">455</td>
      <td style="width: 6.9%;">78</td>
      <td style="width: 6.9%;">74</td>
      <td style="width: 6.9%;">890</td>
      <td style="width: 6.9%;">861</td>
      <td style="width: 6.9%;">226</td>
      <td style="width: 6.9%;">288</td>
      <td style="width: 6.9%;">517</td>
      <td style="width: 6.9%;">720</td>
      <td style="width: 6.9%;">846</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">Division Time</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">5</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">5</td>
      <td style="width: 6.9%;">5</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">4</td>
      <td style="width: 6.9%;">5</td>
      <td style="width: 6.9%;">5</td>
      <td style="width: 6.9%;">5</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">Result</td>
      <td style="width: 6.9%;"><img src="./image/B1.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B2.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B3.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B4.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B5.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B6.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B7.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B8.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B9.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B10.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B11.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B12.png" width="100" height="100"/></td>
      <td style="width: 6.9%;"><img src="./image/B13.png" width="100" height="100"/></td>
    </tr>
  </tbody>
</table>

### Table S6 : Calculation Result of Dataset 2

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="text-align: center; width: 10%;">Cage</th>
      <th style="text-align: center; width: 10%;">A1</th>
      <th style="text-align: center; width: 10%;">C1</th>
      <th style="text-align: center; width: 10%;">F1</th>
      <th style="text-align: center; width: 10%;">F2</th>
      <th style="text-align: center; width: 10%;">H1</th>
      <th style="text-align: center; width: 10%;">N1</th>
      <th style="text-align: center; width: 10%;">O1</th>
      <th style="text-align: center; width: 10%;">O2</th>
      <th style="text-align: center; width: 10%;">W1</th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td style="width: 10%;">Reference/Average Volume (Å<sup>3</sup>)</td>
      <td style="width: 10%;">1375</td>
      <td style="width: 10%;">549</td>
      <td style="width: 10%;">500</td>
      <td style="width: 10%;">4257</td>
      <td style="width: 10%;">259</td>
      <td style="width: 10%;">434</td>
      <td style="width: 10%;">142</td>
      <td style="width: 10%;">400</td>
      <td style="width: 10%;">20</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">SCB result</td>
      <td style="width: 10%;">1455</td>
      <td style="width: 10%;">592</td>
      <td style="width: 10%;">480</td>
      <td style="width: 10%;">32350</td>
      <td style="width: 10%;">167</td>
      <td style="width: 10%;">407</td>
      <td style="width: 10%;">95</td>
      <td style="width: 10%;">433</td>
      <td style="width: 10%;">27</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">Division Time</td>
      <td style="width: 10%;">5</td>
      <td style="width: 10%;">5</td>
      <td style="width: 10%;">5</td>
      <td style="width: 10%;">5</td>
      <td style="width: 10%;">4</td>
      <td style="width: 10%;">4</td>
      <td style="width: 10%;">4</td>
      <td style="width: 10%;">4</td>
      <td style="width: 10%;">4</td>
    </tr>
    <tr style="text-align: center;">
      <td style="width: 10%;">Result</td>
      <td style="width: 10%;"><img src="./image/A1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/C1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/F1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/F2.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/H1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/N1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/O1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/W1.png" width="100" height="100"/></td>
      <td style="width: 10%;"><img src="./image/O2.png" width="100" height="100"/></td>
    </tr>
  </tbody>
</table>

</div>

The selection of parameters in the experiment is primarily based on two principles: data analysis results of division times and comparison of visualization results.   First, we examine the impact of division times on the calculation results for dataset 1 from the paper.   The SCB method's first step is the grid's surface division.   This step is similar to grid partitioning in grid-based methods, where the number of divisions affects the precision and computation time of the final results.   Figure 2 shows the relationship between Division Time (DT) and SCB computation time.  Due to the subdivision surface algorithm causing an exponential increase in the number of vertices, the corresponding computation time also increases with the times of subdivision surface.  It is evident that after six grid divisions, the computation time reaches an unacceptable magnitude (55 seconds).   Therefore, the division parameters should only be between 3, 4, and 5.   In Figure 2, the blue, green, and yellow lines represent the calculation results for subdivision times of 3, 4, and 5, respectively.


<!-- 
实验中的参数选择主要基于两个原则：分裂次数的数据分析结果以及可视化结果对比。首先，我们分裂次数对于论文中数据集1计算结果的影响。SCB方法的第一步是对网格进行曲面划分。这一步骤与基于网格方法中的网格划分相似，划分次数会对最终结果的精确度与计算时间产生影响。图2展示了Division Time（DT）与SCB计算时间的关系。由于网格划分的网格数量是指数增长的，因此相对应的计算时间也随着划分次数进行增长。显而易见的是，在进行六次网格划分后，计算的时间已经达到了不可接受的时间量级（55 second）。因此，分裂参数应只介于3，4，5之间。 图2蓝色、绿色、黄色分别是分裂次数为3，4，5的计算结果。通过观察图标可以得出，DT)= 5时，SCB在较大的超分子笼（Cavity Volume  > 500）计算中有着较好的结果。而在其余的超分子笼空腔计算中，图3A中DT对结果的影响表现的并不明显。因此，我们在使用Rebek's rule的对比基础上引入了Origin Publication cavity volume作为对比参数（Figure 3B）。我们可以清晰的看到，DT = 3 在超分子笼较小时，计算精度较高。DT = 4在两个计算参考中的准确性更稳定且更高。为了进一步探究计算参数的选择，我们将数据中空腔体积较小的数据（B5,B6）进行了可视化。通过对比可视化结果可以发现，计算结果的形状没有发生变化，大小发生了变化。我们认为，大小发生变化的原因是更精细的探针探索到了原子之间的细小空间——空腔客体分子受物理限制所无法到达的空间。然而，结合图表我们可以知道，这些细小空间并不被认为是超分子笼的空腔（更少的顶点却有更高的准确率）。因此，我们认为相较于DT = 5 ,DT = 3或4的结果都可以接受。结合图2中对于MAME的对比，我们最终推荐在超分子笼体积小于500时使用DT=4作为参数。 -->

<div style="text-align: center;">
  <img src="./image/1.png" alt="计算时间与网格划分之间的关系" style="width:50%;">
  <p><em>图2：计算时间与网格划分之间的关系</em></p>
</div>

By observing the graphs, it can be concluded that SCB yields better results for larger supramolecular cages (Cavity Volume > 500) when DT = 5. However, for other supramolecular cage cavity calculations, the impact of DT on the results is not significant, as shown in Figure 3A. Hence, we introduced the Origin Publication cavity volume as a comparison parameter based on Rebek's rule (Figure 3B). DT = 3 has higher calculation accuracy for smaller supramolecular cages. DT = 4 shows more stable and higher accuracy across both calculation references. To further explore the choice of calculation parameters, we visualized the data with smaller cavity volumes (B5, B6).


By comparing the visualization results, the shape of the calculated results did not change, the size did.    We believe the change in size is due to finer probes exploring small spaces between atoms—spaces that cavity guest molecules cannot physically reach.    moreover, by combining the charts, It is evident that these small spaces are not considered part of the supramolecular cage's cavity (fewer vertices result in higher accuracy).    Therefore, we conclude that results for DT = 3 or 4 are acceptable compared to DT = 5.    Considering the comparison with mean absolute error(Figure 3 dotted line) in Figure 2, we ultimately recommend using DT = 4 as the parameter when the volume of the supramolecular cage is less than 500.
<div style="text-align: center;">
  <img src="./image/2.png" alt="计算时间与网格划分之间的关系" style="width:100%;">
  <p><em>图3：分裂次数对最终效果的影响。</em></p>
</div>

<div style="text-align: center;">
  <img src="./image/3.png" alt="计算时间与网格划分之间的关系" style="width:50%;">
  <p><em>图4：B5、B6的空腔计算可视化结果。</em></p>
</div>

