<template>
  <!-- <HelloWorld msg="Cambiando el mensaje"/>
  <MiComponente></MiComponente>
  <LoginPage></LoginPage> -->
  <PostList></PostList>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import MiComponente from './components/MiComponente.vue'
// import LoginPage from './pages/LoginPage.vue'
import PostList from './pages/PostList.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    // MiComponente,
    // LoginPage
    PostList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
