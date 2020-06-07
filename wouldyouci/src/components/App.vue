<template>
  <v-app>
    <div id="app" class="app" data-app>
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
  .app {
    font-family: 'NanumBarunGothicOTF', monospace, 'Nanum Myeongjo', 'Noto Serif KR', 'Noto Sans KR', serif;
  }
</style>
