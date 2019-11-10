<template>
  <div class="container-fluid">
    <h4 class="text-center my-1">Создание нового рецепта</h4>
    <b-row>
      <b-col>
        <b-form-group label-size="sm" label="Наименование рецепта" label-for="input-sm">
          <b-form-input id="input-sm" size="sm"></b-form-input>
        </b-form-group>
        <div class="row">
          <div class="col">
            <div class="card d-flex py-2">
              <h6 class="h6">Общий состав всех добавленных ингредиентов</h6>
              <hr class="d-flex m-0"/>
              <div class="text-center" v-show="ingredientsLoading">
                <b-spinner type="grow" label="Spinning"></b-spinner>
              </div>
              <ul class="composition-list p-2">
                <li class="d-flex align-items-center px-1" v-for="ingredient in ingredients" :key="ingredient.value">
                  <span class="badge badge-secondary mr-1">0</span>
                  {{ ingredient.text }}
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-3">
            <div class="card p-1 my-1  d-flex align-items-center">
              <div class="d-flex flex-column justify-content-between">
                <h6 class="h6 card-head-text">Добавление ингредиента</h6>
                <div class="form-group">
                  <div>
                    <label for="choseIngredient">выберите ингредиенты</label>
                    <b-form-select id="choseIngredient" v-model="formIngredient.ingredient" :options="ingredients"
                                   size="sm"></b-form-select>
                  </div>
                </div>
                <div class="form-group">
                  <label for="input-percentage">введите процент ввода</label>
                  <input type="number" id="input-percentage" class="form-control form-control-sm"/>
                </div>
                <button class="btn btn-success btn-sm mb-2">Добавить</button>
              </div>
            </div>
          </div>
          <div class="col-md-9">
            <div class="card p-1 my-1">
              <h6 class="h6 card-head-text">Список добавленных ингредиентов</h6>
              <table class="table-fill">
                <thead>
                <tr>
                  <th class="text-left">Наименование</th>
                  <th class="text-left">Процент ввода</th>
                  <th class="text-left"></th>
                </tr>
                </thead>
                <tbody class="table-hover">
                <tr>
                  <td class="text-left">пшеница</td>
                  <td class="text-left">60</td>
                  <td class="text-left">
                    <button class="btn btn-sm btn-danger delete-btn">удалить</button>
                  </td>
                </tr>
                <tr>
                  <td class="text-left">кукуруза</td>
                  <td class="text-left">10</td>
                  <td class="text-left">
                    <button class="btn btn-sm btn-danger delete-btn">удалить</button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>
    <hr/>
    <div class="d-flex w-100">
      <b-button variant="success" class="ml-auto">Создать рецепт</b-button>
    </div>
  </div>
</template>
<script>
    export default {
        middleware: 'auth',
        data() {
            return {
                ingredients: [],
                formIngredient: {
                    ingredient: null
                },
                ingredientsLoading: false
            }
        },
        methods: {
            async getIngredients() {
                this.ingredientsLoading = true;
                const {data} = await this.$axios.get('/api/ingredients')
                data.results.forEach((ingredient, idx) => {
                    this.ingredients.push({
                        value: ingredient.id,
                        text: ingredient.name
                    })
                });
                this.ingredientsLoading = false;
            }
        },
        mounted() {
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
</style>
