字符串的权值

[参考-字符串拆分若干个子串权值和](https://blog.csdn.net/weixin_58779667/article/details/154494999)
[参考-字符串拆分2个子串权值和](https://wenku.csdn.net/answer/4yht7v7c8a)

知识点：贪心、枚举（困难）

一个字符串的权值定义为 a-b,其中 a 定义为字符串中存在偶数个字符的个数，b 定义为字符串中存在奇数个字符的个数。输入一个字符串，可以任何位置分割成两个子串，求所有子串权值和的最大值。

示例 1：  
输入：  
eggff
a
aabb
abcabc
输出：  
1  
-1
2
3