<template>
  <div>
    <h1>{{msg}}</h1>
    <div>
      <div v-for="item in courseList">
        <router-link :to="{name:'detail',params:{id:item.id}}">{{item.name}}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "course",
    data() {
      return {
        msg: '这是课程',
        courseList: []
      }
    },
    mounted() {
      this.init()
    },
    methods: {
      init() {
        this.courseList = [
          {id: 1, name: '21天学会Python', img: ''},
          {id: 2, name: '21天学会Java', img: ''},
          {id: 3, name: '21天学会Linux', img: ''},
          {id: 4, name: '21天学会大数据', img: ''},
        ]
      },
    }
  }
</script>

<style scoped>

</style>
