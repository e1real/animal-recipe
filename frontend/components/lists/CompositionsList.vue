<template>
  <div class="composition-list-wrapper">
    <b-badge variant="dark" class="composition" v-for="(composition, key) in compositions" :key="composition.id" ref="compositions">{{composition.name}}: 0</b-badge>
  </div>
</template>
<script>
    export default {
        props: {
            compositions: {
                type: Array,
                default: []
            }
        }
    }
</script>


<style lang="scss" scoped>
  .composition-list-wrapper {
    display: flex;
    width: 100%;

    .composition {
      margin-right: 10px;
    }
  }
</style>
