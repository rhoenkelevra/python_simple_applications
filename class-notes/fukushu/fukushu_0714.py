# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:39:10 2021

@author: user15
"""

# =============================================================================
# input enter data "q" for quit
# ask until q
# output data count
# output singular data count
# count empty and not empty
# =============================================================================
ans_list = []
empty_item = 0
have_item = 0
while True:
    ans = input("データを入力してください。　（’ｑ’を入力すると終了。  \n -->")
    
    if ans == "q":
        break
    # 空を無視する場合
    # if ans:    
    #   ans_list.append(ans)
    
# =============================================================================
#     teacher answer
#     dset.add(ans)
#     count += 1
#     print(len(dset))
# =============================================================================
    
    # 空をカウントする場合
    ans_list.append(ans)
    empty_item = ans_list.count("")
    have_item = len(ans_list) - empty_item
    
# =============================================================================
#  Using list comprehension          
#  non_empty_list = [item for item in ans_list if item]
#  non_empty_list = [item for item in ans_list if "" in item]
#  empty_list = [item for item in ans_list if not item]
# =============================================================================
    
    ans_count = len(ans_list)
    # or use counter variable
    
    ans_set = set(ans_list)
    ans_set_count = len(ans_set)
   

print(f"入力回数は： {ans_count}回でした。\n", ans_list)
print(f"重複を除去したデータは：　{ans_set_count}個でした。\n", ans_set)
print(empty_item, have_item)
# print(non_empty_list)
# print(empty_list)
