<template>
  <div id="app">
    <el-container>
      <el-header>
        <div class="header-content">
          <h1>博客导航</h1>
          <div class="main-nav">
            <router-link to="/" class="nav-item">
              <el-button type="text">博客列表</el-button>
            </router-link>
            <router-link to="/random" class="nav-item">
              <el-button type="text">随机博客</el-button>
            </router-link>
          </div>
        </div>
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
      <el-footer>
        <p>博客列表网站 &copy; 2025</p>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.el-header {
  background-color: #409EFF;
  color: white;
  text-align: center;
  line-height: 60px;
  padding: 0 20px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
}

.main-nav {
  display: flex;
}

.nav-item {
  margin-left: 20px;
  text-decoration: none;
}

.el-button--text {
  color: white;
  font-size: 16px;
}

.el-button--text:hover {
  color: #f0f9ff;
}

.el-footer {
  background-color: #f5f7fa;
  color: #909399;
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #ffffff;
  color: #333;
  text-align: center;
  padding: 20px;
  min-height: calc(100vh - 120px);
}

/* 路由过渡动画 */
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style> 