<template>
  <div class="body">
    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          주차 
        </div>
      </v-col>
      <v-col cols="8">
        <div class="content">
          {{ details.parking }}
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="item" cols="2">
        <div>
          대중교통
        </div>
      </v-col>
      <v-col cols="8">
      <div class="content">
          {{ details.public }}
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="item" cols="2">
        <div>
          회사 
        </div>
      </v-col>
      <v-col cols="8">
        <div class="content">
          {{ details.type }}
        </div>
      </v-col>
    </v-row>
  </div>
</template>
<script>
export default {
  name: 'CinemaInfo',
  props: ["details"],
  components: {
  },

}
</script>

<style src="./CinemaInfo.css" scoped></style>