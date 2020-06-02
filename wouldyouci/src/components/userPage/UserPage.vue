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
      ratedMovies: null,
      wishMovies: null,
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
    ...mapGetters(['getUserInfo'])
  },
  methods: {
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
    const res = await this.bringRatedMovies();
    this.ratedMovies = res;
    console.log(res)
  }
}
</script>

<style src="./UserPage.css" scoped></style>