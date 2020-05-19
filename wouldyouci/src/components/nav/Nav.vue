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

export default {
  name: 'Nav',
  methods: {
    goMap() {
      router.push('/');
    },
    goSearch() {
      const link = document.location.href.split("/");
      if (link[link.length - 1] !== "search") {
        router.push('/search');
      }
    },
    goUserPage() {
      const link = document.location.href.split("/");
      if (link[link.length - 1] !== "userPage") {
        router.push('/userPage');
      }
    }
  }
}
</script>

<style></style>