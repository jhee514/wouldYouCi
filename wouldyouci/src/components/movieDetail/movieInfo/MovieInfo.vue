<template>
  <div class="movieInfo">
    <p>
      <span class="item">
        개봉 
      </span>
      <span class="content">
      {{ details.open_date }}
      </span>
    </p>
    <p>
      <span class="item">
        장르 
      </span>
      <span 
        class="content"
        v-for="(genre, index) in details.genres"
        :key="index"
        >
      {{ genre }}
      </span>
    </p>
    <p>
      <span class="item">
        등급 
      </span>
      <span class="content">
      {{ details.watch_grade }} | {{ details.running_time }}
      </span>
      </p>
    
    <p>
      <span class="item">
        감독
      </span>
      <span 
        class="content"
        v-for="(director, index) in details.directors"
        :key="index"
        >
      {{ director }}
      </span>
      </p>
    <p>
      <span class="item">
        출연  
      </span>
      <span class="content"
        v-for="(actor, index) in details.actors"
        :key="index"
        >
      {{ actor }}, 
      </span>
    </p>

  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  props:["details"],
  data() {
    return {
    }
  }
}
</script>

<style src="./MovieInfo.css" scoped></style>