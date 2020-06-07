<template>
  <div class="movieInfo">
    <p>
      <span class="item">
        개봉 
      </span>
      <span class="contents">
        <span class="content">
          {{ details.open_date }}
        </span>
      </span>
    </p>

    <p>
      <span class="item">
        장르 
      </span>
      <span class="contents">
        <span 
          class="content"
          v-for="(genre, index) in details.genres"
          :key="index"
          >
          {{ genre }}
        </span>
      </span>
    </p>

    <p>
      <span class="item">
        등급 
      </span>
      <span class="contents">
        <span class="content">
          {{ details.watch_grade }} | {{ details.running_time }}
        </span>
      </span>
    </p>
    
    <p>
      <span class="item">
        감독
      </span>
      <span class="contents">
        <span 
          class="content"
          v-for="(director, index) in details.directors"
          :key="index"
          >
          {{ director }}
        </span>
      </span>
    </p>




    <p>
      <span class="item">
        출연  
      </span>
      <span class="contents">
        <span class="content"
          v-for="(actor, index) in details.actors"
          :key="index"
          >
          {{ actor }}, 
        </span>
      </span>
    </p>




    <p> 
      <span class="item">
        줄거리  
      </span>
      <span class="contents">
        <span class="content"
          v-bind:style="lineClamp" 
          @click.prevent="toggleSummaryClamp()"
          >
          {{ details.summary }}
        </span>
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
      isHidden: true,
      lineClamp: {
        overflow: 'hidden',
        display: '-webkit-box',
        height: 'auto',
        '-webkit-box-orient': 'vertical',
        '-webkit-line-clamp': 3,
      }
    }
  },
  methods: {
    toggleSummaryClamp() {
      console.log(this.summary)
      if ( this.isHidden == false) {
        this.isHidden = true;
        this.lineClamp = {
          overflow: 'hidden',
          display: '-webkit-box',
          height: 'auto',
          '-webkit-box-orient': 'vertical',
          '-webkit-line-clamp': 3,
        }
      } else {
        this.isHidden = false;
        this.lineClamp = {
          display: 'block',
          height: 'auto',
          '-webkit-box-orient': 'vertical',
          '-webkit-line-clamp': 'none',
        }
      }
    },
  }
}
</script>

<style src="./MovieInfo.css" scoped></style>