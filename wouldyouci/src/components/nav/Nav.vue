<template>
  <v-bottom-navigation
    grow
    color="teal"
    height="7vh"
    fixed
  >
    <v-btn @click="goMap">
      <v-icon>fas fa-map-marked-alt</v-icon>
    </v-btn>

    <v-btn @click="goSearch">
      <v-icon>fas fa-film</v-icon>
    </v-btn>

    <v-btn @click="goUserPage">
      <v-icon>fas fa-user</v-icon>
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
    ...mapMutations(['setSearchMode']),
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
        }
        if (this.getSearchMode === 'after') {
          this.setSearchMode('before');
        }
      } else {
        router.push('/signup');
      }

      //개발 중 코드
      // const link = document.location.href.split("/");
      // if (link[link.length - 1] !== "search") {
      //   router.push('/search');
      // }
      // if (this.getSearchMode === 'after') {
      //   this.setSearchMode('before');
      // }
    },
    goUserPage() {
      // 실제 출시용 코드
      if (this.isLoggedIn) {
        const link = document.location.href.split("/");
        if (link[link.length - 1] !== "userPage") {
          router.push('/userPage');
        }
      } else {
        router.push('signup');
      }

      // 개발용 코드
      // const link = document.location.href.split("/");
      // if (link[link.length - 1] !== "userPage") {
      //   router.push('/userPage');
      // }
    }
  }
}
</script>

<style></style>