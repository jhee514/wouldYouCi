<template>
  <div>
    <div class="content">
      <TheaterList v-bind:Label="'근처 영화관'" v-bind:pos="pos" v-bind:TheaterList="TheaterList" />
    </div>
    <div class="current">
      <CinemaList v-bind:Label="'현재 상영작 순위'" v-bind:CinemaList="Populars" />
    </div>
    <div class="released">
      <CinemaList v-bind:Label="'개봉예정작'" v-bind:CinemaList="Commings" />
    </div>
  </div>
</template>

<script>
import CinemaList from '../cinemaList/CinemaList.vue';
import TheaterList from '../cinemaList/TheaterList.vue';

export default {
   name: 'Search',
   components: {
     CinemaList,
     TheaterList
   },
   props:['Commings', 'Populars', 'TheaterList', 'pos']


}
</script>

<style src="./MainSearch.css" scoped></style>