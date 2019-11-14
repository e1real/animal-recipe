<template>
  <div class="container-fluid">
    <h4 class="text-center my-3">Создание нового рецепта</h4>
    <hr class="mb-0"/>
    <div>
      <h6 class="my-3 text-center">Наименование ингредиента</h6>
      <b-form-input placeholder="Введите наименование рецепта" v-model="formRecipe.name" class="mt-1 mb-2"
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
        <b-button variant="success" size="sm" class="my-2 align-self-end" @click="addIngredient()">Добавить</b-button>
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
        <div class="composition-list-wrapper">
          <composition
            v-for="(composition, key) of compositions"
            :key="key"
            :name="composition.name"
            :value="composition.value"
          />
        </div>
        <b-form-input v-model="filter" placeholder="Введите данные для пойска" class="mt-1 mb-2"
                      size="sm"></b-form-input>

        <b-table
          show-empty
          empty-text="пусто"
          empty-filtered-text="ничего не найдено"
          small
          bordered
          borderless
          hover
          head-variant="light"
          table-variant="light"
          stacked="md"
          :items="formRecipe.ingredients"
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
            <b>{{ row.value }}</b>
          </template>
          <template v-slot:cell(compositions)="row">
              <span v-if="row.item.compositions"
                    v-for="(value, key) in row.item.compositions"
                    :key="key">
                <span style="font-weight: 500">{{value.composition_name}}:</span>
                {{ value.percentage}}<span v-if="row.item.compositions.length -1 !== key">, </span>
              </span>
          </template>

          <template v-slot:cell(actions)="row">
            <svg
              @click="removeIngredient(row.index)"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="feather feather-trash">
              <polyline
                points="3 6 5 6 21 6"
                color="red"></polyline>
              <path color="red"
                    d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
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
    import CompositionsList from '~/components/lists/CompositionsList.vue'
    import Composition from '~/components/app/Composition.vue'

    export default {
        middleware: 'auth',
        components: {searcherSelect, CompositionsList, Composition},
        data() {
            return {
                selectedIngredient: null,
                ingredients: [],
                ingredientsLoading: false,

                formRecipe: {
                    name: '',
                    ingredients: []
                },

                compositions: {},
                existCompositions: null,
                fields: [
                    {key: 'name', label: 'Наименование', sortable: true, sortDirection: 'desc'},
                    {key: 'compositions', label: 'Состав'},
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
            /** Get all ingredients for dropdown. */
            async getIngredients() {
                this.ingredientsLoading = true;
                const {data} = await this.$axios.get('/api/ingredients');
                this.ingredients = data;
                this.ingredientsLoading = false;
            },
            /** Get all existing compositions. */
            async getAllCompositions() {
                const {data} = await this.$axios.get('/api/compositions/');
                // this.compositions = data;
                data.forEach((value, idx) => {
                    this.compositions[value.id] = {
                        name: value.name,
                        value: 0
                    };
                });
            },
            addIngredient() {
                const exist = this.formRecipe.ingredients.find((el) => {
                    return el.id === this.selectedIngredient.id;
                });
                if (!exist) {
                    this.formRecipe.ingredients.push(this.selectedIngredient);
                    let compositions = this.selectedIngredient.compositions;
                    compositions.forEach((value, idx) => {
                        this.compositions[value.composition_id].value += Number(value.percentage);
                    });
                    return;
                }
                alert('Ингредиент существует');
            },
            removeIngredient(idx) {
                const ingredient = this.formRecipe.ingredients[idx];
                ingredient.compositions.forEach((value, idx) => {
                    this.compositions[value.composition_id].value -= Number(value.percentage);
                });
                this.formRecipe.ingredients.splice(idx, 1);
            },
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length;
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
            this.getIngredients();
            this.getAllCompositions();

            this.totalRows = this.formRecipe.ingredients.length;
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

  .composition-list-wrapper {
    display: flex;
    flex-wrap: wrap;
    width: 100%;

    .composition {
      margin-right: 5px;
      margin-top: 5px;
    }
  }
</style>
