<template>
  <div class="body">
    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          개봉
        </div>
      </v-col>
      <v-col cols="10">
        <div class="content"
          >
          {{ details.open_date }}
        </div>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          장르
        </div>
      </v-col>
      <v-col cols="10">
        <div
          class="content"
          >
          {{ this.details.genres.join(',') }}
        </div>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          등급
        </div>
      </v-col>
      <v-col cols="10">
        <div
          class="content"
          >
          {{ details.watch_grade }} | {{ details.running_time }}
        </div>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          감독
        </div>
      </v-col>
      <v-col cols="10">
        <div
          class="content"
          >
          {{ this.details.directors.join(',') }}
        </div>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          출연
        </div>
      </v-col>
      <v-col cols="10">
        <div>
          {{ this.details.actors.join(', ') }}
        </div>
      </v-col>
    </v-row>
    
  
    <v-row no-gutters>
      <v-col class="item" cols="2">
        <div>
          줄거리
        </div>
      </v-col>
      <v-col cols="10">
        <div class="content"
          v-bind:style="lineClamp" 
          @click.prevent="toggleSummaryClamp()"
          >
          {{ details.summary }}
        </div>
      </v-col>
    </v-row>
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