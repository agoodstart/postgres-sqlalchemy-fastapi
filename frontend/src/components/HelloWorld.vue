<template>
  <ul>
    <li v-for="item in list" :key="item.path">
        {{ item.path }}
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
