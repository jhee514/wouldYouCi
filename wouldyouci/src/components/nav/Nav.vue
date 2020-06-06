<template>
  <v-bottom-navigation
    height="7vh"
    app
    fixed
    grow
    shift
    align="center"
  >
    <v-btn small @click="goMap">
      <span>Nearby</span>
      <v-icon>mdi-map-marker-outline</v-icon>
    </v-btn>

    <v-btn small @click="goSearch">
      <span>Search</span>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-btn small @click="goUserPage">
      <span>My Page</span>
      <v-icon>mdi-account-outline</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import router from "@/router";
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'Nav',
  computed: {
    ...mapGetters(['getSearchMode', 'isLoggedIn'])
  },
  methods: {
    ...mapMutations(['setSearchMode', 'setLoginMode']),
    goMap() {
      const link = document.location.href.split("/");
      if (link[link.length - 1]) {
        router.push('/');
      }
    },
    goSearch() {
      //실제 출시용 코드
      if (this.isLoggedIn) {
        const link = document.location.href.split("/");
        if (link[link.length - 1] !== "search") {
          router.push('/search');
        } else {
          location.reload();
        }
        if (this.getSearchMode === 'after') {
          this.setSearchMode('before');
        }
      } else {
        this.setLoginMode('login');
        router.push('/signup');
      }
    },
    goUserPage() {
      // 실제 출시용 코드
      if (this.isLoggedIn) {
        const link = document.location.href.split("/");
        if (link[link.length - 1] !== "userPage") {
          router.push('/userPage');
        } else {
          location.reload();
        }
      } else {
        this.setLoginMode('login');
        router.push('/signup');
      }
    }
  }
}
</script>

<style></style>