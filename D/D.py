# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
from collections import deque
H, W = [int(item) for item in input().split()]
grid = [input().split() for _ in range(H)]


def cal_dis(start_point):
    # dfsもしくはbfsするキュー(スタック)を生成
    d = deque()
    d.append(start_point)
    #訪れた履歴を管理するスタックを生成
    f = deque()


    #とある座標の値を表示する関数（座標が定義外に飛んだ時にエラーとならないようにtry-exceptで無視できるようにするのがコツ）
    def temp_sign(temp_site):
        try:
            res = map_grid[temp_site[0]][temp_site[1]]
            return res
        except:
            pass

    next_direction_list = [[1, 0], [0,1], [-1, 0], [0, -1]]
    is_found = False

    while len(d) > 0:
        temp_site = d.pop()

        for next_dir in next_direction_list:

            new_site = [x+y for (x, y) in zip(temp_site, next_dir) if x+y >= 0]
            # print(new_site)

            if temp_sign(new_site) in ['.', 'g'] and new_site not in f:
                # print(new_site)
                d.append(new_site)
                f.append(new_site)
    return len(f)

res = []

for j, line in enumerate(grid):
    for i, point in enumerate(line):
        if point is not '#':
            res.append(cal_dis([i+1,j+1]))
print(res)