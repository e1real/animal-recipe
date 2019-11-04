<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#">
        <Horse/>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/" class="text-uppercase" exact exact-active-class="active" v-if="isAuthenticated">рецепты
          </b-nav-item>
          <b-nav-item to="/orders" class="text-uppercase" exact exact-active-class="active" v-if="isAuthenticated">
            заказы
          </b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto" >
          <b-nav-item-dropdown v-if="loggedInUser" right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              {{loggedInUser.username}}
            </template>
            <b-dropdown-item href="#" @click="logout">Выйти</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item to="/login">
            Войти
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <nuxt/>
  </div>
</template>
<script>
    import Horse from '~/components/icons/Horse.vue'
    import {mapGetters} from 'vuex'

    export default {
        components: {
            Horse
        },
        computed: {
            ...mapGetters(['isAuthenticated', 'loggedInUser'])
        },
        methods: {
            async logout() {
                await this.$auth.logout();
            }
        }

    }
</script>
<style>
  table {
    font-size: 0.8rem;
  }
</style>
