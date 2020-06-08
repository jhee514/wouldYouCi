<template>
  <div>
    <v-slide-group
      class="pa-4 cinemaList"
      active-class="success"
      v-if="TheaterList && TheaterList.length"
    >
      <v-slide-item
        v-for="(theater, idx) in TheaterList"
        :key="idx"
      >
        <v-card
          dark
          height="auto"
          width="50vw"
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
      </v-slide-item>
    </v-slide-group>
    <v-card
      v-else
      class="noContent"
      height="20vh"
      width="90vw"
      style="margin-right:2vh"
    >
      <div class="noContentExp">
        해당 콘텐츠가 없습니다.
      </div>
    </v-card>
  </div>
</template>

<script>
import router from '../../../router';
export default {
  name: 'TheaterMovie',
  props: ['TheaterList', 'Label'],
  methods: {
    goDetail(id) {
      router.push(`/cinema/${id}`)
    }
  }
}
</script>

<style src="./MovieList.css" scoped></style>