<template>
    <div>
        <h2>{{msg}}</h2>

        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "help",
        data(){
            return {
                msg:'一级路由，以下显示二级路由的内容'
            }
        }
    }
</script>

<style scoped>

</style>