<template>
  <div id="app">

    <LHeader/>

    <router-view/>

    <LFooter/>


  </div>
</template>

<script>
  import LHeader from './components/Head'
  import LFooter from './components/Foot'

  export default {
    name: 'App',
    components: {
      LHeader,
      LFooter
    }
  }
</script>

<style>
  body {
    margin: 0;
  }
</style>
