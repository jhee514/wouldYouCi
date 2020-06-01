<template>
  <div>
    <div class="content">
      <div style="text-align : left">근처 영화관<br/></div>
      <TheaterList v-bind:TheaterList="TheaterList" />
    </div>
    <div class="current">
      <div style="text-align : left">현재 상영작 순위<br/></div>
      <CinemaList v-bind:CinemaList="Populars" />
    </div>
    <div class="released">
      <div style="text-align : left"> 개봉예정작<br/></div>
      <CinemaList v-bind:CinemaList="Commings" />
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
   props:['Commings', 'Populars', 'TheaterList']


}
</script>

<style src="./MainSearch.css" scoped></style>