<template>
  <div>
    <Title />
    <div class='userPage'>
      <div class="settingIcon">
        <v-icon class="setting" @click="isShow=!isShow">fas fa-cog</v-icon>
        <v-dialog v-model="isShow">
          <SettingCard />
        </v-dialog>
      </div>
      <UserInfo />
      <span>선호하는 영화관</span>
      <MovieList v-bind:CinemaList="theaterList"/>
      <span>내가 평가한 영화</span>
      <MovieList v-bind:CinemaList="ratedMovies"/>
      <span>찜한 영화</span>
      <MovieList v-bind:CinemaList="wishMovies"/>
      <span>나에게 추천하는 영화</span>
      <MovieList v-bind:CinemaList="recommendedMovies"/>
      <span>내 영화 스타일</span>
      <div style="height:50vh; background-color:grey; margin-bottom: 10vh; margin-top: 3vh"></div>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import UserInfo from './userInfo/UserInfo.vue';
import MovieList from './movieList/MovieList.vue';
import SettingCard from './settingCard/SettingCard.vue';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title,
    UserInfo,
    MovieList,
    SettingCard
  },
  data() {
    return {
      theaterList: ['강남 CGV', '코엑스 메가박스'],
      ratedMovies: ['톰보이', '레이니 데이 인 뉴욕', '트롤: 월드 투어', '콜 오브 와일드', '프리즌 이스케이프', '더 플랫폼', '저 산 너머', '씨 피버', '패왕별희'],
      wishMovies: ['카페 벨에포크', '라스트 풀 메저', '킬러의 보디가드', '루키스', '나는 보리', '비커밍 제인'],
      recommendedMovies: ['배고파...', '집이지만', '집에 가고파', '월요병', '스마일감자', '나쁘다....'],
      isShow: false
    }
  }
}
</script>

<style src="./UserPage.css" scoped></style>