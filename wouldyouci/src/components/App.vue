<template>
  <v-app>
    <div id="app" data-app>
      <router-view />
    </div>
    <Nav v-if="getLoginMode === null"/>
  </v-app>
</template>

<script>
import Nav from './nav/Nav';
import { mapGetters } from 'vuex';

export default {
  components: {
    Nav
  },
  computed: {
    ...mapGetters(['getLoginMode'])
  },
  created() {
    this.$store.dispatch("initialLogin");
  }
};
</script>

<style>
</style>
