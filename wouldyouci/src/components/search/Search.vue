<template>
<v-app>
  <div class='search'>
    <div class ="grid">
      <div class="header">
        <h1>🍿우리 주변의 씨네마<br/></h1>
        <i class="fas fa-search-location fa-2x ">현재위치</i>
       
      </div>

      <div class="search">
        
         <v-form v-model="valid">
      <v-container>
            <v-text-field
              v-model="firstname"
              prepend-icon="fa fa-search"
              :rules="rules"
              :counter="10"
              label="영화관을 찾아보세요!"
              required
            ></v-text-field>
      </v-container>
     </v-form> 
      </div>
      <div class="content">
        <div style="text-align : left">근처 영화관<br/></div>
        <nearby-theater/>
      </div>
      <div class="current">
         <div style="text-align : left">현재 상영작 순위<br/></div>
        <curRankings />
      </div>
      <div class="released">
         <div style="text-align : left"> 개봉예정작<br/></div>
        <movie-release/>
      </div>

      <div class="nav">
      

      </div>
      <div class="footer">
        Would Ci !

      </div>
    </div>
  </div>
  </v-app>
</template>

<script>
import curRankings from './curRankings.vue';
import nearbyTheater from './nearbyTheater.vue';
import movieRelease from './movieRelease.vue';

export default {
   name: 'Search',
   components:{
     curRankings,
     nearbyTheater,
     movieRelease,
   },
   model: [],
   data: () => ({
    rules: [
      value => !!value || '영화관을 검색해보세요!',
      value => (value || '').length <= 20 || '최대 글자수는 20글자 입니다.',
      value => {
        const pattern =  /([^가-힣ㄱ-ㅎㅏ-ㅣ\x20])/i
        return !pattern.test(value) || '한글만 적어주세요.'
      },
    ],
   cards: [
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex:4},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex:4 },
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex:4 },
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex:4},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex:4 },
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex:4 },
    ],
  }),

}
</script>

<style src="./Search.css" scoped></style>