<template>
    <Navbar />
    <Main />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
}

main {
  height: 80%;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
// @ is an alias to /src
import Navbar from '@/components/navbar/Navbar.vue'
import Main from '@/components/general/Main.vue'

export default {
  // name: 'Navbar',
  components: {
    Navbar,
    Main
  }
}
</script>