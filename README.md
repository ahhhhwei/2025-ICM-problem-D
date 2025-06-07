# 2025 ICM Problem D Introduction

![](./pic/our_work.png)

This paper focuses on the infrastructure issues in Baltimore's transportation network and proposes an integrated analytical framework combining multiple algorithms. Based on an **improved K-Shell algorithm** — which incorporates node net passenger flow weights and road travel time weights derived from the BPR function — we construct a node importance evaluation model. Using the **K-Prototypes clustering algorithm**, we optimize public transit route planning and recommend the addition of key commuter routes. By integrating the **LWR** model, we establish an exponential growth prediction mechanism for traffic congestion and develop dynamic management strategies. The study verifies the model's robustness and demonstrates its stability via sensitivity analysis on parameter α. This approach provides a spatially adaptable solution for urban transportation network optimization.

本文聚焦巴尔的摩交通网络的基础设施问题，提出融合多算法的综合分析框架：基于改进的K-Shell算法（引入节点净客流量权重与BPR函数推导的道路通行时间权重），构建节点重要性评估模型；通过K-Prototypes聚类算法优化公交线路规划，建议新增关键通勤线路；结合LWR模型建立交通拥堵指数增长预测机制，并制定动态管理策略。研究最终通过参数α的敏感性分析证明模型稳定性，为城市交通网络优化提供了空间适应性解决方案。

# Team Members / 团队成员

![](./pic/2500387.jpg)

This paper was completed by three members from Zhejiang University of Technology:  **Wangzi Chen** , **Jiawei Wen** , and **Lisha Zhang** , and it won the Meritorious Winner in ICM 2025 . Among them, Lisha Zhang was elected as the team leader (#2500387) due to her need for award recognition, and she was responsible for most of the coding. Jiawei Wen handled the modeling and initial draft of the paper, while Wangzi Chen was in charge of visualization, translation, LaTeX layout, and final review. **All three contributed equally to the project.**

本文由浙江工业大学的**陈王子**, **温家伟**和**张莉莎**三位成员共同完成，并荣获 ICM2025 的 Meritorious Winner（国际一等奖）。其中张莉莎被选举为 #2500387 队长，她负责了大部分代码；温家伟负责了建模和论文底稿；陈王子则负责作图、翻译、排版设计和最后的审阅；**三者贡献均等。**

# Files / 项目文件

```
├---baltimore
│   ├---cn
│   │   ├──basic.md
│   │   ├──essay.aux
│   │   ├──essay.bbl
│   │   ├──essay.log
│   │   ├──essay.out
│   │   ├──essay.pdf
│   │   ├──essay.synctex.gz
│   │   ├──essay.tex
│   │   ├---figures
│   │   │   ├──3stage.pdf
│   │   │   ├──busroute.pdf
│   │   │   ├──cluster.png
│   │   │   ├──data.pdf
│   │   │   ├──heatmap.png
│   │   │   ├──heatmapbefore.png
│   │   │   ├──intro.pdf
│   │   │   ├──letter.pdf
│   │   │   ├──topo1.pdf
│   │   │   ├──topo2.pdf
│   │   │   ├──topo3.pdf
│   │   │   ├──vis.png
│   │   │   └──zongshu.pdf
│   │   ├──letter.docx
│   │   └──ref.bib
│   ├---eng
│   │   ├──2500387.pdf
│   │   ├---figures
│   │   │   ├──3stage.pdf
│   │   │   ├──busroute.pdf
│   │   │   ├──cluster.png
│   │   │   ├──data.pdf
│   │   │   ├──heatmap.png
│   │   │   ├──heatmapbefore.png
│   │   │   ├──intro.pdf
│   │   │   ├──letter.pdf
│   │   │   ├──ourwork.pdf
│   │   │   ├──topo1.pdf
│   │   │   ├──topo2.pdf
│   │   │   ├──topo3.pdf
│   │   │   ├──vis.png
│   │   │   └──zongshu.pdf
│   │   ├──mcmthesis.aux
│   │   ├──mcmthesis.bbl
│   │   ├──mcmthesis.log
│   │   ├──mcmthesis.out
│   │   ├──mcmthesis.synctex.gz
│   │   ├──mcmthesis.tex
│   │   ├──mcmthesis.toc
│   │   └──ref.bib
│   ├---pic
│       ├──baltimore_traffic_heatmap.html
│       ├──bridge.py
│       ├──busroute.pdf
│       ├---cache
│       │   ├──570feaa922c478edae030a17449d2eb5221dc9c8.json
│       │   └──e6011c96a3475ac559038ac908b2c16a4aad5a1f.json
│       ├──data.pdf
│       ├──data.pptx
│       ├──heatmap.PNG
│       ├──intro.pdf
│       ├──intro.pptx
│       ├──letter.docx
│       ├──letter.pdf
│       ├──MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv
│       ├──ourwork.pdf
│       ├──topo.pdf
│       ├──topo.pptx
│       ├──zongshu.pdf
│       └──zongshu.pptx
├---code
│   ├──baltimore_traffic_heatmap.html
│   ├──baltimore_traffic_heatmap_large.html
│   ├──baltimore_traffic_heatmap_large_1.html
│   ├──baltimore_traffic_heatmap_small.html
│   ├──baltimore_traffic_heatmap_small_1.html
│   ├──bridge.py
│   ├──bridge_两次随机.py
│   ├──bus_stops_all.html
│   ├──bus_stops_all_another.html
│   ├──clustered_all.html
│   ├──clustered_all映射.py
│   ├──draw_bus_stops.py
│   ├──draw_filtered_stops.py
│   ├──draw_key_nodes.py
│   ├──draw1.py
│   ├──draw2.py
│   ├──draw3.py
│   ├──draw4.py
│   ├──filtered_stops.html
│   ├──filtered_stops_bigger.html
│   ├──key_nodes.html
│   ├──K-shell_for_all.py
│   ├──K-shell识别关键点.py
│   ├──nodes_all.html
│   ├──nodes_all映射.py
│   ├──test_01.html
│   ├──test_02.html
│   ├──test_03.html
│   ├──test_04.html
│   ├──test_05.html
│   ├──test_06.html
│   ├──不显示底图.py
│   ├──处理AADT.py
│   ├──处理busAADT.py
│   ├──处理edges.py
│   ├──处理lanes.py
│   ├──处理路线个数.py
│   ├──改进聚类(K-PandPCA)stops.py
│   ├──合并nodes-aadt.py
│   ├──计算0.25数.py
│   ├──计算MSE.py
│   ├──聚类STOPS(含XY).py
│   ├──聚类stops.py
│   ├──筛出1k点.py
│   ├──筛选AADT.py
│   ├──筛选edges.py
│   ├──筛选node.py
│   ├──筛选聚类stop.py
│   ├──特征权重计算.py
│   └──填充2655.py
├---pic
│   ├──2500387.jpg
│   ├──data_from.png
│   ├──data_look.png
│   ├──KP.png
│   ├──our_work.png
│   ├──quick_fill-1.png
│   ├──quick_fill-2.png
│   ├──quick_fill-3.png
│   ├──result.png
│   ├──文献方法对比与改进思路图.png
│   └──问题背景.png
├──README.md
└──正文-zh.md
```

# Blog / 相关博客

[2025数模美赛 - 阿伟的博客网站](https://ahhhhwei.github.io/2025/05/04/2025数模美赛/)
