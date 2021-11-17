<script>
import { useRoute } from 'vue-router'
import { computed } from '@vue/reactivity'

export default {
    setup() {
        const route = useRoute()
        const id = computed(() => route.name)
        return {id}
    }
}
</script>

<template>
  <main :id="id" class="container-fluid d-flex justify-content-center align-items-center">
    <router-view />
  </main>
</template>