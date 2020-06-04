<template>
  <v-app>
    <v-content>
    <div id="app" data-app>
      <router-view />
    </div>
    </v-content>
    <Nav />
  </v-app>
</template>

<script>
import Nav from './nav/Nav';
export default {
  components: {
    Nav
  },
  created() {
    this.$store.dispatch("initialLogin");
  }
};
</script>

<style>
</style>
