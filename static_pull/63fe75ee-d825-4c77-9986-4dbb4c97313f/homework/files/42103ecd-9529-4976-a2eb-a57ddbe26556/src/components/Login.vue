<template>
  <div class="login">
    <form>
      <div class="login-row">
        <label>用户名: </label><input type="text" placeholder="请输入用户名" v-model="username"/>
      </div>
      <div class="login-row">
        <label>密码: </label><input v-model="password" type="password" placeholder="请输入密码"/>
      </div>
      <div class="login-row">
        <a class="btn" v-on:click="doLogin">登陆</a>
        <span class="error" v-text="error"></span>
      </div>
    </form>
  </div>

</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        username: '',
        password: '',
        error: ''
      }
    },
    methods: {
      doLogin() {
        this.$axios.request({
          url: this.$store.state.apiList.auth,
          method: 'POST',
          data: {
            username: this.username,
            password: this.password
          },
          headers:{
            'Content-Type:':'application/json'
          },
          responseType: 'json'
        }).then(function (arg) {

        }).catch(function (arg) {

        })

        if (this.username === 'oldboy' && this.password === '123') {
          let obj = {username: 'oldboy', token: 'jsudfnksdjwe8234sdfsdkf'}
          this.$store.commit('saveToken', obj)
          let backUrl = this.$route.query.backUrl
          if (backUrl) {
            this.$router.push({path: backUrl})
          } else {
            this.$router.push('/index')
          }
        } else {
          this.error = '用户名或秘密错误'
        }
      }
    }
  }
</script>

<style scoped>
  .login {
    padding: 60px;
    width: 340px;
    margin: 0 auto;
    min-height: 300px;
  }

  .login .login-row {
    padding: 20px 0;
  }

  .login label {
    width: 70px;
    text-align: right;
    display: inline-block;
    margin-right: 10px;
  }

  .login input[type='text'], input[type='password'] {
    width: 250px;
    height: 28px;
  }

  .login .btn {
    float: right;
    display: inline-block;
    border: 1px solid #dddd;
    padding: 5px 15px;
    background: #7ed321;
    color: white;
    font-size: 14px;
  }

  .login .error {
    float: right;
    display: inline-block;
    padding: 5px;
  }
</style>
