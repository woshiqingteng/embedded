#!/usr/bin/env python3
"""
自动更新主索引文件
支持中英文分类映射、Doxygen注释提取和多语言文件映射
修复题目标题读取方式
"""

import re
from pathlib import Path

# 分类名称映射（英文->中文）
CATEGORY_MAPPING = {
    'string': '字符串',
    'math': '数学',
    'bit': '位运算',
    'stack': '栈',
    'search': '搜索',
    'sort': '排序',
    'dp': '动态规划',
    'greedy': '贪心',  
    'simulation': '模拟'
}

# 文件后缀到语言名称的映射
LANGUAGE_MAPPING = {
    '.cpp': 'C++',
    '.cc': 'C++',
    '.cxx': 'C++',
    '.c': 'C',
    '.py': 'Python',
    '.java': 'Java',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.go': 'Go',
    '.rs': 'Rust'
}

def extract_problem_title(first_line):
    """从第一行提取题目标题"""
    # 去掉开头的#和空格
    title = first_line.strip()
    
    # 匹配标题格式：# 标题
    if title.startswith('#'):
        # 去掉#以及后面可能的空格
        title = title[1:].lstrip()
        
        # 如果还有#，继续去掉（处理##、###等情况）
        while title.startswith('#'):
            title = title[1:].lstrip()
    
    return title.strip()

def extract_solution_description(content):
    """从代码内容提取解法描述"""
    # 精确匹配@brief所在行
    patterns = [
        r'@brief\s+(.*?)(?:\*/|$)',      # C++/Java风格
        r'@brief\s+(.*?)(?:\"\"\"|$)',    # Python风格
        r'@brief\s+(.*?)(?:\n|$)'         # 通用匹配
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            description = match.group(1).strip()
            # 清理描述文本，移除可能的特殊字符
            description = re.sub(r'[*/\"]', '', description).strip()
            return description
    
    return "解法描述"

def scan_problems():
    """扫描题目目录，返回分类和题目信息"""
    categories = {}
    
    for problem_file in Path('problem').rglob('*.md'):
        category = problem_file.parent.name
        if category not in categories:
            categories[category] = []
        
        # 读取题目标题
        try:
            with open(problem_file, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                title = extract_problem_title(first_line)
        except Exception as e:
            print(f"读取题目文件 {problem_file} 失败: {e}")
            title = problem_file.stem
        
        # 查找解法
        problem_name = problem_file.stem
        solution_dir = Path('solution') / category / problem_name
        solutions = []
        
        if solution_dir.exists():
            for solution_file in solution_dir.iterdir():
                if solution_file.is_file():
                    file_ext = solution_file.suffix.lower()
                    language = LANGUAGE_MAPPING.get(file_ext, file_ext.upper())
                    
                    # 检查文件名格式
                    pattern1 = rf'{re.escape(problem_name)}_(\d+){re.escape(file_ext)}'
                    pattern2 = rf'{re.escape(problem_name)}{re.escape(file_ext)}'
                    
                    match = re.match(pattern1, solution_file.name, re.IGNORECASE)
                    solution_num = "1"
                    
                    if match:
                        solution_num = match.group(1)
                    else:
                        # 尝试第二种模式
                        match = re.match(pattern2, solution_file.name, re.IGNORECASE)
                        if not match:
                            continue
                    
                    # 提取解法描述
                    try:
                        with open(solution_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            description = extract_solution_description(content)
                    except Exception as e:
                        print(f"读取解法文件 {solution_file} 失败: {e}")
                        description = "解法描述"
                    
                    solutions.append((language, solution_num, description, solution_file))
            
            # 按语言和序号排序
            if solutions:
                language_order = list(LANGUAGE_MAPPING.values())
                solutions.sort(key=lambda x: (
                    language_order.index(x[0]) if x[0] in language_order else len(language_order),
                    int(x[1])
                ))
        
        categories[category].append({
            'title': title,
            'problem_path': problem_file,
            'solutions': solutions
        })
    
    return categories

def get_sorted_categories(categories):
    """获取排序后的分类列表"""
    mapped = [(cat, CATEGORY_MAPPING.get(cat, cat)) for cat in CATEGORY_MAPPING if cat in categories]
    unmapped = [(cat, CATEGORY_MAPPING.get(cat, cat)) for cat in categories if cat not in CATEGORY_MAPPING]
    unmapped.sort(key=lambda x: x[1])
    return mapped + unmapped

def generate_index_content(categories):
    """生成索引文件内容"""
    if not categories:
        return "# ACM算法笔记\n\n暂无题目\n"
    
    content = "# ACM算法笔记\n\n## 目录\n\n"
    
    # 生成目录
    sorted_categories = get_sorted_categories(categories)
    for category, category_name in sorted_categories:
        content += f"- [{category_name}](#{category_name})\n"
        for problem in categories[category]:
            # 创建锚点（将标题转换为链接友好的格式）
            anchor = re.sub(r'[^\w\- ]', '', problem['title']).replace(' ', '-')
            content += f"  - [{problem['title']}](#{anchor})\n"
    
    content += "\n---\n\n## 题目统计\n\n| 分类 | 题目数量 |\n|------|----------|\n"
    
    # 生成统计表格
    total = 0
    for category, category_name in sorted_categories:
        count = len(categories[category])
        total += count
        content += f"| {category_name} | {count} |\n"
    
    content += f"| **总计** | **{total}** |\n\n"
    
    # 生成分类内容
    for category, category_name in sorted_categories:
        if categories[category]:
            content += f"## {category_name}\n\n"
            for problem in categories[category]:
                problem_path_str = problem['problem_path'].as_posix()
                content += f"### [{problem['title']}]({problem_path_str})\n"
                
                if problem['solutions']:
                    for lang, num, desc, path in problem['solutions']:
                        path_str = path.as_posix()
                        content += f"- [{lang} {desc}]({path_str})\n"
                else:
                    content += "*暂无解法*\n"
                
                content += "\n"
    
    return content

def main():
    """主函数"""
    print("正在扫描目录结构...")
    categories = scan_problems()
    
    print("生成索引内容...")
    index_content = generate_index_content(categories)
    
    print("写入README.md...")
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    total_categories = len(categories)
    total_problems = sum(len(problems) for problems in categories.values())
    print(f"索引更新完成！统计: {total_categories} 个分类, {total_problems} 个题目")
    
    # 打印调试信息
    print("\n扫描到的分类和题目:")
    for category, problems in categories.items():
        category_name = CATEGORY_MAPPING.get(category, category)
        print(f"  {category_name}: {len(problems)}个题目")
        for problem in problems:
            print(f"    - {problem['title']}: {len(problem['solutions'])}个解法")

if __name__ == "__main__":
    main()