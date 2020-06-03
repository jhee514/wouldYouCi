<template>
  <v-app>
  <div id="app" data-app>
    <router-view />
  </div>
  </v-app>
</template>

<script>
export default {
  created() {
    this.$store.dispatch("initialLogin");
  }
};
</script>

<style>
</style>
