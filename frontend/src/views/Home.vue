<template>
  <div class="home">
    <div class="filters">
      <div class="filter-group">
        <el-input 
          v-model="searchQuery" 
          placeholder="搜索标签" 
          prefix-icon="el-icon-search"
          clearable
          @input="searchTags"
          class="search-input">
        </el-input>
        
        <el-select 
          v-model="selectedTag" 
          placeholder="按标签筛选" 
          clearable 
          @change="filterBlogs"
          class="tag-select">
          <el-option
            v-for="tag in filteredTags"
            :key="tag"
            :label="tag"
            :value="tag">
          </el-option>
        </el-select>
      </div>
      
      <router-link to="/random">
        <el-button type="primary" icon="el-icon-magic-stick">随机博客体验</el-button>
      </router-link>
    </div>
    
    <el-row :gutter="20" class="blog-list">
      <el-col :xs="24" :sm="12" :md="8" :lg="6" v-for="blog in blogs" :key="blog.title">
        <el-card class="blog-card">
          <div class="blog-title">{{ blog.title }}</div>
          <div class="blog-tags">
            <el-tag v-for="tag in blog.tags" :key="tag" size="mini" @click="selectTag(tag)">
              {{ tag }}
            </el-tag>
          </div>
          <div class="blog-actions">
            <el-button type="text" @click="openBlog(blog.url)">访问博客</el-button>
            <el-button type="text" v-if="blog.rss" @click="openBlog(blog.rss)">RSS</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
    
    <div class="empty-state" v-if="blogs.length === 0">
      <el-empty description="没有找到匹配的博客"></el-empty>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      blogs: [],
      tags: [],
      filteredTags: [],
      selectedTag: '',
      searchQuery: '',
      loading: false
    }
  },
  created() {
    this.fetchBlogs()
    this.fetchTags()
  },
  methods: {
    async fetchBlogs() {
      this.loading = true
      try {
        let url = '/api/blogs'
        const params = new URLSearchParams()
        
        if (this.selectedTag) {
          params.append('tag', this.selectedTag)
        }
        
        if (this.searchQuery) {
          params.append('search', this.searchQuery)
        }
        
        if (params.toString()) {
          url += `?${params.toString()}`
        }
        
        const response = await this.$http.get(url)
        this.blogs = response.data
      } catch (error) {
        console.error('Error fetching blogs:', error)
        this.$message.error('获取博客列表失败')
      } finally {
        this.loading = false
      }
    },
    async fetchTags() {
      try {
        const response = await this.$http.get('/api/tags')
        this.tags = response.data
        this.filteredTags = [...this.tags]
      } catch (error) {
        console.error('Error fetching tags:', error)
        this.$message.error('获取标签列表失败')
      }
    },
    filterBlogs() {
      this.fetchBlogs()
    },
    selectTag(tag) {
      this.selectedTag = tag
      this.fetchBlogs()
    },
    searchTags() {
      if (!this.searchQuery) {
        this.filteredTags = [...this.tags]
      } else {
        const query = this.searchQuery.toLowerCase()
        this.filteredTags = this.tags.filter(tag => 
          tag.toLowerCase().includes(query)
        )
      }
      this.fetchBlogs()
    },
    openBlog(url) {
      window.open(url, '_blank')
    }
  }
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
}

.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  align-items: center;
}

.filter-group {
  display: flex;
  gap: 10px;
  flex: 1;
  max-width: 500px;
}

.search-input {
  width: 200px;
}

.tag-select {
  width: 200px;
}

.blog-list {
  margin-top: 20px;
}

.blog-card {
  height: 180px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.blog-title {
  font-weight: bold;
  font-size: 16px;
  margin-bottom: 10px;
  flex-grow: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
}

.blog-tags {
  margin-bottom: 10px;
  min-height: 40px;
  overflow: hidden;
}

.blog-tags .el-tag {
  margin-right: 5px;
  margin-bottom: 5px;
  cursor: pointer;
}

.blog-actions {
  display: flex;
  justify-content: space-between;
}

.empty-state {
  margin-top: 40px;
}
</style> 