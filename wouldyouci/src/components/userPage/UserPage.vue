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
        <TheaterList v-bind:TheaterList="theaterList"/>
        <span>찜한 영화</span>
        <MovieList v-bind:CinemaList="wishMovies"/>
        <span>나에게 추천하는 상영 중 영화</span>
        <MovieList v-if="recommendedOnscreen.length" v-bind:CinemaList="recommendedOnscreen"/>
        <v-card class="noReco" v-else>
          <div class="exp">
            현재 데이터가 부족해 영화 추천이 불가능 합니다.
          </div>
          <v-btn text @click="goFirstRating">
            영화 평가하러 가기
            <v-icon small style="margin-left:3vw;">fas fa-arrow-right</v-icon>
          </v-btn>
        </v-card>
        <span>나에게 추천하는 영화</span>
        <MovieList v-if="recommendedMovies.length" v-bind:CinemaList="recommendedMovies"/>
        <v-card class="noReco" v-else>
          <div class="exp">
            현재 데이터가 부족해 영화 추천이 불가능 합니다.
          </div>
          <v-btn text @click="goFirstRating">
            영화 평가하러 가기
            <v-icon small style="margin-left:3vw;">fas fa-arrow-right</v-icon>
          </v-btn>
        </v-card>
      </div>
      <div class="rating" v-else>
        <RatingMovies v-bind:CinemaList="ratedMovies"/>
      </div>
    </div>
    <v-overlay :value="getLoading">
        <v-progress-circular
          :size="70"
          :width="7"
          color="#4520EA"
          indeterminate
        ></v-progress-circular>
      </v-overlay>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import UserInfo from './userInfo/UserInfo.vue';
import MovieList from './movieList/MovieList.vue';
import TheaterList from './movieList/TheaterList.vue';
import SettingCard from './settingCard/SettingCard.vue';
import ChangeUserImage from './changeUserInfo/ChangeUserImage.vue';
import ChangeUserPass from './changeUserInfo/ChangeUserPass.vue';
import RatingMovies from './ratingMovies/RatingMovies.vue';
import router from '../../router';
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title,
    UserInfo,
    MovieList,
    TheaterList,
    SettingCard,
    ChangeUserImage,
    ChangeUserPass,
    RatingMovies
  },
  data() {
    return {
      theaterList: null,
      ratedMovies: null,
      wishMovies: null,
      recommendedOnscreen: [],
      recommendedMovies: [],
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
    ...mapGetters(['getUserInfo', 'getLoading'])
  },
  methods: {
    ...mapMutations(['setLoading']),
    ...mapActions(['bringUserInfo', 'bringRatedMovies']),
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
      if (this.getUserInfo.data.user.file.length) {
        const HOST = process.env.VUE_APP_SERVER_HOST;
        this.profileURL = `${HOST}/${this.getUserInfo.data.user.file[0]}`;
      } else {
        this.profileURL = null;
      }
    }
  },
  async mounted() {
    this.setLoading(true);
    await this.bringUserInfo();
    console.log(this.getUserInfo)
    const HOST = process.env.VUE_APP_SERVER_HOST;
    if (this.getUserInfo.data.user.file.length) {
      this.profileURL = `${HOST}/${this.getUserInfo.data.user.file[0]}`;
    }
    this.userName = this.getUserInfo.data.user.username;
    this.theaterList = this.getUserInfo.data.pick_cinemas;
    this.wishMovies = this.getUserInfo.data.pick_movies;
    this.recommendedOnscreen = this.getUserInfo.data.recommend_onscreen;
    this.recommendedMovies = this.getUserInfo.data.recommend_movies;
    const res = await this.bringRatedMovies();
    this.ratedMovies = res;
    console.log(res)
    this.setLoading(false);
  }
}
</script>

<style src="./UserPage.css" scoped></style>