from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import csv
import random
import os
import re

app = Flask(__name__, static_folder='../frontend/dist')
CORS(app)  # 启用跨域

# 标签映射表，将相似标签合并
TAG_MAPPING = {
    '前端': ['前端', '前端开发', '前端笔记', 'Web', 'web开发'],
    '后端': ['后端', '后端开发', 'Java', 'PHP', 'Go', 'Golang', 'Python'],
    '算法': ['算法', '数据结构'],
    '移动开发': ['iOS', 'Android', '移动开发'],
    '开源': ['开源'],
    '编程': ['编程', '程序员', '代码'],
    '架构': ['架构', '系统设计'],
    '人工智能': ['机器学习', '深度学习', 'AI', '人工智能'],
    '生活': ['生活', '随笔', '日常', '思考'],
    '创业': ['创业', '产品'],
    '设计': ['设计', 'UI', 'UX'],
}

# 读取博客数据
def load_blogs():
    blogs = []
    with open('../blogs-original.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳过标题行
        for row in reader:
            if len(row) >= 4:
                original_tags = [tag.strip() for tag in row[3].split(';')] if row[3] else []
                
                # 应用标签映射，合并相似标签
                normalized_tags = normalize_tags(original_tags)
                
                blog = {
                    'title': row[0].strip(),
                    'url': row[1].strip(),
                    'rss': row[2].strip(),
                    'tags': normalized_tags,
                    'original_tags': original_tags
                }
                blogs.append(blog)
    return blogs

# 标签归一化，将相似标签合并为主标签
def normalize_tags(tags):
    normalized = set()
    for tag in tags:
        if not tag:
            continue
            
        # 检查标签是否在映射表中
        found = False
        for main_tag, similar_tags in TAG_MAPPING.items():
            if any(re.search(similar, tag, re.IGNORECASE) for similar in similar_tags):
                normalized.add(main_tag)
                found = True
                break
                
        # 如果没有匹配的映射，保留原标签
        if not found:
            normalized.add(tag)
            
    return sorted(list(normalized))

# 获取所有标签
def get_all_tags(blogs):
    tags = set()
    for blog in blogs:
        for tag in blog['tags']:
            if tag:
                tags.add(tag)
    return sorted(list(tags))

# 路由 - 获取所有博客
@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = load_blogs()
    tag = request.args.get('tag', '')
    search = request.args.get('search', '').lower()
    
    # 按标签筛选
    if tag:
        blogs = [blog for blog in blogs if tag in blog['tags']]
    
    # 按标签搜索
    if search:
        blogs = [blog for blog in blogs if any(search in t.lower() for t in blog['tags'])]
    
    return jsonify(blogs)

# 路由 - 获取所有标签
@app.route('/api/tags', methods=['GET'])
def get_tags():
    blogs = load_blogs()
    tags = get_all_tags(blogs)
    return jsonify(tags)

# 路由 - 获取随机博客（支持多标签筛选）
@app.route('/api/random', methods=['GET'])
def get_random_blog():
    blogs = load_blogs()
    if not blogs:
        return jsonify({'error': 'No blogs available'}), 404
    
    # 获取所有tag参数（可以有多个）
    tags = request.args.getlist('tag')
    
    # 如果指定了标签，只在符合标签的博客中随机选择
    if tags:
        filtered_blogs = []
        for blog in blogs:
            # 检查博客是否包含所有指定的标签
            if all(tag in blog['tags'] for tag in tags):
                filtered_blogs.append(blog)
        
        # 如果没有符合所有标签的博客，返回错误
        if not filtered_blogs:
            return jsonify({'error': 'No blogs with the specified tags'}), 404
        
        random_blog = random.choice(filtered_blogs)
    else:
        random_blog = random.choice(blogs)
    
    return jsonify(random_blog)

# 服务前端静态文件
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 