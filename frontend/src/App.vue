<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1>博客导航</h1>
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
</style> 