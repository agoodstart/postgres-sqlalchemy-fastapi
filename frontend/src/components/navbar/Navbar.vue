<script>
import NavbarLink from './NavbarLink.vue'

export default {
  props: {},
  components: {NavbarLink},
  data() {
    return {
      routes: this.$router.options.routes
    }
  }
}
</script>


<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <img
        class="logo"
        src="./../../assets/logo.png"
        alt=""
      >
      <!-- <a href="#" class="navbar-brand">Test 123</a> -->
      <div
        class="collapse navbar-collapse"
        id="navbarCollapse"
      >
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li
            v-for="route in routes"
            :key="route.path"
            class="nav-item"
          >
            <NavbarLink
              :to="route.path"
              :name="route.name"
            />
          </li>
        </ul>
        <div class="col-md-2 d-flex justify-content-around">
            <a href="/login" class="btn btn-primary btn-lg">Login</a>
          <a href="#" class="btn btn-secondary btn-lg">Sign up</a>
        </div>
        
      </div>
    </div>
  </nav>
</template>

<style scoped>
  .logo {
    width: auto;
    height: 4rem;
  }
</style>