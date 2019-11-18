<template>
  <b-badge variant="dark" class="composition">
    {{name}}<span v-if="name.length > 0">:</span>
    {{newValue}}</b-badge>
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
        },
        computed: {
            newValue() {
                return Math.sign(this.value) === -1 ? 0.00 : this.value.toFixed(2)
            }
        }
    }
</script>
