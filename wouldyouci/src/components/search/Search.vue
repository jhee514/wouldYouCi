<template>
  <div>
    <Title />
    <div class='search'>
      <v-container>
        <form @submit.prevent="changeSearchMode">
          <v-text-field
            v-model="keyword"
            prepend-icon="fa fa-search"
            :rules="rules"
            :counter="20"
            label="영화/ 영화관을 찾아보세요!"
            required
          ></v-text-field>
        </form>
      </v-container>
      <div v-if="getSearchMode">
        <MainSearch v-if="getSearchMode==='before'" v-bind:CinemaList="cards" />
        <AfterSearch v-else v-bind:KeyWords="keywordProps" v-bind:CinemaList="cards" />
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
import { mapGetters, mapMutations } from 'vuex';

export default {
   name: 'Search',
   components:{
    Nav,
    Title,
    MainSearch,
    AfterSearch
   },
   model: [],
   data: () => ({
    rules: [
      value => (value || '').length <= 20 || '최대 글자수는 20글자 입니다.'
    ],
   cards: [
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg'},
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg'},
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg'},
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg'},
    ],
    keyword: null,
    keywordProps: null
  }),
  computed: {
    ...mapGetters(['getSearchMode'])
  },
  methods: {
    ...mapMutations(['setSearchMode']),
    changeSearchMode() {
      this.setSearchMode('after');
      this.keywordProps = this.keyword;
      this.keyword = null;
    }
  }
}
</script>

<style src="./Search.css" scoped></style>