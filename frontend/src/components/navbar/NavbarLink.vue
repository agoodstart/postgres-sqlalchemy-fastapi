<script>
import { computed } from '@vue/reactivity'
import { useRoute } from 'vue-router'

export default {
    props: {
        to: { type: String, required: true},
        name: {type: String, required: true}
    },
    setup(props) {
        const route = useRoute()
        const isActive = computed(() => route.path === props.to)
        return {isActive}
    }
}
</script>

<template>
  <router-link
    :to="to"
    class="nav-link"
    :class="{active: isActive}"
  >
    {{ name }}
  </router-link>
</template>