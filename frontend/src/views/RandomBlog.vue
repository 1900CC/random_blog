<template>
  <div class="random-blog">
    <div class="page-header">
      <h1>随机博客</h1>
      <p class="description">发现精彩，偶遇知识，开启随机阅读之旅</p>
    </div>

    <div class="action-container">
      <div class="quote-box" v-if="randomBlog">
        <p class="quote">"阅读是在别人思想的帮助下建立自己的思想"</p>
      </div>
      <el-button 
        type="primary" 
        size="large" 
        @click="goToRandomBlog" 
        :loading="loading"
        icon="el-icon-magic-stick"
        class="random-button">
        探索新世界
      </el-button>
    </div>

    <div class="preview-container" v-if="randomBlog">
      <div class="preview-header">
        <h2>你的发现</h2>
        <div class="discovery-count">发现计数: {{ discoveryCount }}</div>
      </div>
      <el-card class="blog-preview" :body-style="{ padding: '0px' }">
        <div class="blog-card-content">
          <div class="blog-title">{{ randomBlog.title }}</div>
          <div class="blog-tags">
            <el-tag v-for="tag in randomBlog.tags" :key="tag" size="mini" type="info" effect="plain">
              {{ tag }}
            </el-tag>
          </div>
          <div class="blog-actions">
            <el-button type="primary" @click="openBlog(randomBlog.url)" icon="el-icon-view">查看博客</el-button>
            <el-button v-if="randomBlog.rss" @click="openBlog(randomBlog.rss)" icon="el-icon-connection" type="info">RSS</el-button>
          </div>
        </div>
      </el-card>
    </div>

    <div class="welcome-container" v-else>
      <i class="el-icon-discover discovery-icon"></i>
      <p class="welcome-text">点击上方按钮，发现精彩博客</p>
    </div>

    <div class="back-home">
      <router-link to="/home"><el-button icon="el-icon-back">返回博客列表</el-button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomBlog',
  data() {
    return {
      loading: false,
      randomBlog: null,
      discoveryCount: 0
    }
  },
  created() {
    // 从本地存储恢复上次的随机博客
    const savedBlog = localStorage.getItem('lastRandomBlog')
    if (savedBlog) {
      try {
        this.randomBlog = JSON.parse(savedBlog)
      } catch (e) {
        console.error('无法解析保存的博客数据', e)
      }
    }
    
    // 获取发现计数
    const count = localStorage.getItem('discoveryCount')
    this.discoveryCount = count ? parseInt(count) : 0
  },
  methods: {
    async goToRandomBlog() {
      this.loading = true
      try {
        const response = await this.$http.get('/api/random')
        
        if (response.data && response.data.url) {
          this.randomBlog = response.data
          
          // 更新发现计数
          this.discoveryCount++
          localStorage.setItem('discoveryCount', this.discoveryCount)
          
          // 保存到本地存储
          localStorage.setItem('lastRandomBlog', JSON.stringify(this.randomBlog))
          
          // 打开博客
          window.open(response.data.url, '_blank')
        } else {
          this.$message.warning('没有找到符合条件的博客')
        }
      } catch (error) {
        console.error('获取随机博客失败:', error)
        this.$message.error('获取随机博客失败')
      } finally {
        this.loading = false
      }
    },
    openBlog(url) {
      window.open(url, '_blank')
    }
  }
}
</script>

<style scoped>
.random-blog {
  max-width: 800px;
  margin: 0 auto;
  padding: 30px 20px;
  min-height: 80vh;
  display: flex;
  flex-direction: column;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
}

.page-header h1 {
  font-size: 36px;
  color: #409EFF;
  margin-bottom: 15px;
  letter-spacing: 1px;
}

.description {
  color: #606266;
  font-size: 18px;
  font-weight: 300;
}

.action-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
  background: linear-gradient(135deg, #e0f2ff 0%, #e8f6ff 100%);
  padding: 40px 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.action-container:hover {
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.12);
  transform: translateY(-5px);
}

.quote-box {
  margin-bottom: 30px;
  text-align: center;
}

.quote {
  font-style: italic;
  color: #606266;
  font-size: 18px;
  font-weight: 300;
}

.random-button {
  font-size: 22px;
  padding: 18px 50px;
  font-weight: bold;
  border-radius: 50px;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(64, 158, 255, 0.3);
}

.random-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(64, 158, 255, 0.4);
}

.preview-container {
  margin-bottom: 40px;
  background-color: #f9fafc;
  padding: 30px;
  border-radius: 12px;
  border: 1px solid #ebeef5;
  transition: all 0.3s ease;
}

.preview-container:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.preview-header h2 {
  font-size: 22px;
  color: #303133;
  margin: 0;
}

.discovery-count {
  color: #909399;
  font-size: 16px;
}

.blog-preview {
  overflow: hidden;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.blog-card-content {
  padding: 25px;
  background-color: white;
}

.blog-title {
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 15px;
  color: #409EFF;
}

.blog-tags {
  margin-bottom: 25px;
}

.blog-tags .el-tag {
  margin-right: 8px;
  margin-bottom: 8px;
}

.blog-actions {
  display: flex;
  gap: 15px;
}

.welcome-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 50px 0;
  color: #909399;
  padding: 40px;
  border: 2px dashed #dcdfe6;
  border-radius: 12px;
}

.discovery-icon {
  font-size: 60px;
  margin-bottom: 20px;
  color: #c0c4cc;
}

.welcome-text {
  font-size: 18px;
}

.back-home {
  text-align: center;
  margin-top: auto;
  padding-top: 20px;
}
</style> 