<template>
  <section id="single-employee">
    {{employee}}
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Single Employee',
  data() {
    return {
        employee: {},
        route: this.$route.params.id
    };
  },
  methods: {
    getEmployee() {
      axios.get(`employees/${this.route}`)
        .then((res) => {
          this.employee = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getEmployee();
  },
}
</script>
