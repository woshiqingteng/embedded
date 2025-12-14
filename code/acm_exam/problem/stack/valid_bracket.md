括号有效性

知识点：栈

[参考-有效的括号字符串](https://leetcode.cn/problems/valid-parenthesis-string/description/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号
给定一个输入，输出是否有效

示例 1：
输入：
8
()
()[]{}
(]
([)]
{[]}
((()))
{[()]}
([)]
输出：
True
True
False
False
True
True
True
False