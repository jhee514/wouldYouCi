<template>
  <div class="body">
    <v-row no-gutters>
      <!-- <v-col class="item" cols="3">
        <span>
          홈페이지
        </span>
      </v-col>
      <v-col cols="9">
        <span class="content">
          <v-btn
            text
            target="_blank"
            :href="details.url" 
            >
            홈페이지
          </v-btn>
        </span>
      </v-col> -->
    </v-row>
    <v-row>
      <v-col class="item" cols="3">
        <span>
          주차 
        </span>
      </v-col>
      <v-col cols="9">
        <p 
          class="content"
          >
          {{ details.parking }}
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="item" cols="3">
        <span>
          대중교통
        </span>
      </v-col>
      <v-col cols="9">
        <p class="content">
          {{ details.public }}
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="item" cols="3">
        <span>
          회사 
        </span>
      </v-col>
      <v-col cols="9">
        <span class="content">
          {{ details.type }}
        </span>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="item" cols="3">
        <span>
          전화
        </span>
      </v-col>
      <v-col cols="9">
      <a 
        class="tel"
        :href="`tel:+${ details.tel }`">
        {{ details.tel }}
      </a>
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