//步骤一 求多源最短路径,利用Floyd于O(n3)复杂度内算出各点间最短路径
void Floyd(int n) {
    for (int i = 0; i < n; i++) {
        dis[i][i] = 0;
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
            }
        }
    }
}
//步骤二 最短路径性质挖掘
基于步骤一，进一步考察最短路径上点、边、距离关系，为高效统计计算做铺垫。
最短路径子路性
       假设A点到B点最短距离为Dis[A][B]，B到C点最短距离为Dis[B][C]，A到C点最短距离为Dis[A][C]
       则B为A→C最短路径上一点 

       Dis[A][B]+Dis[B][C]=Dis[A][C]
设Cnt[A][B]数组表示A点到B点最短路径组成的网络所含邻接B点的边数
for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (e[k][j] != INF && dis[i][k] + e[k][j]  
                  == dis[i][j]) 
                {
                    cnt[i][j]++;
                }
            }
        }
    }
