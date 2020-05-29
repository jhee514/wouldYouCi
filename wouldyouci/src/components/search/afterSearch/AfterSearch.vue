<template>
  <div class="afterSearch">
    <div v-if="CinemaList || Similar">
      <div v-if="CinemaList">
        <div class="keyword">
          {{ KeyWords }} 에 대한 검색 결과입니다.
        </div>
        <CinemaList v-bind:CinemaList="CinemaList" />
      </div>
      <div v-if="CinemaList && Similar">
        <v-divider
          style="margin-bottom:2vh;"
        ></v-divider>
      </div>
      <div v-if="Similar">
        <div class="keyword">
          {{ KeyWords }} 에 대한 유사 검색 결과입니다.
        </div>
        <CinemaList v-bind:CinemaList="Similar" />
      </div>
    </div>
    <div v-else>
      <div class="keyword" style="margin-bottom: 3vh;">
        {{ KeyWords }} 에 대한 검색 결과과 없습니다.
      </div>
      <div>
        현재 상영 중인 추천 영화
      </div>
      <CinemaList v-bind:CinemaList="CinemaList" />
    </div>
  </div>
</template>

<script>
import CinemaList from '../cinemaList/CinemaList.vue';

export default {
   name: 'AfterSearch',
   props: ['KeyWords', 'CinemaList', 'Similar'],
   components: {
     CinemaList,
   }
}
</script>

<style src="./AfterSearch.css" scoped></style>