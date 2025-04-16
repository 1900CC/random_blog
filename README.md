# 博客导航网站

这是一个展示博客列表的Web应用，提供按标签筛选和随机访问功能。

## 技术栈

- 后端：Python 3.9 + Flask
- 前端：Vue.js + Element UI
- 环境：Node.js v16.15.1, npm 8.11.0

## 项目结构

```
blogs-web/
├── backend/            # Flask后端
│   ├── app.py          # 主应用程序
│   └── requirements.txt # Python依赖
├── frontend/           # Vue前端
│   ├── public/         # 静态资源
│   ├── src/            # 源代码
│   │   ├── assets/     # 资源文件
│   │   ├── components/ # 组件
│   │   ├── router/     # 路由
│   │   ├── views/      # 视图
│   │   ├── App.vue     # 根组件
│   │   └── main.js     # 入口文件
│   ├── .gitignore      # Git忽略文件
│   ├── babel.config.js # Babel配置
│   ├── package.json    # 依赖管理
│   └── vue.config.js   # Vue配置
└── blogs-original.csv  # 博客数据文件
```

## 功能特性

- 博客列表展示
- 按标签筛选博客
- 随机访问博客
- 响应式设计

## 安装和运行

### 后端

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 前端

```bash
cd frontend
npm install
npm run serve
```

访问 http://localhost:8080 查看应用。

## 构建生产环境版本

```bash
cd frontend
npm run build
```

然后使用Flask提供静态文件：

```bash
cd backend
python app.py
```

访问 http://localhost:5000 查看生产环境应用。 