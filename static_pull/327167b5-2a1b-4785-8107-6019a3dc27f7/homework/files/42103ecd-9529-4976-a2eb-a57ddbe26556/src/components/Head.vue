<template>
  <div class="pg-header">
    <div class="lf-container">
      <img class="logo" src="../assets/img/logo.png" alt="">
      <div class="nav">
        <router-link to="/index">首页</router-link>
        <router-link to="/course">课程</router-link>
        <router-link to="/micro">LuffyX学位</router-link>
        <router-link to="/news">深科技</router-link>
      </div>
      <div class="account">
        <div v-if="this.$store.state.token">
          <a>{{ this.$store.state.username }}</a>
          <a @click="logout">注销</a>
        </div>
        <router-link v-else :to="{name:'login',query:{ backUrl: this.$route.path }}">登录</router-link>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: "header",
    methods: {
      logout() {
        this.$store.commit('clearToken')
        this.$router.push({path: '/index'})
      }
    }
  }
</script>

<style scoped>
  .pg-header {
    height: 80px;
    background: #fff;
    box-shadow: 0 2px 4px 0 #c9c9c9;
    padding-bottom: 3px;

  }
  .lf-container{
    width: 980px;
    margin: 0 auto;
  }

  .logo {
    margin-top: 20px;
    float: left;
    width: 40px;
    height: 40px;
    vertical-align: middle;

  }

  .nav {
    float: left;
    margin-left: 33%;
    line-height: 80px;
  }

  .nav a {
    display: inline-block;
    padding: 0 15px;
    color: #7f7f7f;
    text-decoration: none;
  }

  .nav a:hover {
    border-bottom: 3px solid darkseagreen;
  }

  .account {
    float: right;
    line-height: 80px;
    font-size: 14px;
    color: #7f7f7f;
  }
</style>

