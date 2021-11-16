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
        <form class="d-flex">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          >
          <button
            class="btn btn-outline-success"
            type="submit"
          >
            Search
          </button>
        </form>
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