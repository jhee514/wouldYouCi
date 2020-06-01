<template>
  <div>
    <Title />
    <div class='userPage'>
      <div class="settingIcon">
        <v-icon class="setting" @click="isShow=!isShow">fas fa-cog</v-icon>
        <v-dialog v-model="isShow">
          <SettingCard @settingCard="closeDialog" />
        </v-dialog>
        <v-dialog v-model="isShowChangeImgDialog">
          <ChangeUserImage v-if="isShowChangeImgDialog" @changeUserImage="closeChangeImgDialog" @changeP="changeP"/>
        </v-dialog>
        <v-dialog v-model="isShowChangePassDialog">
          <ChangeUserPass v-if="isShowChangePassDialog" @changeUserPass="closeChangePassDialog"/>
        </v-dialog>
      </div>
      <UserInfo v-bind:UserName="userName" v-bind:UserProfile="profileURL" @deleteP="deleteP"/>
      <div class="tabs">
        <v-tabs
          v-model="tab"
          background-color="transparent"
          grow
        >
          <v-tab
            v-for="item in items"
            :key="item"
          >
            {{ item }}
          </v-tab>
        </v-tabs>
      </div>
      <div class="prefer" v-if="tab===0">
        <span>선호하는 영화관</span>
        <MovieList v-bind:CinemaList="theaterList"/>
        <span>찜한 영화</span>
        <MovieList v-bind:CinemaList="wishMovies"/>
        <span>나에게 추천하는 영화</span>
        <MovieList v-bind:CinemaList="recommendedMovies"/>
        <span>내 영화 스타일</span>
        <div style="height:50vh; margin-bottom: 10vh; margin-top: 3vh; background-color:#FFC9E1; text-align:center; padding-top:5vh;">
          현재 데이터가 부족해 내 영화 스타일에 대한 분석이 불가능 합니다.
          <div style="padding-top:5vh;">
            <v-btn text @click="goFirstRating">
              영화 평가하러 가기
              <v-icon small style="margin-left:3vw;">fas fa-arrow-right</v-icon>
            </v-btn>
          </div>
        </div>
      </div>
      <div class="rating" v-else>
        <RatingMovies v-bind:CinemaList="ratedMovies"/>
      </div>
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
import ChangeUserImage from './changeUserInfo/ChangeUserImage.vue';
import ChangeUserPass from './changeUserInfo/ChangeUserPass.vue';
import RatingMovies from './ratingMovies/RatingMovies.vue';
import router from '../../router';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title,
    UserInfo,
    MovieList,
    SettingCard,
    ChangeUserImage,
    ChangeUserPass,
    RatingMovies
  },
  data() {
    return {
      theaterList: null,
      ratedMovies: ['톰보이', '레이니 데이 인 뉴욕', '트롤: 월드 투어', '콜 오브 와일드', '프리즌 이스케이프', '더 플랫폼', '저 산 너머', '씨 피버', '패왕별희'],
      wishMovies: null,
      recommendedMovies: ['배고파...', '집이지만', '집에 가고파', '월요병', '스마일감자', '나쁘다....'],
      isShow: false,
      isShowChangeImgDialog: false,
      isShowChangePassDialog: false,
      userName: null,
      profileURL: null,
      tab: 0,
      items: ['내가 선호하는 영화', '내가 평가한 영화']
    }
  },
  computed: {
    ...mapGetters(['getUserInfo'])
  },
  methods: {
    ...mapActions(['bringUserInfo']),
    closeDialog(type) {
      if (type === "image") {
        this.isShowChangeImgDialog = true;
      } else if (type === "password") {
        this.isShowChangePassDialog = true;
      }
      this.isShow = false;
    },
    closeChangeImgDialog() {
      this.isShowChangeImgDialog = false;
    },
    closeChangePassDialog() {
      this.isShowChangePassDialog = false;
    },
    goFirstRating() {
      router.push('/firstRating');
    },
    async deleteP() {
      await this.bringUserInfo();
      if (this.getUserInfo.file.length) {
        const HOST = process.env.VUE_APP_SERVER_HOST;
        this.profileURL = `${HOST}/${this.getUserInfo.file[0]}`;
      } else {
        this.profileURL = null;
      }
    },
    async changeP() {
      await this.bringUserInfo();
      if (this.getUserInfo.file.length) {
        const HOST = process.env.VUE_APP_SERVER_HOST;
        this.profileURL = `${HOST}/${this.getUserInfo.file[0]}`;
      } else {
        this.profileURL = null;
      }
    }
  },
  async mounted() {
    await this.bringUserInfo();
    const HOST = process.env.VUE_APP_SERVER_HOST;
    if (this.getUserInfo.file.length) {
      this.profileURL = `${HOST}/${this.getUserInfo.file[0]}`;
    }
    this.userName = this.getUserInfo.username;
    this.theaterList = this.getUserInfo.pick_cinemas;
    this.wishMovies = this.getUserInfo.pick_movies;
  }
}
</script>

<style src="./UserPage.css" scoped></style>