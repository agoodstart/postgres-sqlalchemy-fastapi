<template>
  <ul>
    <li v-for="item in list" :key="item.path">
        <a href="#" class="btn btn-primary">{{ item.name }}</a>
    </li>
  </ul>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Test',
  data() {
    return {
      list: [],
    };
  },
  methods: {
    getList() {
      axios.get('/')
        .then((res) => {
          this.list = res.data;
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
