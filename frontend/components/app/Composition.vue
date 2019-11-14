<template>
  <b-badge variant="dark" class="composition">
    {{name}}<span v-if="name.length > 0">:</span>
    {{value.toFixed(2)}}</b-badge>
</template>
<script>
    export default {
        props: {
            name: {
                type: String,
                default: ''
            },
            value: {
                type: Number,
                default: 0
            }
        }
    }
</script>
