<template>
<v-bottom-navigation
  v-model="bottomNav"
  color="amber"
  horizontal
  height="5vh"
  app
  fixed
  grow
  hide-on-scroll
  shift
  align="center"
  >
    <v-btn @click="goMap">
      <v-icon small>mdi-map-marker-outline</v-icon>
      <span>Nearby</span>
    </v-btn>

    <v-btn @click="goSearch">
      <v-icon small>mdi-magnify</v-icon>
      <span>Search</span>
    </v-btn>

    <v-btn @click="goUserPage">
      <v-icon small>mdi-account-outline</v-icon>
      <span>My Page</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import router from "@/router";
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'Nav',
  computed: {
    ...mapGetters(['getSearchMode', 'isLoggedIn']),
  },
  methods: {
    ...mapMutations(['setSearchMode']),
    goMap() {
      this.bottomNav = 0
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
        } else {
          location.reload();
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

<style>
  v-btn {
    padding: 0;
  }

  v-icon {
    size: x-small;
  }

  span {
    font-size: 1.5vh;
    bottom: 0;
    top: 0.5vh;
  }
</style>