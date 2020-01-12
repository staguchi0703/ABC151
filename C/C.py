# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
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
N, M = [int(item) for item in input().split()]
ans_list = [input().split() for _ in range(M)]
# print(ans_list)

res_ac = 0
ans_stack = []
wa_stack = []

for q, ans in ans_list:
    # print(q, ans)
    if ans == 'AC':
        if q not in ans_stack:
            res_ac += 1
        ans_stack.append(q)
    else:
        if q not in ans_stack:
            wa_stack.append(q)

res_list = []
for i in wa_stack:
    if i in ans_stack:
        res_list.append(i)


print(res_ac, len(res_list))

            