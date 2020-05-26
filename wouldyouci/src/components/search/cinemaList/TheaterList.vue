<template>
  <v-slide-group
    class="pa-4 cinemaList"
    active-class="success"
  >
    <v-slide-item
      v-for="(theater, idx) in TheaterList"
      :key="idx"
    >
      <v-card
        v-if="theater !== 'Nothing'"
        class="ma-4"
        height="20vh"
        width="50vw"
        style="margin-right:2vh"
        @click="goDetail(theater.id)"
      >
        <v-img 
          :src=theater.img
          height="15vh"
          width="50vw"
        >
        </v-img>
        <v-card-text><h4>{{ theater.name }}</h4></v-card-text>
      </v-card>

      <v-card
        v-else
        class="ma-4"
        height="20vh"
        width="90vw"
        style="margin-right:2vh"
      >
      <div>
        근처에 영화관이 없습니다.
      </div>
      </v-card>
    </v-slide-item>
  </v-slide-group>
</template>

<script>
import router from '../../../router';
export default {
  name: 'TheaterMovie',
  props: ['TheaterList'],
  methods: {
    goDetail(id) {
      router.push(`/cinema/${id}`)
    }
  }
}
</script>

<style src="./CinemaList.css" scoped></style>