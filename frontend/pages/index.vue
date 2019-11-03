<template>
  <b-container fluid>
    <h4 class="h4 my-2 text-center">Рецепты</h4>
    <recipes-table/>
  </b-container>
</template>

<script>
    import RecipesTable from "~/components/tables/recipes.vue"

    export default {
        middleware: 'auth',
        components: {
            RecipesTable
        },
        data() {
            return {
                columns: [
                    {
                        title: 'Item ID',
                        field: 'id'
                    },
                    {
                        field: 'name',
                        title: 'Item Name'
                    },
                    {
                        field: 'price',
                        title: 'Item Price'
                    }
                ],
                data: [
                    {
                        id: 1,
                        name: 'Item 1',
                        price: '$1'
                    }
                ],
                options: {
                    search: true,
                    showColumns: true
                }
            }
        }
    }
</script>

<style>

</style>
