<template>
<v-app>
  <div>
    <Title />
    <div class="movieDetail">
      <div class="header">
        {{ movieTitle }}
      </div>

      <div class="movieTrailer">
        <iframe 
        title=movieTitle
        width=auto 
        height=auto 
        :src=movieTrailerLink
        allowfullscreen 
        frameborder="0" 
        scrolling="no" 
        allow="autoplay"></iframe>
      </div>
      <div class="rating">
        <v-rating
          v-model="movieRating"
          background-color="orange lighten-3"
          color="orange"
          half-increments
          readonly="True"
          dense
        ></v-rating>
        
      </div>

      <v-divider></v-divider>
      <div class="movieInfo">

    
      </div>

      <div class="movieReview">
      </div>
      
    </div>
    <Nav />
  </div>
</v-app>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
  },
  data() {
    return {
      movieTitle: "패왕별희 디 오리지널",
      movieDirector: "누굴까",
      movieTrailerLink: "https://play-tv.kakao.com/embed/player/cliplink/408733684?service=daum_movie",
      movieRating: 3.5,
    }
  }
}
</script>

<style src="./MovieDetail.css" scoped></style>