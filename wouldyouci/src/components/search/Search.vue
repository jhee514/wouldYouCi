<template>
  <div>
    <Title />
    <div class='search'>
      <v-container>
        <v-radio-group dense v-model="searchType" row>
          <v-radio label="영화" value="movies"></v-radio>
          <v-radio label="영화관" value="theater"></v-radio>
        </v-radio-group>
        <form @submit.prevent="changeSearchMode">
          <v-text-field
            v-if="searchType === 'movies'"
            v-model="keyword"
            prepend-icon="fa fa-search"
            :rules="rules"
            :counter="20"
            label="영화 제목을 검색해보세요!"
            required
          ></v-text-field>
          <v-text-field
            v-else
            v-model="keyword"
            prepend-icon="fa fa-search"
            :rules="rules"
            :counter="20"
            label="지역명을 검색해보세요!"
            required
          ></v-text-field>
        </form>
      </v-container>
      <div class="now" v-if="getInitSearchInfo">
        <v-btn small text @click="reBringMyPos">
          <v-icon small>fas fa-crosshairs</v-icon>
          {{ nowAddress }}
        </v-btn>
      </div>
      <div v-if="getSearchMode">
        <MainSearch v-if="getSearchMode==='before'" v-bind:Commings="commings" v-bind:Populars="populars" v-bind:TheaterList="nearTheater"/>
        <AfterSearch v-else v-bind:KeyWords="keywordProps" v-bind:Type="searchTypeProps" v-bind:ResultList="cards" v-bind:Similar="similar"/>
      </div>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import MainSearch from './mainSearch/MainSearch.vue';
import AfterSearch from './afterSearch/AfterSearch.vue';
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'Search',
  components:{
    Nav,
    Title,
    MainSearch,
    AfterSearch
  },
  data() {
    return {
      rules: [
        value => (value || '').length <= 20 || '최대 글자수는 20글자 입니다.'
      ],
      cards: [],
      keyword: null,
      keywordProps: null,
      nowAddress: null,
      similar: [],
      searchType: 'movies',
      searchTypeProps: 'movies',
      pos: null,
      nearTheater: [],
      commings: [],
      populars: [],
    }
  },
  computed: {
    ...mapGetters(['getSearchMode', 'getInitSearchInfo', 'getSearchList', 'getSearchSimiList', 'getAddress'])
  },
  methods: {
    ...mapMutations(['setSearchMode']),
    ...mapActions(['bringInitSearchInfo', 'searchMovies', 'bringAddress', 'searchTheater']),
    async changeSearchMode() {
      this.setSearchMode('after');
      this.keywordProps = this.keyword;
      this.searchTypeProps = this.searchType;
      if (this.searchType === 'movies') {
        await this.searchMovies(this.keyword);
      } else {
        await this.searchTheater(this.keyword);
      }
      this.cards = this.getSearchList;
      this.similar = this.getSearchSimiList;
      this.keyword = null;
    },
    reBringMyPos() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          this.pos = pos;
        }.bind(this))
        setTimeout(async function() {
          await this.bringAddress(this.pos);
          await this.bringInitSearchInfo(this.pos);
          this.nowAddress = this.getAddress;
          console.log(this.getInitSearchInfo);
          this.nearTheater = this.getInitSearchInfo.near_cinema;
          this.commings = this.getInitSearchInfo.comming_soon;
          this.populars = this.getInitSearchInfo.popular_movies;
        }.bind(this), 600)
      } else {
        alert('위치 설정을 켜주세요.');
      }
    }
  },
  mounted() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        this.pos = pos;
      }.bind(this))
      setTimeout(async function() {
        await this.bringAddress(this.pos);
        await this.bringInitSearchInfo(this.pos);
        this.nowAddress = this.getAddress;
        console.log(this.getInitSearchInfo);
        this.nearTheater = this.getInitSearchInfo.near_cinema;
        this.commings = this.getInitSearchInfo.comming_soon;
        this.populars = this.getInitSearchInfo.popular_movies;
      }.bind(this), 250)
    } else {
      alert('위치 설정을 켜주세요.');
    }
  }
}
</script>

<style src="./Search.css" scoped></style>