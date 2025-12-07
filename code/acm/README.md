# ACM算法笔记

## 目录

- [数学](#数学)
  - [六边形面积](#六边形面积)
  - [字符串转换](#字符串转换)
  - [三角形判断](#三角形判断)
  - [函数 f(x)=lowbit(x) 的求和](#函数-fxlowbitx-的求和)
  - [墙壁划线](#墙壁划线)
  - [最多质数和](#最多质数和)
  - [最小质因数](#最小质因数)
  - [被三整除子串](#被三整除子串)
  - [发短信](#发短信)
  - [异或找缺失数](#异或找缺失数)
  - [好数的异或和](#好数的异或和)
- [栈](#栈)
  - [括号调整次数](#括号调整次数)
  - [前缀串长度](#前缀串长度)
  - [括号有效性](#括号有效性)
- [队列](#队列)
  - [字符串加减 1](#字符串加减-1)
- [图](#图)
  - [格子染色](#格子染色)
  - [打僵尸](#打僵尸)
  - [棋子移动](#棋子移动)
- [动态规划](#动态规划)
  - [括号期望](#括号期望)
  - [随机加减](#随机加减)
- [贪心](#贪心)
  - [01 字符串交换次数](#01-字符串交换次数)
  - [加减 1 次数](#加减-1-次数)
  - [加减 1 相等](#加减-1-相等)
  - [加减 1 均值](#加减-1-均值)
  - [大胃王比赛](#大胃王比赛)
  - [买花](#买花)
  - [买文具](#买文具)
  - [对答案](#对答案)
  - [分苹果](#分苹果)
  - [k 个子序列极差和最大](#k-个子序列极差和最大)
  - [物品价值](#物品价值)
  - [最大非零子数组](#最大非零子数组)
  - [游戏嘲笑子数组](#游戏嘲笑子数组)
  - [密码锁拨动次数](#密码锁拨动次数)
  - [商品折扣](#商品折扣)
  - [字符串的权值](#字符串的权值)
  - [学生分组](#学生分组)
  - [打印次数](#打印次数)
  - [病毒](#病毒)
- [字符串](#字符串)
  - [字符串拼接](#字符串拼接)
  - [红黑数之和](#红黑数之和)
- [排序](#排序)
  - [数组模排序](#数组模排序)
  - [分数排序](#分数排序)
- [双指针](#双指针)
  - [字符串统计](#字符串统计)
- [模拟](#模拟)
  - [打印里字](#打印里字)
  - [01 字符串截取](#01-字符串截取)
- [分治](#分治)
  - [池化](#池化)

---

## 题目统计

| 分类 | 题目数量 |
|------|----------|
| 数学 | 11 |
| 栈 | 3 |
| 队列 | 1 |
| 图 | 3 |
| 动态规划 | 2 |
| 贪心 | 19 |
| 字符串 | 2 |
| 排序 | 2 |
| 双指针 | 1 |
| 模拟 | 2 |
| 分治 | 1 |
| **总计** | **47** |

## 数学

### [六边形面积](problem\math\area_of_hexagon.md)
- [Python 数学](solution\math\area_of_hexagon\area_of_hexagon.py)

### [字符串转换](problem\math\convert_string_by_index.md)
- [Python 数学](solution\math\convert_string_by_index\convert_string_by_index.py)

### [三角形判断](problem\math\judge_triangle.md)
- [Python 数学](solution\math\judge_triangle\judge_triangle.py)

### [函数 f(x)=lowbit(x) 的求和](problem\math\lowbit_fx_sum.md)
- [Python 位运算](solution\math\lowbit_fx_sum\lowbit_fx_sum.py)

### [墙壁划线](problem\math\mark_wall.md)
- [Python 数学](solution\math\mark_wall\mark_wall.py)

### [最多质数和](problem\math\max_prime.md)
- [Python 数学](solution\math\max_prime\max_prime.py)

### [最小质因数](problem\math\min_prime.md)
- [Python 数学](solution\math\min_prime\min_prime.py)

### [被三整除子串](problem\math\multiple_of_three.md)
- [Python 数学](solution\math\multiple_of_three\multiple_of_three.py)

### [发短信](problem\math\send_message.md)
- [Python 数学](solution\math\send_message\send_message.py)

### [异或找缺失数](problem\math\xor_missing_number.md)
- [Python 数学](solution\math\xor_missing_number\xor_missing_number.py)

### [好数的异或和](problem\math\xor_sum.md)
- [Python 数学](solution\math\xor_sum\xor_sum.py)

## 栈

### [括号调整次数](problem\stack\adjust_bracket.md)
- [Python 栈](solution\stack\adjust_bracket\adjust_bracket.py)

### [前缀串长度](problem\stack\prefix_length.md)
- [Python 栈](solution\stack\prefix_length\prefix_length_1.py)
- [Python 计数](solution\stack\prefix_length\prefix_length_2.py)

### [括号有效性](problem\stack\valid_bracket.md)
- [Python 栈](solution\stack\valid_bracket\valid_bracket.py)

## 队列

### [字符串加减 1](problem\queue\add_sub_string.md)
- [Python 枚举](solution\queue\add_sub_string\add_sub_string_1.py)
- [Python 队列](solution\queue\add_sub_string\add_sub_string_2.py)

## 图

### [格子染色](problem\graph\dyed_plaid.md)
- [Python 图遍历](solution\graph\dyed_plaid\dyed_plaid.py)

### [打僵尸](problem\graph\fight_zombies.md)
- [Python DFS](solution\graph\fight_zombies\fight_zombies_1.py)
- [Python BFS](solution\graph\fight_zombies\fight_zombies_2.py)

### [棋子移动](problem\graph\move_chess.md)
- [Python 状态机](solution\graph\move_chess\move_chess.py)

## 动态规划

### [括号期望](problem\dp\bracket_mean.md)
- [Python DP](solution\dp\bracket_mean\bracket_mean.py)

### [随机加减](problem\dp\random_add_sub.md)
- [Python DFS](solution\dp\random_add_sub\random_add_sub.py)

## 贪心

### [01 字符串交换次数](problem\greedy\01_string_swap.md)
- [Python 贪心](solution\greedy\01_string_swap\01_string_swap.py)

### [加减 1 次数](problem\greedy\add_sub_count.md)
- [Python 贪心](solution\greedy\add_sub_count\add_sub_count.py)

### [加减 1 相等](problem\greedy\add_sub_equal.md)
- [Python 贪心](solution\greedy\add_sub_equal\add_sub_equal.py)

### [加减 1 均值](problem\greedy\add_sub_mean.md)
- [Python 贪心](solution\greedy\add_sub_mean\add_sub_mean.py)

### [大胃王比赛](problem\greedy\big_eater.md)
- [Python 贪心](solution\greedy\big_eater\big_eater.py)

### [买花](problem\greedy\buy_flower.md)
- [Python 贪心](solution\greedy\buy_flower\buy_flower.py)

### [买文具](problem\greedy\buy_stationery.md)
- [Python 贪心](solution\greedy\buy_stationery\buy_stationery.py)

### [对答案](problem\greedy\check_answer.md)
- [Python 贪心](solution\greedy\check_answer\check_answer.py)

### [分苹果](problem\greedy\divide_apple.md)
- [Python 贪心](solution\greedy\divide_apple\divide_apple.py)

### [k 个子序列极差和最大](problem\greedy\extreme_sum.md)
- [Python 贪心](solution\greedy\extreme_sum\extreme_sum.py)

### [物品价值](problem\greedy\item_value.md)
- [Python 贪心](solution\greedy\item_value\item_value.py)

### [最大非零子数组](problem\greedy\max_nonzero_subarray.md)
- [Python 贪心](solution\greedy\max_nonzero_subarray\max_nonzero_subarray.py)

### [游戏嘲笑子数组](problem\greedy\mock_game.md)
- [Python 贪心](solution\greedy\mock_game\mock_game.py)

### [密码锁拨动次数](problem\greedy\password_lock.md)
- [Python 贪心](solution\greedy\password_lock\password_lock.py)

### [商品折扣](problem\greedy\product_discounts.md)
- [Python 贪心](solution\greedy\product_discounts\product_discounts.py)

### [字符串的权值](problem\greedy\string_weight.md)
- [Python 贪心](solution\greedy\string_weight\string_weight.py)

### [学生分组](problem\greedy\student_groups.md)
- [Python 贪心](solution\greedy\student_groups\student_groups.py)

### [打印次数](problem\greedy\suffix_count.md)
- [Python 贪心](solution\greedy\suffix_count\suffix_count.py)

### [病毒](problem\greedy\virus.md)
- [Python 贪心](solution\greedy\virus\virus.py)

## 字符串

### [字符串拼接](problem\string\concatenate_string.md)
- [Python 字符串](solution\string\concatenate_string\concatenate_string.py)

### [红黑数之和](problem\string\red_black_number.md)
- [Python 贪心](solution\string\red_black_number\red_black_number.py)

## 排序

### [数组模排序](problem\sort\sort_mod.md)
- [Python 冒泡排序](solution\sort\sort_mod\sort_mod.py)

### [分数排序](problem\sort\sort_score.md)
- [Python 排序](solution\sort\sort_score\sort_score.py)

## 双指针

### [字符串统计](problem\two-pointers\string_count.md)
- [Python 双指针](solution\two-pointers\string_count\string_count_1.py)
- [Python 枚举](solution\two-pointers\string_count\string_count_2.py)

## 模拟

### [打印里字](problem\simulation\print_li.md)
- [Python 模拟](solution\simulation\print_li\print_li.py)

### [01 字符串截取](problem\simulation\truncate_01_string.md)
- [Python 模拟](solution\simulation\truncate_01_string\truncate_01_string.py)

## 分治

### [池化](problem\divide-and-rule\pooling.md)
- [Python 分治](solution\divide-and-rule\pooling\pooling.py)

