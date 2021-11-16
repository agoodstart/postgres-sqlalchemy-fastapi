<template>
  <div class="home">
    <Homecard />
  </div>
</template>

<script>
// @ is an alias to /src
import Homecard from '@/components/Homecard.vue'

export default {
  name: 'Home',
  components: {
    Homecard
  }
}
</script>
