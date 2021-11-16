<template>
  <!-- <ul>
    <li v-for="item in list" :key="item.path">
        <a href="#" class="btn btn-primary">{{ item.name }}</a>
    </li>
  </ul> -->
  <div>
    {{ employee }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Test',
  data() {
    return {
      employee: {},
    };
  },
  methods: {
    getList() {
      axios.get('/')
        .then((res) => {
          this.employee = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getList();
  },
}
</script>
