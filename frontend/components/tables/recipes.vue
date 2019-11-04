<template>
  <div>
    <b-card class="mt-2 mb-0">
      <h6 class="h6">Фильтры:</h6>
      <b-row>
        <b-col md="8">
          <b-form-group
            label="Поиск по таблице"
            label-for="filterInput"
            label-size="sm">
            <b-input-group size="sm">
              <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="введите данные для поиска"
              ></b-form-input>
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''">Очистить</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form-group>
        </b-col>
        <b-col md="4">
          <b-form-group
            label="Показать на таблице"
            label-for="perPageSelect"
            label-size="sm">
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions">
            </b-form-select>
          </b-form-group>
        </b-col>
      </b-row>
      <hr>
      <div class="d-flex justify-content-between mb-2">

        <h6 class="h6">Таблица с рецептами:</h6>
        <b-button variant="success" size="sm">Создать рецепт</b-button>
      </div>
      <b-table
        show-empty
        :small="true"
        :hover="true"
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
          <b-button size="sm" @click="row.toggleDetails" variant="primary" class="very-sm-btn">
            редактировать
          </b-button>
          <b-button size="sm" @click="row.toggleDetails" variant="danger" class="very-sm-btn">
            удалить
          </b-button>
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
      ></b-pagination>
    </b-card>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    {isActive: true, age: 40, name: {first: 'Dickerson', last: 'Macdonald'}},
                    {isActive: false, age: 21, name: {first: 'Larsen', last: 'Shaw'}},
                    {
                        isActive: false,
                        age: 9,
                        name: {first: 'Mini', last: 'Navarro'},
                        _rowVariant: 'success'
                    },
                    {isActive: false, age: 89, name: {first: 'Geneva', last: 'Wilson'}},
                    {isActive: true, age: 38, name: {first: 'Jami', last: 'Carney'}},
                    {isActive: false, age: 27, name: {first: 'Essie', last: 'Dunlap'}},
                    {isActive: true, age: 40, name: {first: 'Thor', last: 'Macdonald'}},
                    {
                        isActive: true,
                        age: 87,
                        name: {first: 'Larsen', last: 'Shaw'},
                        _cellVariants: {age: 'danger', isActive: 'warning'}
                    },
                    {isActive: false, age: 26, name: {first: 'Mitzi', last: 'Navarro'}},
                    {isActive: false, age: 22, name: {first: 'Genevieve', last: 'Wilson'}},
                    {isActive: true, age: 38, name: {first: 'John', last: 'Carney'}},
                    {isActive: false, age: 29, name: {first: 'Dick', last: 'Dunlap'}}
                ],
                fields: [
                    {key: 'name', label: 'Наименование', sortable: true, sortDirection: 'desc'},
                    {key: 'age', label: 'Person age', sortable: true, class: 'text-center'},
                    {
                        key: 'isActive',
                        label: 'is Active',
                        formatter: (value, key, item) => {
                            return value ? 'Yes' : 'No'
                        },
                        sortable: true,
                        sortByFormatted: true,
                        filterByFormatted: true
                    },
                    {key: 'actions', label: 'Actions'}
                ],
                totalRows: 1,
                currentPage: 1,
                perPage: 5,
                pageOptions: [5, 10, 15, 25, 50],
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: null,
                filterOn: []
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
            // Set the initial number of items
            this.totalRows = this.items.length
        },
        methods: {
            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length
                this.currentPage = 1
            }
        }
    }
</script>
<style scoped lang="scss">
  .very-sm-btn {
    padding: .1rem .3rem;
    font-size: .7rem;
  }
</style>
