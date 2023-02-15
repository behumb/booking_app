<template>
  <div class="isolate bg-white">
    <div class="px-6 pt-6 lg:px-8">
      <nav class="flex items-center justify-between" aria-label="Global">
        <div class="flex lg:flex-1">
          <a href="#" class="-m-0.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img class="h-8" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt=""/>
          </a>
        </div>
        <div class="flex gap-x-12">
          <router-link to="/" class="text-sm font-semibold leading-6 text-gray-900">Home</router-link>
          <router-link to="/catalog" class="text-sm font-semibold leading-6 text-gray-900">Catalog</router-link>
          <router-link to="/" class="text-sm font-semibold leading-6 text-gray-900">Contacts</router-link>
          <router-link to="/" class="text-sm font-semibold leading-6 text-gray-900">Delivery</router-link>
        </div>
        <div class="flex flex-1 justify-end">
          <router-link v-if="!isAuth" to="/login" class="text-sm font-semibold leading-6 text-gray-900">Log in <span
              aria-hidden="true">&rarr;</span></router-link>
          <a v-if="isAuth" @click="logout()" class="text-sm font-semibold leading-6 text-gray-900">Logout</a>
        </div>
      </nav>

    </div>
    <router-view/>
  </div>
</template>

<script>
import { nextTick } from 'vue'

export default {
  methods: {
    logout() {
      this.$store.dispatch('accounts/logout').then(response => {
      })
    }
  },
  computed: {
    isAuth() {
      return this.$store.state.accounts.token
    }
  },
  mounted() {
    console.log(this.$store.getters['accounts/isAuthorized'])
  },
}
</script>
