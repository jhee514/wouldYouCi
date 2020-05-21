<template>

  <div class="movieInfo">
    <!-- <p>trailer</p> -->

    <p>개봉 {{ movie.fields.open_date }}</p>
    <p>장르 {{ movie.fields.genres }} | {{ movie.fields.running_time }}</p>
    <p>등급 {{ movie.fields.watch_grade }}</p>
    
    <p>감독 {{ movie.fields.directors }}</p>
    <p>출연 {{ movie.fields.actors }}</p>

  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  props:["movie"],
  data() {
    return {
    }
  }
}
</script>

<style src="./MovieInfo.css" scoped></style>