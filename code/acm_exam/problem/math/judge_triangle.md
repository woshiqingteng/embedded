三角形判断

知识点：数学

[类似-不可能三角](https://www.nowcoder.com/discuss/750016145939247104?sourceSSR=post)

判断输入的多个正整数数组能否构成三角形，以及与给定三角形是否相似。  
输入：  
第一行输入一个数组，代表基底三角形，输入保证是合法三角形  
第二行输入一个数字，代表即将要输入n行数组，每个数组长度为 3  
接下来输入n个数组...  
输出：  
对每组输入数组，首先判断数组能否构成三角形，如果能，接着判断是否与基底三角形相似，然后根据情况，每组判断后分别输出：("Similar"、"Can form a triangle but not similar"、"Can not form a triangle")

示例 1：
输入：
3 4 5
3
6 8 10
1 3 3
1 2 3
输出：
Similar
Can form a triangle but not similar
Can not form a triangle