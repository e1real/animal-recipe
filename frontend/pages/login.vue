<template>
  <div class="d-flex align-items-center flex-column">
    <h2 class="text-center my-2">Войти в приложение</h2>
    <b-alert v-if="error" show variant="danger">{{ error + '' }}</b-alert>
    <b-alert show v-if="$auth.$state.redirect">
      You have to login before accessing to <strong>{{ $auth.$state.redirect }}</strong>
    </b-alert>
    <b-card bg-variant="light" class="w-50">
      <busy-overlay/>
      <form @keydown.enter="login">
        <b-form-group label="Логин">
          <b-input v-model="form.username" placeholder="введите логин" ref="username"/>
        </b-form-group>

        <b-form-group label="Пароль">
          <b-input type="password" v-model="form.password" placeholder="введите пароль"/>
        </b-form-group>

        <div class="text-center">
          <b-btn @click="login" variant="primary" block>Войти</b-btn>
        </div>
      </form>
    </b-card>
  </div>
</template>

<script>
    import busyOverlay from '~/components/utils/busy-overlay'

    export default {
        middleware: 'auth',
        components: { busyOverlay },
        data: () => ({
            error: null,
            form: {
                username: '',
                password: ''
            }
        }),
        methods: {
            async login() {
                try {
                    await this.$auth.login({data: this.form})
                    if (this.$auth.hasScope('general')) {
                        this.$nuxt.$router.push('/general')
                    } else if (this.$auth.hasScope('admin')) {
                        this.$nuxt.$router.push('/admin')
                    }
                } catch (e) {
                    this.error = 'Login failed.'
                }
            }
        }
    }
</script>
