<template>
  <div class="footWrap">
    <div class="main">
      <div class="foot-link">
        <router-link v-for="(item,key) in guid" :key="key" :to="{name:item.link}">{{item.text}}
        </router-link>
      </div>
      <p class="base-style">Copyright &copy; Luffycity.com版权所有</p>
    </div>
  </div>


</template>

<script>
  export default {
    name: "footer",
    data() {
      return {
        guid: [
          {text: '关于我们', link: 'about-us'},
          {text: '意见反馈', link: 'feedback'},
          {text: '新手指南', link: 'user-note'},
        ]
      }
    }
  }
</script>

<style scoped>
  .footWrap {
    width: 100%;
    height: 128px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #25292E;
  }

  .main {
    width: 435px;
  }

  .foot-link {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;

  }

  .base-style {
    font-size: 14px;
    color: #FFFFFF;
    letter-spacing: 0.22px;
    display: flex;
    justify-content: center;
  }

  .foot-link a {
    color: white;
  }
</style>
