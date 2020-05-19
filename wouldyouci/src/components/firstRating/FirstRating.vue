<template>
  <div>
    <Title />
    <div class="firstRating">
      <v-card class="explanation">
        <v-card-text>
          아래의 영화 중 본 영화에 대해 1~5점 사이의 평점을 남겨주시면
          당신의 취향에 맞는 영화를 추천해드립니다.
          <h4>단, 최소 5개 이상의 영화를 평가해주셔서 추천이 가능합니다.</h4>
        </v-card-text>
      </v-card>
      <v-container fluid>
        <v-row dense justify="center">
          <v-col
            v-for="card in cards"
            :key="card.title"
            cols="12"
            sm="5"
            md="2"
          >
            <v-card class="movieCard">
              <v-img
                :src="card.src"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              >
              </v-img>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-rating
                  v-model="card.rating"
                  color="#F7FE2E"
                  background-color="#F2F2F2"
                ></v-rating>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-spacer></v-spacer>
          <v-btn text>제출</v-btn>
          <v-btn class="next" text>다음에 하기</v-btn>
        </v-row>
      </v-container>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title
  },
  data() {
    return {
      cards: [
        { src: 'https://movie-phinf.pstatic.net/20200506_168/1588731103437Jz8kl_JPEG/movie_image.jpg', rating: 0},
        { src: 'https://movie-phinf.pstatic.net/20200428_196/1588038709486FYyHu_JPEG/movie_image.jpg', rating: 0},
        { src: 'https://movie-phinf.pstatic.net/20200429_215/15881414327594O6hj_JPEG/movie_image.jpg', rating: 0},
      ],
    }
  }
}
</script>

<style src="./FirstRating.css" scoped></style>