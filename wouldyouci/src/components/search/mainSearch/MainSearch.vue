<template>
  <div>
    <div class="content">
      <div style="text-align : left">근처 영화관<br/></div>
      <CinemaList v-bind:CinemaList="CinemaList" />
    </div>
    <div class="current">
      <div style="text-align : left">현재 상영작 순위<br/></div>
      <CinemaList v-bind:CinemaList="CinemaList" />
    </div>
    <div class="released">
      <div style="text-align : left"> 개봉예정작<br/></div>
      <CinemaList v-bind:CinemaList="CinemaList" />
    </div>
  </div>
</template>

<script>
import CinemaList from '../cinemaList/CinemaList.vue';

export default {
   name: 'Search',
   components: {
     CinemaList
   },
   props:['CinemaList']


}
</script>

<style src="./MainSearch.css" scoped></style>