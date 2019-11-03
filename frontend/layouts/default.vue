<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#">
        <Horse/>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/" class="text-uppercase" exact exact-active-class="active">рецепты</b-nav-item>
          <b-nav-item to="/orders" class="text-uppercase" exact exact-active-class="active">заказы</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <nuxt/>
  </div>
</template>
<script>
    import Horse from '~/components/icons/Horse.vue'

    export default {
        components: {
            Horse
        }
    }
</script>
<style>
  table {
    font-size: 0.8rem;
  }
</style>
