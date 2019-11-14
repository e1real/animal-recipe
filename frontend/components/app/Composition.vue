<template>
  <b-badge variant="dark" class="composition">
    {{name}}<span v-if="name.length > 0"></span>
    {{value}}</b-badge>
</template>
<script>
    export default {
        props: {
            name: {
                type: String,
                default: ''
            },
            value: {
                type: String,
                default: '0'
            }
        }
    }
</script>
