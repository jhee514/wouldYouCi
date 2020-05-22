<template>
  <div id="app" data-app>
    <router-view />
  </div>
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
