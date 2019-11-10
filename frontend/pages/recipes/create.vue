<template>
  <div class="container-fluid">
    <h4 class="text-center my-3">Создание нового рецепта</h4>
    <hr class="mb-0"/>
    <div>
      <h6 class="my-3 text-center">Наименование ингредиента</h6>
      <b-form-input placeholder="Введите наименование рецепта" class="mt-1 mb-2"
                    size="sm"></b-form-input>
    </div>

    <div class="area-wrapper">
      <div class="search-ingredient">
        <h6 class="my-3 text-center">Найти ингредиент</h6>
        <div>
          <searcher-select :options="ingredients" @selected="selectedIngredient = $event"
                           placeholder="Выберите ингредиент" class="search-select">
          </searcher-select>
          <div class="info-icon-wrapper align-self-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                 class="feather feather-alert-circle" id="dropDownInfoIcon">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
          </div>
        </div>
        <b-button variant="success" size="sm" class="my-2 align-self-end">Добавить</b-button>
        <b-tooltip target="dropDownInfoIcon" placement="top">
          <div v-if="selectedIngredient">
            <ul style="list-style: none;margin: 0;padding: 0">
              <li v-for="composition in selectedIngredient.compositions">
                {{composition.composition_name}} - {{composition.percentage}}
              </li>
            </ul>
          </div>
          <span v-else>Информация о выбранном ингредиенте</span>
        </b-tooltip>
      </div>
      <div class="ingredients-list">
        <h6 class="my-3">Список добавленных ингредиентов</h6>
        <b-form-input v-model="filter" placeholder="Введите данные для пойска" class="mt-1 mb-2"
                      size="sm"></b-form-input>

        <b-table
          show-empty
          small
          bordered
          borderless
          hover
          head-variant="light"
          table-variant="light"
          stacked="md"
          :items="items"
          :fields="fields"
          :current-page="currentPage"
          :per-page="perPage"
          :filter="filter"
          :filterIncludedFields="filterOn"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
          :sort-direction="sortDirection"
          @filtered="onFiltered"
        >
          <template v-slot:cell(name)="row">
            {{ row.value.first }} {{ row.value.last }}
          </template>

          <template v-slot:cell(actions)="row">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                 class="feather feather-trash">
              <polyline points="3 6 5 6 21 6" color="red"></polyline>
              <path color="red" d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
            <!--            <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">-->
            <!--              Info modal-->
            <!--            </b-button>-->
            <!--            <b-button size="sm" @click="row.toggleDetails">-->
            <!--              {{ row.detailsShowing ? 'Hide' : 'Show' }} Details-->
            <!--            </b-button>-->
          </template>

          <template v-slot:row-details="row">
            <b-card>
              <ul>
                <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
              </ul>
            </b-card>
          </template>
        </b-table>
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          size="sm"

        ></b-pagination>
      </div>
    </div>
    <hr/>
    <div class="d-flex w-100">
      <b-button variant="success" class="ml-auto">Создать рецепт</b-button>
    </div>
  </div>
</template>
<script>
    import searcherSelect from '~/components/forms/searcherSelect.vue'

    export default {
        middleware: 'auth',
        components: {searcherSelect},
        data() {
            return {
                selectedIngredient: null,
                ingredients: [],
                formIngredient: {
                    ingredient: null
                },
                ingredientsLoading: false,

                // Table
                items: [
                    // {isActive: true, age: 40, name: {first: 'Dickerson', last: 'Macdonald'}},
                    // {isActive: false, age: 21, name: {first: 'Larsen', last: 'Shaw'}},
                    // {
                    //     isActive: false,
                    //     age: 9,
                    //     name: {first: 'Mini', last: 'Navarro'},
                    //     _rowVariant: 'success'
                    // },
                    // {isActive: false, age: 89, name: {first: 'Geneva', last: 'Wilson'}},
                    // {isActive: true, age: 38, name: {first: 'Jami', last: 'Carney'}},
                    // {isActive: false, age: 27, name: {first: 'Essie', last: 'Dunlap'}},
                    // {isActive: true, age: 40, name: {first: 'Thor', last: 'Macdonald'}},
                    // {
                    //     isActive: true,
                    //     age: 87,
                    //     name: {first: 'Larsen', last: 'Shaw'},
                    //     _cellVariants: {age: 'danger', isActive: 'warning'}
                    // },
                    // {isActive: false, age: 26, name: {first: 'Mitzi', last: 'Navarro'}},
                    // {isActive: false, age: 22, name: {first: 'Genevieve', last: 'Wilson'}},
                    // {isActive: true, age: 38, name: {first: 'John', last: 'Carney'}},
                    // {isActive: false, age: 29, name: {first: 'Dick', last: 'Dunlap'}}
                ],
                fields: [
                    {key: 'name', label: 'Наименование', sortable: true, sortDirection: 'desc'},
                    {key: 'age', label: 'Ингредиенты', sortable: true, class: 'text-center'},
                    // {
                    //     key: 'isActive',
                    //     label: 'is Active',
                    //     formatter: (value, key, item) => {
                    //         return value ? 'Yes' : 'No'
                    //     },
                    //     sortable: true,
                    //     sortByFormatted: true,
                    //     filterByFormatted: true
                    // },
                    {key: 'actions', label: 'Действие'}
                ],
                totalRows: 1,
                currentPage: 1,
                perPage: 10,
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: '',
                filterOn: [],
                infoModal: {
                    id: 'info-modal',
                    title: '',
                    content: ''
                }

            }
        }
        ,
        methods: {
            async getIngredients() {
                this.ingredientsLoading = true;
                const {data} = await this.$axios.get('/api/ingredients');
                this.ingredients = data.results;
                // data.results.forEach((ingredient, idx) => {
                //     this.ingredients.push({
                //         value: ingredient.id,
                //         text: ingredient.name
                //     })
                // });
                this.ingredientsLoading = false;
            },

            info(item, index, button) {
                this.infoModal.title = `Row index: ${index}`
                this.infoModal.content = JSON.stringify(item, null, 2)
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
            },
            resetInfoModal() {
                this.infoModal.title = ''
                this.infoModal.content = ''
            },
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length
                this.currentPage = 1
            }
        },
        computed: {
            sortOptions() {
                // Create an options list from our fields
                return this.fields
                    .filter(f => f.sortable)
                    .map(f => {
                        return {text: f.label, value: f.key}
                    })
            }
        },

        mounted() {
            this.totalRows = this.items.length;
            this.getIngredients();
        }
    }
</script>
<style scoped lang="scss">
  .composition-list {
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    margin: 0;
    padding: 0;
    font-size: .8rem;
  }

  .add-ingredient-wrapper {
    /*display: flex;*/

    /*.search-select {*/
    /*  display: flex;*/
    /*  flex-grow: 1;*/
    /*}*/

    /*.feather-alert-circle {*/
    /*  display: flex;*/
    /*  flex-grow: 3;*/
    /*}*/
  }

  .area-wrapper {
    display: grid;
    grid-template-columns: .4fr 1fr;

    @media (max-width: 720px) {
      grid-template-columns: 1fr;
    }

    .search-ingredient {
      align-self: baseline;

      div {
        display: flex;
      }
    }

    .dropdown-wrapper {
      flex-basis: 80%;
    }

    .ingredients-list {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }

  .info-icon-wrapper {
    margin-left: .4rem;
  }
</style>
