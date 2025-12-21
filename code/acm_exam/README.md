# ACM算法笔记

## 目录

- [字符串](#字符串)
  - [01字符串计数](#01字符串计数)
  - [字符串加减1](#字符串加减1)
  - [删除公共字符](#删除公共字符)
  - [字符串表达式](#字符串表达式)
  - [数字位整除个数](#数字位整除个数)
  - [查找敏感词](#查找敏感词)
  - [字母和](#字母和)
  - [相同子串个数](#相同子串个数)
  - [字符串统计](#字符串统计)
  - [子串最小代价](#子串最小代价)
  - [大小写翻转](#大小写翻转)
- [数学](#数学)
  - [六边形面积](#六边形面积)
  - [成绩统计](#成绩统计)
  - [字符串转换](#字符串转换)
  - [骰子期望次数](#骰子期望次数)
  - [牛牛吃饭期望](#牛牛吃饭期望)
  - [k个子序列极差和最大](#k个子序列极差和最大)
  - [三角形判断](#三角形判断)
  - [发射火箭](#发射火箭)
  - [墙壁划线](#墙壁划线)
  - [最多质数和](#最多质数和)
  - [最小质因数](#最小质因数)
  - [被三整除子串](#被三整除子串)
  - [红黑数之和](#红黑数之和)
  - [计算工资](#计算工资)
  - [发短信](#发短信)
  - [数组相减相等](#数组相减相等)
  - [病毒](#病毒)
  - [最小权值和](#最小权值和)
- [位运算](#位运算)
  - [lowbit求和](#lowbit求和)
  - [最大异或数](#最大异或数)
  - [X与Y的对数](#X与Y的对数)
  - [减2的n次幂](#减2的n次幂)
  - [异或找缺失数](#异或找缺失数)
  - [好数的异或和](#好数的异或和)
- [栈](#栈)
  - [括号调整次数](#括号调整次数)
  - [括号期望](#括号期望)
  - [前缀串长度](#前缀串长度)
  - [括号有效性](#括号有效性)
  - [合法字符串](#合法字符串)
- [搜索](#搜索)
  - [分苹果](#分苹果)
  - [格子染色](#格子染色)
  - [打僵尸](#打僵尸)
  - [好格子](#好格子)
  - [字符串插入加号](#字符串插入加号)
  - [最小操作树](#最小操作树)
  - [多叉树](#多叉树)
  - [树子节点颜色个数](#树子节点颜色个数)
  - [随机加减](#随机加减)
- [排序](#排序)
  - [字典序最大序列](#字典序最大序列)
  - [游戏记录](#游戏记录)
  - [最少交换次数](#最少交换次数)
  - [数组删除](#数组删除)
  - [数组模排序](#数组模排序)
  - [分数排序](#分数排序)
  - [对称数组](#对称数组)
- [动态规划](#动态规划)
  - [迷宫寻宝](#迷宫寻宝)
  - [打地鼠](#打地鼠)
  - [包粽子](#包粽子)
- [贪心](#贪心)
  - [01字符串交换次数](#01字符串交换次数)
  - [加减1次数](#加减1次数)
  - [加减1相等](#加减1相等)
  - [加减1均值](#加减1均值)
  - [炸弹](#炸弹)
  - [买花](#买花)
  - [买商品](#买商品)
  - [买文具](#买文具)
  - [包车](#包车)
  - [蛇吃水果](#蛇吃水果)
  - [物品价值](#物品价值)
  - [最大非零子数组](#最大非零子数组)
  - [最大正方形边长](#最大正方形边长)
  - [游戏嘲笑子数组](#游戏嘲笑子数组)
  - [非递减数组](#非递减数组)
  - [完美集合](#完美集合)
  - [商品折扣](#商品折扣)
  - [去除小于平均值的次数](#去除小于平均值的次数)
  - [打枪](#打枪)
  - [字符串的权值](#字符串的权值)
  - [学生分组](#学生分组)
  - [打印次数](#打印次数)
  - [有效卡片](#有效卡片)
- [模拟](#模拟)
  - [数组加1](#数组加1)
  - [对答案](#对答案)
  - [密文解密](#密文解密)
  - [棋子移动](#棋子移动)
  - [密码锁拨动次数](#密码锁拨动次数)
  - [池化](#池化)
  - [打印里字](#打印里字)
  - [连续反转字符串](#连续反转字符串)
  - [贪吃蛇](#贪吃蛇)
  - [子数组除法](#子数组除法)
  - [01字符串截取](#01字符串截取)

---

## 题目统计

| 分类 | 题目数量 |
|------|----------|
| 字符串 | 11 |
| 数学 | 18 |
| 位运算 | 6 |
| 栈 | 5 |
| 搜索 | 9 |
| 排序 | 7 |
| 动态规划 | 3 |
| 贪心 | 23 |
| 模拟 | 11 |
| **总计** | **93** |

## 字符串

### [01字符串计数](problem/string/01_string_count.md)
- [Python 贪心](solution/string/01_string_count/01_string_count.py)

### [字符串加减1](problem/string/add_sub_string.md)
- [Python 枚举](solution/string/add_sub_string/add_sub_string_1.py)
- [Python 队列](solution/string/add_sub_string/add_sub_string_2.py)

### [删除公共字符](problem/string/delete_common_char.md)
- [Python 字符串](solution/string/delete_common_char/delete_common_char.py)

### [字符串表达式](problem/string/delete_string.md)
- [Python eval](solution/string/delete_string/delete_string_1.py)
- [Python 手动构造](solution/string/delete_string/delete_string_2.py)

### [数字位整除个数](problem/string/digit_division.md)
- [Python 数论](solution/string/digit_division/digit_division.py)

### [查找敏感词](problem/string/find_substring.md)
- [Python 字符串匹配](solution/string/find_substring/find_substring.py)

### [字母和](problem/string/letter_sum.md)
- [Python 集合去重](solution/string/letter_sum/letter_sum_1.py)
- [Python 构造列表](solution/string/letter_sum/letter_sum_2.py)

### [相同子串个数](problem/string/same_substring.md)
- [Python 列表](solution/string/same_substring/same_substring_1.py)
- [Python 字典](solution/string/same_substring/same_substring_2.py)

### [字符串统计](problem/string/string_count.md)
- [Python 暴力枚举](solution/string/string_count/string_count.py)

### [子串最小代价](problem/string/substring_cost.md)
- [Python 字符串匹配](solution/string/substring_cost/substring_cost.py)

### [大小写翻转](problem/string/toggle_case.md)
- [Python 数论](solution/string/toggle_case/toggle_case.py)

## 数学

### [六边形面积](problem/math/area_of_hexagon.md)
- [Python 几何](solution/math/area_of_hexagon/area_of_hexagon.py)

### [成绩统计](problem/math/calculate_grade.md)
- [Python 统计](solution/math/calculate_grade/calculate_grade.py)

### [字符串转换](problem/math/convert_string_by_index.md)
- [Python 内置函数计算](solution/math/convert_string_by_index/convert_string_by_index_1.py)
- [Python 手动计算](solution/math/convert_string_by_index/convert_string_by_index_2.py)

### [骰子期望次数](problem/math/dice_expectation.md)
- [Python 数学](solution/math/dice_expectation/dice_expectation.py)

### [牛牛吃饭期望](problem/math/eating_expectation.md)
- [Python 数学](solution/math/eating_expectation/eating_expectation.py)

### [k个子序列极差和最大](problem/math/extreme_sum.md)
- [Python 数论](solution/math/extreme_sum/extreme_sum.py)

### [三角形判断](problem/math/judge_triangle.md)
- [Python 几何](solution/math/judge_triangle/judge_triangle.py)

### [发射火箭](problem/math/launch_rocket.md)
- [Python 几何](solution/math/launch_rocket/launch_rocket.py)

### [墙壁划线](problem/math/mark_wall.md)
- [Python 数学](solution/math/mark_wall/mark_wall.py)

### [最多质数和](problem/math/max_prime.md)
- [Python 数学](solution/math/max_prime/max_prime.py)

### [最小质因数](problem/math/min_prime.md)
- [Python 内置函数](solution/math/min_prime/min_prime_1.py)
- [Python 手动构造](solution/math/min_prime/min_prime_2.py)

### [被三整除子串](problem/math/multiple_of_three.md)
- [Python 计数](solution/math/multiple_of_three/multiple_of_three_1.py)
- [Python 分组讨论](solution/math/multiple_of_three/multiple_of_three_2.py)

### [红黑数之和](problem/math/red_black_number.md)
- [Python 数论](solution/math/red_black_number/red_black_number.py)

### [计算工资](problem/math/salary.md)
- [Python 数论](solution/math/salary/salary.py)

### [发短信](problem/math/send_message.md)
- [Python 统计](solution/math/send_message/send_message.py)

### [数组相减相等](problem/math/subtract_array.md)
- [Python 数论](solution/math/subtract_array/subtract_array.py)

### [病毒](problem/math/virus.md)
- [Python 数论](solution/math/virus/virus.py)

### [最小权值和](problem/math/weight_sum.md)
- [Python 数论](solution/math/weight_sum/weight_sum.py)

## 位运算

### [lowbit求和](problem/bit/lowbit_fx_sum.md)
- [Python 位运算](solution/bit/lowbit_fx_sum/lowbit_fx_sum.py)

### [最大异或数](problem/bit/max_xor.md)
- [Python 位运算](solution/bit/max_xor/max_xor.py)

### [X与Y的对数](problem/bit/pair_of_XY.md)
- [Python 位运算](solution/bit/pair_of_XY/pair_of_XY.py)

### [减2的n次幂](problem/bit/sub_power_of_2.md)
- [Python 位运算](solution/bit/sub_power_of_2/sub_power_of_2.py)

### [异或找缺失数](problem/bit/xor_missing_number.md)
- [Python 快速异或](solution/bit/xor_missing_number/xor_missing_number_1.py)
- [Python 普通异或](solution/bit/xor_missing_number/xor_missing_number_2.py)

### [好数的异或和](problem/bit/xor_sum.md)
- [Python 内置函数](solution/bit/xor_sum/xor_sum_1.py)
- [Python 手动构造](solution/bit/xor_sum/xor_sum_2.py)

## 栈

### [括号调整次数](problem/stack/adjust_bracket.md)
- [Python 栈](solution/stack/adjust_bracket/adjust_bracket.py)

### [括号期望](problem/stack/bracket_mean.md)
- [Python DP](solution/stack/bracket_mean/bracket_mean_1.py)
- [Python 暴力枚举](solution/stack/bracket_mean/bracket_mean_2.py)

### [前缀串长度](problem/stack/prefix_length.md)
- [Python 栈计数](solution/stack/prefix_length/prefix_length_1.py)
- [Python 直接计数](solution/stack/prefix_length/prefix_length_2.py)

### [括号有效性](problem/stack/valid_bracket.md)
- [Python 栈](solution/stack/valid_bracket/valid_bracket.py)

### [合法字符串](problem/stack/valid_string.md)
- [Python 栈](solution/stack/valid_string/valid_string.py)

## 搜索

### [分苹果](problem/search/divide_apple.md)
- [Python 二分查找](solution/search/divide_apple/divide_apple.py)

### [格子染色](problem/search/dyed_plaid.md)
- [Python 图遍历](solution/search/dyed_plaid/dyed_plaid.py)

### [打僵尸](problem/search/fight_zombies.md)
- [Python DFS](solution/search/fight_zombies/fight_zombies_1.py)
- [Python BFS](solution/search/fight_zombies/fight_zombies_2.py)

### [好格子](problem/search/good_grid.md)
- [Python 图遍历](solution/search/good_grid/good_grid.py)

### [字符串插入加号](problem/search/insert_plus.md)
- [Python DFS](solution/search/insert_plus/insert_plus.py)

### [最小操作树](problem/search/min_operation.md)
- [Python BFS](solution/search/min_operation/min_operation_1.py)
- [Python DFS](solution/search/min_operation/min_operation_2.py)

### [多叉树](problem/search/multifork_tree.md)
- [Python DFS](solution/search/multifork_tree/multifork_tree.py)

### [树子节点颜色个数](problem/search/node_color.md)
- [Python BFS](solution/search/node_color/node_color_1.py)
- [Python DFS](solution/search/node_color/node_color_2.py)

### [随机加减](problem/search/random_add_sub.md)
- [Python DFS](solution/search/random_add_sub/random_add_sub.py)

## 排序

### [字典序最大序列](problem/sort/dict_order.md)
- [Python 排序](solution/sort/dict_order/dict_order.py)

### [游戏记录](problem/sort/game_record.md)
- [Python 字典](solution/sort/game_record/game_record.py)

### [最少交换次数](problem/sort/min_swap.md)
- [Python 模拟](solution/sort/min_swap/min_swap_1.py)
- [Python 归并排序](solution/sort/min_swap/min_swap_2.py)

### [数组删除](problem/sort/sort_deletion.md)
- [Python 数论](solution/sort/sort_deletion/sort_deletion.py)

### [数组模排序](problem/sort/sort_mod.md)
- [Python 排序](solution/sort/sort_mod/sort_mod.py)

### [分数排序](problem/sort/sort_score.md)
- [Python 内置函数](solution/sort/sort_score/sort_score_1.py)
- [Python 手动构造](solution/sort/sort_score/sort_score_2.py)

### [对称数组](problem/sort/symmetric_array.md)
- [Python 双指针](solution/sort/symmetric_array/symmetric_array.py)

## 动态规划

### [迷宫寻宝](problem/dp/hunt_treasure.md)
- [Python DP](solution/dp/hunt_treasure/hunt_treasure.py)

### [打地鼠](problem/dp/whack_mole.md)
- [Python DP](solution/dp/whack_mole/whack_mole_1.py)
- [Python 滑动窗口+DP](solution/dp/whack_mole/whack_mole_2.py)

### [包粽子](problem/dp/wrap_zongzi.md)
- [Python DP](solution/dp/wrap_zongzi/wrap_zongzi.py)

## 贪心

### [01字符串交换次数](problem/greedy/01_string_swap.md)
- [Python 贪心](solution/greedy/01_string_swap/01_string_swap.py)

### [加减1次数](problem/greedy/add_sub_count.md)
- [Python 贪心](solution/greedy/add_sub_count/add_sub_count.py)

### [加减1相等](problem/greedy/add_sub_equal.md)
- [Python 贪心](solution/greedy/add_sub_equal/add_sub_equal.py)

### [加减1均值](problem/greedy/add_sub_mean.md)
- [Python 贪心](solution/greedy/add_sub_mean/add_sub_mean.py)

### [炸弹](problem/greedy/bomb.md)
- [Python 内置函数](solution/greedy/bomb/bomb_1.py)
- [Python 手动构造](solution/greedy/bomb/bomb_2.py)

### [买花](problem/greedy/buy_flower.md)
- [Python 贪心](solution/greedy/buy_flower/buy_flower.py)

### [买商品](problem/greedy/buy_product.md)
- [Python 贪心](solution/greedy/buy_product/buy_product.py)

### [买文具](problem/greedy/buy_stationery.md)
- [Python 贪心](solution/greedy/buy_stationery/buy_stationery.py)

### [包车](problem/greedy/charter.md)
- [Python 贪心](solution/greedy/charter/charter.py)

### [蛇吃水果](problem/greedy/eat_fruit.md)
- [Python 贪心](solution/greedy/eat_fruit/eat_fruit.py)

### [物品价值](problem/greedy/item_value.md)
- [Python 贪心](solution/greedy/item_value/item_value.py)

### [最大非零子数组](problem/greedy/max_nonzero_subarray.md)
- [Python 贪心](solution/greedy/max_nonzero_subarray/max_nonzero_subarray.py)

### [最大正方形边长](problem/greedy/max_side.md)
- [Python 贪心](solution/greedy/max_side/max_side.py)

### [游戏嘲笑子数组](problem/greedy/mock_game.md)
- [Python 贪心](solution/greedy/mock_game/mock_game.py)

### [非递减数组](problem/greedy/non_decreasing_array.md)
- [Python 贪心](solution/greedy/non_decreasing_array/non_decreasing_array.py)

### [完美集合](problem/greedy/perfect_set.md)
- [Python 数组去重](solution/greedy/perfect_set/perfect_set.py)

### [商品折扣](problem/greedy/product_discounts.md)
- [Python 贪心](solution/greedy/product_discounts/product_discounts.py)

### [去除小于平均值的次数](problem/greedy/remove_below_mean.md)
- [Python 贪心](solution/greedy/remove_below_mean/remove_below_mean.py)

### [打枪](problem/greedy/shooting.md)
- [Python 贪心](solution/greedy/shooting/shooting.py)

### [字符串的权值](problem/greedy/string_weight.md)
- [Python 贪心](solution/greedy/string_weight/string_weight.py)

### [学生分组](problem/greedy/student_groups.md)
- [Python 贪心](solution/greedy/student_groups/student_groups.py)

### [打印次数](problem/greedy/suffix_count.md)
- [Python 贪心](solution/greedy/suffix_count/suffix_count.py)

### [有效卡片](problem/greedy/valid_card.md)
- [Python 贪心](solution/greedy/valid_card/valid_card.py)

## 模拟

### [数组加1](problem/simulation/array_add_1.md)
- [Python 模拟](solution/simulation/array_add_1/array_add_1.py)

### [对答案](problem/simulation/check_answer.md)
- [Python 模拟](solution/simulation/check_answer/check_answer.py)

### [密文解密](problem/simulation/decrypt_string.md)
- [Python 模拟](solution/simulation/decrypt_string/decrypt_string.py)

### [棋子移动](problem/simulation/move_chess.md)
- [Python 模拟](solution/simulation/move_chess/move_chess.py)

### [密码锁拨动次数](problem/simulation/password_lock.md)
- [Python 模拟](solution/simulation/password_lock/password_lock.py)

### [池化](problem/simulation/pooling.md)
- [Python 模拟](solution/simulation/pooling/pooling.py)

### [打印里字](problem/simulation/print_li.md)
- [Python 模拟](solution/simulation/print_li/print_li.py)

### [连续反转字符串](problem/simulation/reverse_string.md)
- [Python 模拟](solution/simulation/reverse_string/reverse_string.py)

### [贪吃蛇](problem/simulation/snake.md)
- [Python 模拟](solution/simulation/snake/snake.py)

### [子数组除法](problem/simulation/subarray_division.md)
- [Python 模拟](solution/simulation/subarray_division/subarray_division.py)

### [01字符串截取](problem/simulation/truncate_01_string.md)
- [Python 模拟](solution/simulation/truncate_01_string/truncate_01_string.py)

